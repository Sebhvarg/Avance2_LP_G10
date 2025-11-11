# ------------------------------------------------------------ 
# parser.py
# Analizador Sintáctico usando PLY.Yacc
# Grupo 10
# ------------------------------------------------------------

import ply.yacc as yacc
from Avance1.lexer import get_git_user, tokens
import datetime
import os
import subprocess
import sys

# Guarda el último error sintáctico reportado por p_error
last_syntax_error = None
# Lista para acumular todos los errores sintácticos encontrados durante el parseo
syntax_errors = []
# Ruta del archivo de log donde se irán escribiendo los errores a medida que se detectan
log_file_path = None

# ------------------------------------------------------------
# Integrantes:
#   Derian Baque Choez (fernan0502)
#   Sebastian Holguin (Sebhvarg)
# ------------------------------------------------------------


# ------------------------------------------------------------
# Símbolo inicial
# ------------------------------------------------------------
start = 'programa'

def p_programa(p):
    '''programa : funcion
                | programa funcion'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

# ------------------------------------------------------------
# Reglas de la gramática (restauradas)
def p_funcion(p):
    'funcion : FN IDENTIFICADOR PAREN_IZQ PAREN_DER LLAVE_IZQ instrucciones LLAVE_DER'
    p[0] = ('funcion', p[2], p[6])

def p_instrucciones(p):
    '''instrucciones : instruccion
                     | instrucciones instruccion'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_instruccion(p):
    '''instruccion : asignacion
                   | imprimir'''
    p[0] = p[1]

def p_instruccion_error(p):
    'instruccion : error PUNTOCOMA'
    # Regla de recuperación: cuando hay un error dentro de una instrucción,
    # consumir hasta el punto y continuar. Registramos un nodo de error.
    p[0] = ('error_sintactico',)

def p_asignacion(p):
    'asignacion : LET IDENTIFICADOR ASIGNACION expresion PUNTOCOMA'
    p[0] = ('asignacion', p[2], p[4])
def p_re_asignacion(p):
    'asignacion : IDENTIFICADOR ASIGNACION expresion PUNTOCOMA'
    p[0] = ('re_asignacion', p[1], p[3])

def p_valor(p):
    '''valor : NUMERO
             | CADENA
             | CARACTER
             | BOOLEANO'''
    p[0] = p[1]

def p_expresion(p):
    'expresion : valor'
    p[0] = p[1]

def p_expresion_identificador(p):
    'expresion : IDENTIFICADOR'
    p[0] = ('identificador', p[1])
# ==========================================================
# ------------------ Sebastian Holguin ------------------

def p_imprimir(p):
    'imprimir : PRINT PAREN_IZQ expresion PAREN_DER PUNTOCOMA'
    p[0] = ('imprimir', p[3])
    
def p_expresion_parentesis(p):
    'expresion : PAREN_IZQ expresion PAREN_DER'
    p[0] = p[2]
def p_expresion_aritmetica(p):
    '''expresion : expresion operador termino'''
    # Regla izquierda-recursiva que permite encadenar una o más operaciones aritméticas
    # Ejemplo: 1 + 2 + 3 -> ('operacion_aritmetica', '+', ('operacion_aritmetica', '+', 1, 2), 3)
    p[0] = ('operacion_aritmetica', p[2], p[1], p[3])


def p_operador(p):
    '''operador : SUMA
                | RESTA
                | MULT
                | DIV'''
    p[0] = p[1]

def p_termino(p):
    '''termino : valor
               | IDENTIFICADOR
               | PAREN_IZQ expresion PAREN_DER'''
    # 'termino' agrupa los elementos que pueden aparecer a la derecha de un operador
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]
def p_expresion_booleana(p):
    '''expresion : expresion AND expresion
                 | expresion OR expresion
                 | NOT expresion'''
    if len(p) == 4:
        p[0] = ('operacion_booleana', p[2], p[1], p[3])
    else:
        p[0] = ('operacion_booleana', p[1], p[2])

def p_expresion_relacional(p):
    '''expresion : expresion MENOR expresion
                 | expresion MAYOR expresion
                 | expresion MENOR_IGUAL expresion
                 | expresion MAYOR_IGUAL expresion
                 | expresion IGUAL expresion
                 | expresion DIFERENTE expresion'''
    p[0] = ('operacion_relacional', p[2], p[1], p[3])  


# ------------------ Fin  Sebastian Holguin ---------------

# ------------------ Derian Baque ------------------


# ------------------ Fin  Derian Baque ---------------

# ------------------ Carlos Ronquillo ------------------

# ------------------ Fin Carlos Ronquillo ---------------

# ==========================================================

# ------------------------------------------------------------
# Manejo de errores
# ------------------------------------------------------------
def p_error(p):
    global last_syntax_error, syntax_errors
    global log_file_path
    if p is None:
        # fin de entrada inesperado
        msg = "Error de sintaxis: fin de entrada inesperado"
    else:
        lineno = getattr(p, 'lineno', 'desconocida')
        msg = f"Error de sintaxis en la línea {lineno}: token={p.type} valor={p.value}"
    # No imprimir aquí: sólo acumular el error para reportar tras el parseo
    last_syntax_error = msg
    syntax_errors.append(msg)
    # Mostrar inmediatamente en consola y escribir en el archivo de log si está definido
    try:
        print(msg)
        if log_file_path:
            with open(log_file_path, 'a', encoding='utf-8') as lf:
                lf.write(msg + "\n")
    except Exception:
        # No detener el parser por errores al escribir en el log
        pass


# ------------------------------------------------------------
# Construcción del parser
# ------------------------------------------------------------
parser = yacc.yacc()


# ------------------------------------------------------------
# Ejecución principal
# ------------------------------------------------------------
if __name__ == "__main__":
    print("Analizador Sintáctico - Ingrese su algoritmo:")
    if len(sys.argv) > 1:
        archivo = sys.argv[1]
    else:
        archivo = input("Ingrese la ruta del archivo a analizar: ").strip()

    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            codigo = f.read()

        # Crear carpeta de logs
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        usuario = get_git_user()
        fecha_hora = datetime.datetime.now().strftime("%d-%m-%Y-%Hh%M")
        log_file = os.path.join(log_dir, f"sintactico-{usuario}-{fecha_hora}.txt")
        # Exponer la ruta del log para que p_error pueda escribir inmediatamente
        log_file_path = log_file

        # Analizar todo el código
        try:
            # Resetear errores previos antes de parsear
            syntax_errors.clear()
            last_syntax_error = None
            result = parser.parse(codigo)
            # Sólo mostrar errores sintácticos si se encontraron
            with open(log_file, "a", encoding="utf-8") as log_f:
                log_f.write("Resultado del análisis sintáctico:\n")
                if syntax_errors:
                    # Si hubo errores, mostrar únicamente la sección de errores
                    print("\nResultado del análisis sintáctico:")
                    print("Errores sintácticos:")
                    log_f.write("Errores sintácticos:\n")
                    for err in syntax_errors:
                        print(err)
                        log_f.write(f"{err}\n")
                else:
                    # No hubo errores: formatear y escribir el resultado completo
                    print("\nResultado del análisis sintáctico:")
                    def lines_for_result(res, indent=0):
                        """Devuelve una lista de líneas formateadas para 'res'.

                        Reglas simples:
                        - list: iterar elementos al mismo nivel
                        - tuple: si contiene listas, imprimir cabecera (partes no-lista) y luego las listas como elementos indentados
                        - cualquier otro: str(res)
                        """
                        indent_str = '  ' * indent
                        lines = []
                        if res is None:
                            # Si hubo un error sintáctico, escribir el mensaje capturado
                            err = globals().get('last_syntax_error')
                            if err:
                                return [indent_str + err]
                            return [indent_str + '<sin resultado>']
                        if isinstance(res, list):
                            for itm in res:
                                lines.extend(lines_for_result(itm, indent))
                        elif isinstance(res, tuple):
                            # detectar elementos de tipo lista dentro de la tupla
                            nested_lists = [x for x in res if isinstance(x, list)]
                            if nested_lists:
                                # cabecera: partes no-lista (por ejemplo: 'funcion', 'main')
                                header_parts = [x for x in res if not isinstance(x, list)]
                                if header_parts:
                                    lines.append(indent_str + str(tuple(header_parts)))
                                # ahora iterar cada lista encontrada
                                for lst in nested_lists:
                                    for itm in lst:
                                        lines.extend(lines_for_result(itm, indent + 1))
                            else:
                                lines.append(indent_str + str(res))
                        else:
                            lines.append(indent_str + str(res))
                        return lines

                    lines = lines_for_result(result)
                    for line in lines:
                        print(line)
                        log_f.write(f"{line}\n")
        except Exception as ex:
            print(f" Error en el análisis: {ex}")
            with open(log_file, "a", encoding="utf-8") as log_f:
                log_f.write(f"Error en el análisis: {ex}\n")

    except FileNotFoundError:
        print(f" Error: No se encontró el archivo '{archivo}'")
    except Exception as ex:
        print(f" Error al leer el archivo '{archivo}': {ex}")

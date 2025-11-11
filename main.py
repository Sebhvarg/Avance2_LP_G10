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
# Reglas de la gramática
# ------------------------------------------------------------
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
    
def expresion_parentesis(p):
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
    global last_syntax_error
    if p is None:
        # fin de entrada inesperado
        msg = "Error de sintaxis: fin de entrada inesperado"
        print(msg)
        last_syntax_error = msg
    else:
        lineno = getattr(p, 'lineno', 'desconocida')
        msg = f"Error de sintaxis en la línea {lineno}: token={p.type} valor={p.value}"
        print(msg)
        last_syntax_error = msg


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

        # Analizar todo el código
        try:
            result = parser.parse(codigo)
            # Imprimir y escribir en el log cada detección en una línea separada
            print("\nResultado del análisis sintáctico:")
            with open(log_file, "a", encoding="utf-8") as log_f:
                log_f.write("Resultado del análisis sintáctico:\n")

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

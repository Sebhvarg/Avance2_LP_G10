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
#   Carlos Ronquillo (carrbrus)
# ------------------------------------------------------------

# ------------------------------------------------------------
# Símbolo inicial
# ------------------------------------------------------------
start = 'programa'

def p_programa(p):
    '''programa : funcion
                | programa funcion
                | clase
                | programa clase'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

# ------------------------------------------------------------
# Reglas de la gramática (Derian + Sebastian)
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
                   | imprimir
                   | condicional
                   | condicional_else
                   | condicional_elif
                   | input
                   | for_loop
                   | while_loop
                   | return_stmt
                   | llamada_funcion
                   | uso_clase'''
    p[0] = p[1]

def p_instruccion_error(p):
    'instruccion : error PUNTOCOMA'
    p[0] = ('error_sintactico',)

def p_asignacion(p):
    'asignacion : LET IDENTIFICADOR ASIGNACION expresion PUNTOCOMA'
    p[0] = ('asignacion', p[2], p[4])

def p_re_asignacion(p):
    'asignacion : IDENTIFICADOR ASIGNACION expresion PUNTOCOMA'
    p[0] = ('re_asignacion', p[1], p[3])

def p_valor(p):
    '''valor : ENTERO
             | FLOTANTE
             | CADENA
             | CARACTER
             | BOOLEANO'''
    p[0] = p[1]

def p_expresion_valor(p):
    'expresion : valor'
    p[0] = p[1]

def p_expresion_identificador(p):
    'expresion : IDENTIFICADOR'
    p[0] = ('identificador', p[1])

# ------------------ Sebastian Holguin ------------------

def p_imprimir(p):
    'imprimir : PRINT PAREN_IZQ expresion PAREN_DER PUNTOCOMA'
    p[0] = ('imprimir', p[3])

def p_expresion_parentesis(p):
    'expresion : PAREN_IZQ expresion PAREN_DER'
    p[0] = p[2]

def p_expresion_aritmetica(p):
    '''expresion : expresion operador termino'''
    p[0] = ('operacion_aritmetica', p[2], p[1], p[3])

def p_operador(p):
    '''operador : SUMA
                | RESTA
                | MULT
                | DIV
                | MODULO'''
    p[0] = p[1]

def p_termino(p):
    '''termino : valor
               | IDENTIFICADOR
               | PAREN_IZQ expresion PAREN_DER'''
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

def p_condicional_elif(p):
    'condicional_elif : IF PAREN_IZQ expresion PAREN_DER LLAVE_IZQ instrucciones LLAVE_DER ELSE instruccion'
    p[0] = ('condicional_elif', p[3], p[6], p[9])

def p_expresion_ternaria(p):
    'expresion : expresion INTERROGACION expresion DOSPUNTOS expresion'
    p[0] = ('expresion_ternaria', p[1], p[3], p[5])  

# ------------------ Derian Baque ------------------

def p_input(p):
    'input : INPUT PAREN_IZQ CADENA PAREN_DER PUNTOCOMA'
    p[0] = ('input', p[3])

def p_condicional(p):
    'condicional : IF PAREN_IZQ expresion PAREN_DER LLAVE_IZQ instrucciones LLAVE_DER'
    p[0] = ('condicional', p[3], p[6])

def p_condicional_else(p):
    'condicional_else : IF PAREN_IZQ expresion PAREN_DER LLAVE_IZQ instrucciones LLAVE_DER ELSE LLAVE_IZQ instrucciones LLAVE_DER'
    p[0] = ('condicional_else', p[3], p[6], p[10])

def p_lista(p):
    'expresion : CORCHETE_IZQ elementos CORCHETE_DER'
    p[0] = ('lista', p[2])

def p_elementos(p):
    '''elementos : expresion
                 | elementos COMA expresion'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

# ------------------ Carlos Ronquillo ------------------

def p_acceso_indice(p):
    'expresion : IDENTIFICADOR CORCHETE_IZQ expresion CORCHETE_DER'
    p[0] = ('acceso_indice', p[1], p[3])

def p_for_loop(p):
    'for_loop : FOR PAREN_IZQ IDENTIFICADOR IN expresion PAREN_DER LLAVE_IZQ instrucciones LLAVE_DER'
    p[0] = ('for_in', p[3], p[5], p[9])

def p_while_loop(p):
    'while_loop : WHILE PAREN_IZQ expresion PAREN_DER LLAVE_IZQ instrucciones LLAVE_DER'
    p[0] = ('while', p[3], p[6])

def p_return_stmt(p):
    'return_stmt : RETURN expresion PUNTOCOMA'
    p[0] = ('return', p[2])

def p_llamada_funcion(p):
    '''llamada_funcion : IDENTIFICADOR PAREN_IZQ PAREN_DER
                       | IDENTIFICADOR PAREN_IZQ elementos PAREN_DER'''
    if len(p) == 4:
        p[0] = ('call_func', p[1], [])
    else:
        p[0] = ('call_func', p[1], p[3])

# ============================================================
# Clases, Propiedades y Métodos
# ============================================================

def p_clase(p):
    'clase : CLASS IDENTIFICADOR LLAVE_IZQ cuerpo_clase LLAVE_DER'
    p[0] = ('clase', p[2], p[4])

def p_cuerpo_clase(p):
    '''cuerpo_clase : lista_miembros'''
    p[0] = p[1]

def p_lista_miembros(p):
    '''lista_miembros : lista_miembros miembro
                      | miembro'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_miembro(p):
    '''miembro : propiedad
               | metodo'''
    p[0] = p[1]

def p_propiedad(p):
    'propiedad : LET IDENTIFICADOR ASIGNACION expresion PUNTOCOMA'
    p[0] = ('propiedad', p[2], p[4])

def p_metodo(p):
    'metodo : FN IDENTIFICADOR PAREN_IZQ parametros_opt PAREN_DER LLAVE_IZQ cuerpo LLAVE_DER'
    p[0] = ('metodo', p[2], p[4], p[7])

def p_parametros_opt(p):
    '''parametros_opt : parametros
                      | empty'''
    p[0] = p[1]

def p_parametros(p):
    '''parametros : IDENTIFICADOR
                  | parametros COMA IDENTIFICADOR'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_cuerpo(p):
    'cuerpo : instrucciones'
    p[0] = p[1]

def p_uso_clase(p):
    'uso_clase : IDENTIFICADOR PUNTO IDENTIFICADOR PAREN_IZQ parametros_opt PAREN_DER PUNTOCOMA'
    p[0] = ('uso_clase', p[1], p[3], p[5])

def p_empty(p):
    'empty :'
    p[0] = None

# ------------------------------------------------------------
# Manejo de errores
# ------------------------------------------------------------
def p_error(p):
    global last_syntax_error, syntax_errors, log_file_path
    if p is None:
        msg = "Error de sintaxis: fin de entrada inesperado"
    else:
        lineno = getattr(p, 'lineno', 'desconocida')
        msg = f"Error de sintaxis en la línea {lineno}: token={p.type} valor={p.value}"
    print(msg)
    syntax_errors.append(msg)
    if log_file_path:
        with open(log_file_path, 'a', encoding='utf-8') as lf:
            lf.write(msg + "\n")
    parser.errok()

# ------------------------------------------------------------
# Construcción del parser
# ------------------------------------------------------------
parser = yacc.yacc()

# ------------------------------------------------------------
# Ejecución principal
# ------------------------------------------------------------
if __name__ == "__main__":
    print("Analizador Sintáctico - Ingrese su algoritmo:")
    archivo = sys.argv[1] if len(sys.argv) > 1 else input("Ingrese la ruta del archivo a analizar: ").strip()
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            codigo = f.read()
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        usuario = get_git_user()
        fecha_hora = datetime.datetime.now().strftime("%d-%m-%Y-%Hh%M")
        log_file_path = os.path.join(log_dir, f"sintactico-{usuario}-{fecha_hora}.txt")
        syntax_errors.clear()
        result = parser.parse(codigo)
        print("\nResultado del análisis sintáctico:")
        if syntax_errors:
            print("Errores sintácticos:")
            for err in syntax_errors:
                print(err)
        else:
            print(result)
    except Exception as ex:
        print(f"Error al analizar: {ex}")


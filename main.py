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

def p_valor(p):
    '''valor : NUMERO
             | CADENA
             | CARACTER
             | BOOLEANO'''
    p[0] = p[1]

def p_expresion(p):
    'expresion : valor'
    p[0] = p[1]

def p_expresion_binaria(p):
    '''expresion : expresion SUMA expresion
                 | expresion RESTA expresion
                 | expresion MULT expresion
                 | expresion DIV expresion'''
    p[0] = ('binaria', p[2], p[1], p[3])

def p_expresion_identificador(p):
    'expresion : IDENTIFICADOR'
    p[0] = ('identificador', p[1])

# ==========================================================
# ------------------ Sebastian Holguin ------------------

def p_imprimir(p):
    'imprimir : PRINT PAREN_IZQ expresion PAREN_DER PUNTOCOMA'
    p[0] = ('imprimir', p[3])
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
    if p is None:
        print("Error de sintaxis: fin de entrada inesperado")
    else:
        lineno = getattr(p, 'lineno', 'desconocida')
        print(f"Error de sintaxis en la línea {lineno}: token={p.type} valor={p.value}")


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
        log_dir = "log"
        os.makedirs(log_dir, exist_ok=True)
        usuario = get_git_user()
        fecha_hora = datetime.datetime.now().strftime("%d-%m-%Y-%Hh%M")
        log_file = os.path.join(log_dir, f"sintactico-{usuario}-{fecha_hora}.txt")

        # Analizar todo el código
        try:
            result = parser.parse(codigo)
            print("\nResultado del análisis sintáctico:\n", result)
            with open(log_file, "a", encoding="utf-8") as log_f:
                log_f.write(f"Resultado del análisis sintáctico:\n{result}\n")
        except Exception as ex:
            print(f" Error en el análisis: {ex}")
            with open(log_file, "a", encoding="utf-8") as log_f:
                log_f.write(f"Error en el análisis: {ex}\n")

    except FileNotFoundError:
        print(f" Error: No se encontró el archivo '{archivo}'")
    except Exception as ex:
        print(f" Error al leer el archivo '{archivo}': {ex}")

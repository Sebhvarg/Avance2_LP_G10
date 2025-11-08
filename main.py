# ------------------------------------------------------------ 
# lexer.py
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



#Funcion de error definida

# ------------------------------------------------------------
# Reglas de la gramática

def p_asignacion(p):
    'asignacion : LET IDENTIFICADOR ASIGNACION expresion PUNTOCOMA'
    p[0] = ('asignacion', p[1], p[3])
    
def p_valor(p):
    '''valor : NUMERO
             | CADENA
             | CARACTER
             | BOOLEANO'''
    p[0] = ('valor', p[1])


def p_expresion(p):
    """expresion : valor"""
    # Simple expression rule (expand later): an expresion can be a single valor
    p[0] = ('expresion', p[1])
  

# Error rule for syntax errors
def p_error(p):
    # p can be None when the parser reaches EOF or an unexpected token
    if p is None:
        print("Error de sintaxis: fin de entrada inesperado")
    else:
        # Some tokens may not carry a lineno attribute; guard accordingly
        lineno = getattr(p, 'lineno', 'desconocida')
        print(f"Error de sintaxis en la línea {lineno}: token={p.type} valor={p.value}")

# Build the parser
parser = yacc.yacc()


if __name__ == "__main__":
    print("Analizador Sintáctico - Ingrese su algoritmo:")
    e = 0
    if len(sys.argv) > 1:
        archivo = sys.argv[1]
    else:
        archivo = input("Ingrese la ruta del archivo a analizar: ").strip()
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lines = f.readlines()

            # Prepare log file
            log_dir = "log"
            os.makedirs(log_dir, exist_ok=True)
            usuario = get_git_user()
            fecha_hora = datetime.datetime.now().strftime("%d-%m-%Y-%Hh%M")
            log_file = os.path.join(log_dir, f"sintactico-{usuario}-{fecha_hora}.txt")


            with open(log_file, "a", encoding="utf-8") as log_f:
                for lineno, raw_line in enumerate(lines, start=1):
                    line = raw_line.rstrip('\n')
                    text = line.strip()
                    if not line.strip():
                        continue
                    try:
                        result = parser.parse(line)
                        print(f"Linea {lineno}: {text} \n ==> { result}")
                        log_f.write(f"Linea {lineno}: {text} \n ==> { result}\n")
                    except Exception as ex:
           
                        err_msg = f"Error en linea {lineno}: {ex}"
                        print(err_msg)
                        log_f.write(err_msg + "\n")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}'")
    except Exception as ex:
        print(f"Error al leer el archivo '{archivo}': {ex}")
   
        
           
        
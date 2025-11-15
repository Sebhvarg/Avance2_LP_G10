# Yacc example

import ply.yacc as yacc
import sys
import datetime
import os
import subprocess

# Get the token map from the lexer.  This is required.
from Avance1.lexer import tokens, get_git_user

mensajes = []
# ------------------------------------------------------------   
def p_programa(p):
    '''programa : instrucciones
                | programa instrucciones
                '''
       
def p_instrucciones(p):
    '''instrucciones : asignacion
                 | imprimir
                 | funcion
             
                 ''' 
def p_funcion(p):
    'funcion : FUNCION IDENTIFICADOR PAREN_IZQ PAREN_DER LLAVE_IZQ programa LLAVE_DER'

def p_funcion_parametros(p):
    'funcion : FUNCION IDENTIFICADOR PAREN_IZQ parametros PAREN_DER LLAVE_IZQ programa LLAVE_DER'

def p_parametros(p):
    '''parametros : IDENTIFICADOR
                  | IDENTIFICADOR COMA parametros
    '''
      
def p_asignacion(p):
    'asignacion : VARIABLE IDENTIFICADOR IGUAL valor PUNTOCOMA'
    
def  p_valor(p):
    '''valor : CADENA
             | CARACTER
             | BOOLEANO
             | VARIABLE 
             | valor_numerico
             | operacion_aritmetica'''
    

def p_valor_numerico(p):
    '''valor_numerico : ENTERO
                      | FLOTANTE'''
    

def p_valor_operacionAritmetica(p):
    '''operacion_aritmetica : valor_numerico operador_aritmetico valor_numerico
    | repite_operacion_aritmetica 
    '''
   
    
def p_operador_aritmetico(p):
    '''operador_aritmetico : SUMA
                           | RESTA
                           | MULT
                           | DIV
                           | MODULO'''

def p_repite_operacionAritmetica(p):
    '''repite_operacion_aritmetica : operacion_aritmetica 
                                    | operacion_aritmetica operador_aritmetico valor_numerico'''

def p_imprimir(p):
    '''imprimir : IMPRIMIR PAREN_IZQ repite_valores PAREN_DER PUNTOCOMA
    | IMPRIMIRLN PAREN_IZQ repite_valores PAREN_DER PUNTOCOMA

    '''
    
def p_repite_valores(p):
    '''repite_valores : valor
                      | valor COMA repite_valores'''
                      

# Error rule for syntax errors
def p_error(p):
    print("Error sintáctico en la linea %d" % p.lineno if p else "Error sintáctico al final del archivo")
    print(p);
    mensaje_error = f"Error sintáctico en la linea {p.lineno}" if p else "Error sintáctico al final del archivo"
    mensajes.append(mensaje_error)
        
# ------------------------------------------------------------
# Función para registrar los tokens en un archivo de log
def log_token(mensaje):
    usuario = get_git_user()
    fecha_hora = datetime.datetime.now().strftime("%d-%m-%Y-%Hh%M")
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, f"sintactico-{usuario}-{fecha_hora}.txt")
    with open(log_file_path, 'a', encoding='utf-8') as log_file:
        log_file.write(mensaje + "\n")
    

# Build the parser
parser = yacc.yacc()

if __name__ == "__main__":
    print("Analizador sintáctico ARust \n")
    if len(sys.argv) > 1:
        archivo_entrada = sys.argv[1]
    else:
        archivo_entrada = input("Ingrese el nombre del archivo de entrada: ").strip()
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            datos = archivo.read()

        # Crear el archivo de log desde el inicio
        log_token("Inicio análisis sintáctico del archivo: " + archivo_entrada)

        # Ejecutar análisis sintáctico
        parser.parse(datos)
        

        while True:
            if not mensajes:
                print("Análisis sintáctico completado sin errores.")
                log_token("Análisis sintáctico completado sin errores.")
                break
            else:
                for mensaje in mensajes:
                    log_token(mensaje)
                break

        print("\nTokens registrados en archivo de log.")
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no fue encontrado.")

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no fue encontrado.")
        
        
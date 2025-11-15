# ------------------------------------------------------------ 
# parser.py
# Analizador Sintáctico usando PLY.Yacc
# Grupo 10
# ------------------------------------------------------------

import ply.yacc as yacc
import sys
import datetime
import os
from Avance1.lexer import tokens, get_git_user
# ------------------------------------------------------------
# Integrantes:
#   Derian Baque Choez (fernan0502)
#   Sebastian Holguin (Sebhvarg)
#   Carlos Ronquillo (carrbrus)
# ------------------------------------------------------------

mensajes = [] #Guarda los errores

# ------------------------------------------------------------   
def p_programa(p):
    '''programa : instrucciones
                | programa instrucciones
                '''
       
def p_instrucciones(p):
    '''instrucciones : asignacion
                 | imprimir
                 | funcion
                 | estructura_control
                 | bloque
                 | llamada_funcion
                 ''' 
#sombrado
def p_bloque(p):
    '''bloque : LLAVE_IZQ programa LLAVE_DER
    '''
    
# ------------------------------------------------------------
# Reglas de la gramática (Derian + Sebastian)
def p_asignacion(p):
    '''asignacion : VARIABLE IDENTIFICADOR IGUAL valor PUNTOCOMA
                    | IDENTIFICADOR IGUAL valor PUNTOCOMA                    
    '''
def p_asignacion_mutable(p):
    '''asignacion : VARIABLE MUTABLE IDENTIFICADOR IGUAL valor PUNTOCOMA'''
def p_asignacion_constante(p):
    '''asignacion : CONSTANTE IDENTIFICADOR IGUAL valor PUNTOCOMA'''
def p_asignacion_explicita_valor(p):
    '''asignacion : VARIABLE IDENTIFICADOR DOSPUNTOS tipo_dato IGUAL valor PUNTOCOMA
    '''
    
def  p_valor(p):
    '''valor : CADENA
             | CARACTER
             | BOOLEANO
             | IDENTIFICADOR
             | asignacion 
             | valor_numerico
             | operacion_aritmetica
             | tupla
             | matriz
             | llamada_funcion_sin_puntocoma'''

def p_valor_booleano(p):
    '''valor : VERDAD
             | FALSO'''

def p_valor_numerico(p):
    '''valor_numerico : ENTERO
                      | FLOTANTE'''

def p_tipo_dato(p):
    '''tipo_dato : ITIPO
                 | I8
                 | I16
                 | I32
                 | I64
                 | I128
                 | U8
                 | U16
                 | U32
                 | U64
                 | U128
                 | F32
                 | F64
                 | BOOLEANO_TIPO
                 | CARACTER_TIPO
                 | CADENA_TIPO
                 | UTIPO
                 
    '''


def p_valor_operacionAritmetica(p):
    '''operacion_aritmetica : valor operador_aritmetico valor
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
def p_expresion_booleana(p):
    '''expresion_booleana : valor operador_relacional valor    
    '''

def p_operador_relacional(p):
    '''operador_relacional : MAYOR
                           | MENOR
                           | MAYOR_IGUAL
                           | MENOR_IGUAL
                           | IGUALDOBLE
                           | DIFERENTE'''
# ------------------ Funciones ------------------
def p_imprimir(p):
    '''imprimir : IMPRIMIR PAREN_IZQ repite_valores PAREN_DER PUNTOCOMA
    | IMPRIMIRLN PAREN_IZQ repite_valores PAREN_DER PUNTOCOMA
    '''
    
def p_repite_valores(p):
    '''repite_valores : valor
                      | valor COMA repite_valores'''
def p_funcion(p):
    'funcion : FUNCION IDENTIFICADOR PAREN_IZQ PAREN_DER LLAVE_IZQ programa LLAVE_DER'

def p_funcion_parametros(p):
    'funcion : FUNCION IDENTIFICADOR PAREN_IZQ parametros PAREN_DER LLAVE_IZQ programa LLAVE_DER'

def p_parametros(p):
    '''parametros : IDENTIFICADOR
                  | IDENTIFICADOR COMA parametros
                  | IDENTIFICADOR DOSPUNTOS tipo_dato 
                  | IDENTIFICADOR DOSPUNTOS tipo_dato COMA parametros
    '''

def p_llamada_funcion(p):
    '''llamada_funcion : IDENTIFICADOR PAREN_IZQ PAREN_DER PUNTOCOMA
                       | IDENTIFICADOR PAREN_IZQ repite_valores PAREN_DER PUNTOCOMA
    '''

def p_llamada_funcion_sin_puntocoma(p):
    '''llamada_funcion_sin_puntocoma : IDENTIFICADOR PAREN_IZQ PAREN_DER
                                     | IDENTIFICADOR PAREN_IZQ repite_valores PAREN_DER
    '''
# -------- Estructuras de datos ----------------------

def p_estructura_datos(p):
    '''estructura_datos : tupla
                        | matriz
    '''
def p_tupla(p):
    '''tupla : PAREN_IZQ repite_valores PAREN_DER
            | PAREN_IZQ PAREN_DER
            | PAREN_IZQ repite_valores COMA tupla PAREN_DER
    '''
def p_tupla_acceso(p):
    '''valor : IDENTIFICADOR PUNTO ENTERO
    '''

def p_tupla_asignacion(p):
    '''asignacion : VARIABLE IDENTIFICADOR IGUAL tupla PUNTOCOMA
    | VARIABLE MUTABLE IDENTIFICADOR IGUAL tupla PUNTOCOMA
    | IDENTIFICADOR IGUAL tupla PUNTOCOMA
    '''
def p_matriz(p):
    '''matriz : CORCHETE_IZQ repite_valores CORCHETE_DER
              | CORCHETE_IZQ CORCHETE_DER
    '''

def p_matriz_asignacion(p):
    '''asignacion : VARIABLE IDENTIFICADOR IGUAL matriz PUNTOCOMA
                  | VARIABLE MUTABLE IDENTIFICADOR IGUAL matriz PUNTOCOMA
                  | IDENTIFICADOR IGUAL matriz PUNTOCOMA
    '''
def p_matriz_acceso(p):
    '''valor : IDENTIFICADOR CORCHETE_IZQ ENTERO CORCHETE_DER
    '''
# ------- Estructuras de control ----------------------
def p_estructura_control(p):
    '''estructura_control : condicional_if
                         | ciclo_while
                         | ciclo_for
    '''

def p_condicional_if(p):
    '''condicional_if : SI PAREN_IZQ expresion_booleana PAREN_DER LLAVE_IZQ programa LLAVE_DER
                        | SI PAREN_IZQ expresion_booleana PAREN_DER LLAVE_IZQ programa LLAVE_DER SINO LLAVE_IZQ programa LLAVE_DER
                        | SI PAREN_IZQ expresion_booleana PAREN_DER LLAVE_IZQ programa LLAVE_DER condicional_elif
    '''
def p_condicional_elif(p):
    '''condicional_elif : SINO SI PAREN_IZQ expresion_booleana PAREN_DER LLAVE_IZQ programa LLAVE_DER
                        | SINO SI PAREN_IZQ expresion_booleana PAREN_DER LLAVE_IZQ programa LLAVE_DER condicional_elif
                        | SINO SI PAREN_IZQ expresion_booleana PAREN_DER LLAVE_IZQ programa LLAVE_DER SINO LLAVE_IZQ programa LLAVE_DER
    '''
def p_ciclo_while(p):
    'ciclo_while : MIENTRAS PAREN_IZQ expresion_booleana PAREN_DER LLAVE_IZQ programa LLAVE_DER'
def p_ciclo_for(p):
    'ciclo_for : POR PAREN_IZQ asignacion expresion_booleana PUNTOCOMA asignacion_incremento PAREN_DER LLAVE_IZQ programa LLAVE_DER'
def p_asignacion_incremento(p):
    '''asignacion_incremento : IDENTIFICADOR MAS_IGUAL ENTERO
                                | IDENTIFICADOR MENOS_IGUAL ENTERO
                                | IDENTIFICADOR SUMA SUMA
                                | IDENTIFICADOR RESTA RESTA
                                | IDENTIFICADOR IGUAL IDENTIFICADOR SUMA ENTERO
                
    '''
# ------------------------------------------------------------
    
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
        
        
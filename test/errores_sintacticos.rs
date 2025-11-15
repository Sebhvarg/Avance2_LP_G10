// ==================== ERRORES SINTÁCTICOS ====================
// Este archivo contiene ejemplos de errores sintácticos
// según la gramática definida en sintax.py

// ==================== ERROR 1: Falta punto y coma en asignación ====================
fn test_error_1() {
    let x = 5  // ERROR: falta PUNTOCOMA
    let y = 10;
}

// ==================== ERROR 2: Falta VARIABLE (let) en asignación ====================
fn test_error_2() {
    x = 5;  // ERROR: falta VARIABLE (let)
}

// ==================== ERROR 3: Falta paréntesis en condición if ====================
fn test_error_3() {
    let x = 5;
    if x < 10 {  // ERROR: falta PAREN_IZQ y PAREN_DER
        println!("menor");
    }
}

// ==================== ERROR 4: Falta llaves en bloque if ====================
fn test_error_4() {
    let x = 5;
    if (x < 10)  // ERROR: falta LLAVE_IZQ
        println!("menor");  // ERROR: falta LLAVE_DER
}

// ==================== ERROR 5: Falta llaves en función ====================
fn test_error_5()  // ERROR: falta LLAVE_IZQ
    println!("error");  // ERROR: falta LLAVE_DER

// ==================== ERROR 6: Falta paréntesis en función ====================
fn test_error_6 {  // ERROR: falta PAREN_IZQ y PAREN_DER
    println!("error");
}

// ==================== ERROR 7: Operador aritmético inválido ====================
fn test_error_7() {
    let x = 5 ** 2;  // ERROR: ** no es un operador válido (debería ser ^)
}

// ==================== ERROR 8: Falta operador en expresión ====================
fn test_error_8() {
    let x = 5 10;  // ERROR: falta operador entre 5 y 10
}

// ==================== ERROR 9: Falta valor en asignación ====================
fn test_error_9() {
    let x = ;  // ERROR: falta valor después de IGUAL
}

// ==================== ERROR 10: Falta identificador en asignación ====================
fn test_error_10() {
    let = 5;  // ERROR: falta IDENTIFICADOR
}

// ==================== ERROR 11: Falta punto y coma en print ====================
fn test_error_11() {
    println!("mensaje")  // ERROR: falta PUNTOCOMA
}

// ==================== ERROR 12: Falta paréntesis en print ====================
fn test_error_12() {
    println!"mensaje";  // ERROR: falta PAREN_IZQ y PAREN_DER
}

// ==================== ERROR 13: Falta coma en múltiples valores ====================
fn test_error_13() {
    println!("valor1" "valor2");  // ERROR: falta COMA entre valores
}

// ==================== ERROR 14: Falta paréntesis en while ====================
fn test_error_14() {
    let mut x = 0;
    while x < 5 {  // ERROR: falta PAREN_IZQ y PAREN_DER
        x = x + 1;
    }
}

// ==================== ERROR 15: Falta punto y coma en for ====================
fn test_error_15() {
    for (i = 0 i < 10; i = i + 1) {  // ERROR: falta PUNTOCOMA después de i = 0
        println!(i);
    }
}

// ==================== ERROR 16: Falta else después de else if ====================
fn test_error_16() {
    let x = 5;
    if (x < 10) {
        println!("menor");
    } else if (x < 20)  // ERROR: falta LLAVE_IZQ y LLAVE_DER
}

// ==================== ERROR 17: Tipo de dato incorrecto ====================
fn test_error_17() {
    let x: integer = 5;  // ERROR: integer no es un tipo válido (debería ser i32, i64, etc.)
}

// ==================== ERROR 18: Falta dos puntos en tipo explícito ====================
fn test_error_18() {
    let x i32 = 5;  // ERROR: falta DOSPUNTOS antes de i32
}

// ==================== ERROR 19: Falta igual en asignación ====================
fn test_error_19() {
    let x: i32 5;  // ERROR: falta IGUAL
}

// ==================== ERROR 20: Tupla mal formada ====================
fn test_error_20() {
    let tupla = (1, 2, 3,);  // ERROR: coma al final sin más elementos
}

// ==================== ERROR 21: Acceso a tupla sin punto ====================
fn test_error_21() {
    let tupla = (1, 2, 3);
    let x = tupla 0;  // ERROR: falta PUNTO
}

// ==================== ERROR 22: Array sin corchetes de cierre ====================
fn test_error_22() {
    let arr = [1, 2, 3;  // ERROR: falta CORCHETE_DER
}

// ==================== ERROR 23: Acceso a array sin corchetes ====================
fn test_error_23() {
    let arr = [1, 2, 3];
    let x = arr(0);  // ERROR: debería usar CORCHETE_IZQ y CORCHETE_DER, no paréntesis
}

// ==================== ERROR 24: Función sin flecha con tipo de retorno ====================
fn test_error_24() i32 {  // ERROR: falta FLECHA (->)
    5
}

// ==================== ERROR 25: Parámetro sin tipo ====================
fn test_error_25(x) {  // ERROR: falta DOSPUNTOS y tipo_dato
    println!(x);
}

// ==================== ERROR 26: Falta coma entre parámetros ====================
fn test_error_26(x: i32 y: i32) {  // ERROR: falta COMA entre parámetros
    println!(x, y);
}

// ==================== ERROR 27: Llamada a función sin punto y coma ====================
fn test_error_27() {
    saludar()  // ERROR: falta PUNTOCOMA
}

// ==================== ERROR 28: Struct sin llaves ====================
struct Persona  // ERROR: falta LLAVE_IZQ
    nombre: String,
    edad: u8,
}  // ERROR: estructura mal formada

// ==================== ERROR 29: Atributo de struct sin coma ====================
struct Punto {
    x: i32
    y: i32,  // ERROR: falta COMA después de x: i32
}

// ==================== ERROR 30: Atributo sin tipo ====================
struct Rectangulo {
    ancho,  // ERROR: falta DOSPUNTOS y tipo_dato
    alto: u32,
}

// ==================== ERROR 31: Operador relacional inválido ====================
fn test_error_31() {
    let x = 5;
    if (x <> 10) {  // ERROR: <> no es válido (debería ser !=)
        println!("diferente");
    }
}

// ==================== ERROR 32: Bloque de retorno sin llaves ====================
fn test_error_32() {
    let x = 
        let a = 5;  // ERROR: falta LLAVE_IZQ para iniciar bloque
        a + 10
    ;  // ERROR: falta LLAVE_DER para cerrar bloque
}

// ==================== ERROR 33: Expresión sin punto y coma en medio del bloque ====================
fn test_error_33() {
    let x = 5
    x + 10  // ERROR: la primera línea necesita PUNTOCOMA
}

// ==================== ERROR 34: Incremento en for mal formado ====================
fn test_error_34() {
    for (i = 0; i < 10; i+) {  // ERROR: i+ no es válido (debería ser i = i + 1 o i += 1)
        println!(i);
    }
}

// ==================== ERROR 35: Asignación mutable sin valor ====================
fn test_error_35() {
    let mut x;  // ERROR: falta IGUAL y valor
}

// ==================== ERROR 36: Constante sin inicialización ====================
fn test_error_36() {
    const PI: f32;  // ERROR: falta IGUAL y valor
}

// ==================== ERROR 37: While sin llaves ====================
fn test_error_37() {
    let mut x = 0;
    while (x < 5)  // ERROR: falta LLAVE_IZQ
        x = x + 1;  // ERROR: falta LLAVE_DER
}

// ==================== ERROR 38: For sin paréntesis ====================
fn test_error_38() {
    for i = 0; i < 10; i = i + 1 {  // ERROR: falta PAREN_IZQ y PAREN_DER
        println!(i);
    }
}

// ==================== ERROR 39: Función main sin fn ====================
main() {  // ERROR: falta FUNCION (fn)
    println!("error");
}

// ==================== ERROR 40: Valor booleano incorrecto ====================
fn test_error_40() {
    let activo = verdadero;  // ERROR: verdadero no es válido (debería ser true)
}

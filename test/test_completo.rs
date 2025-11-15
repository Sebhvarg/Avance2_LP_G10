// Test completo del analizador sintáctico ARust
// Prueba todas las características implementadas

// ==================== FUNCIONES ====================
fn main() {
    println!("=== Test Completo ARust ===");
    
    // ==================== ASIGNACIONES ====================
    // Asignación simple
    let x = 5;
    let y = 10;
    
    // Asignación mutable
    let mut contador = 0;
    
    // Asignación constante
    const PI = 3.14;
    
    // Asignación con tipo explícito
    let edad: i32 = 25;
    let altura: f32 = 1.75;
    let nombre: String = "Sebastian";
    let letra: char = 'A';
    let activo: bool = true;
    
    // ==================== OPERACIONES ARITMÉTICAS ====================
    let suma = x + y;
    let resta = y - x;
    let mult = x * y;
    let div = y / x;
    let modulo = y % x;
    let complejo = x + y * 2 - 5;
    
    // ==================== EXPRESIONES BOOLEANAS ====================
    if (x < y) {
        println!("x es menor que y");
    }
    
    if (x > 0) {
        println!("x es positivo");
    }
    
    if (x == 5) {
        println!("x es igual a 5");
    }
    
    if (x != y) {
        println!("x es diferente de y");
    }
    
    // ==================== BLOQUES CON RETORNO ====================
    let resultado = {
        let a = 10;
        let b = 20;
        a + b
    };
    
    // ==================== TUPLAS ====================
    let tupla1 = (1, 2, 3);
    let tupla2 = ("texto", 42, 3.14);
    let tupla_vacia = ();
    
    // Acceso a tuplas
    let primero = tupla1.0;
    let segundo = tupla1.1;
    
    // ==================== MATRICES/ARRAYS ====================
    let numeros = [1, 2, 3, 4, 5];
    let matriz_vacia = [];
    let meses = ["Enero", "Febrero", "Marzo"];
    
    // Acceso a arrays
    let primer_numero = numeros[0];
    let segundo_numero = numeros[1];
    
    // ==================== ESTRUCTURAS DE CONTROL ====================
    
    // If-else
    if (x < 10) {
        println!("x es menor que 10");
    } else {
        println!("x es mayor o igual a 10");
    }
    
    // If-else if-else
    if (edad < 18) {
        println!("Menor de edad");
    } else if (edad < 65) {
        println!("Adulto");
    } else {
        println!("Adulto mayor");
    }
    
    // While
    while (contador < 5) {
        println!("Contador: ", contador);
        contador = contador + 1;
    }
    
    // For
    for (i = 0; i < 10; i = i + 1) {
        println!("i: ", i);
    }
    
    // ==================== LLAMADAS A FUNCIONES ====================
    saludar();
    let area = calcular_area(5, 10);
    imprimir_mensaje("Hola Mundo");
    
    // ==================== IMPRESIÓN ====================
    print!("Mensaje sin salto");
    println!("Mensaje con salto");
    println!("Valor de x: ", x);
    println!("Multiple valores: ", x, y, suma);
    
    // ==================== BLOQUES ANIDADOS (SHADOWING) ====================
    {
        let x = 100;
        println!("x interno: ", x);
        {
            let x = 200;
            println!("x más interno: ", x);
        }
    }
}

// ==================== DEFINICIÓN DE FUNCIONES ====================

// Función sin parámetros ni retorno
fn saludar() {
    println!("Hola desde la función saludar");
}

// Función con parámetros sin retorno
fn imprimir_mensaje(mensaje: String) {
    println!(mensaje);
}

// Función con parámetros y tipo de retorno
fn calcular_area(base: i32, altura: i32) -> i32 {
    base * altura
}

// Función con múltiples parámetros
fn sumar_tres(a: i32, b: i32, c: i32) -> i32 {
    a + b + c
}

// Función que retorna un valor directamente
fn obtener_numero() -> i32 {
    42
}

// Función con bloque de retorno
fn calcular_doble(x: i32) -> i32 {
    let resultado = x * 2;
    resultado
}

// ==================== ESTRUCTURAS (STRUCT) ====================
struct Persona {
    nombre: String,
    edad: u8,
    altura: f32,
}

struct Punto {
    x: i32,
    y: i32,
}

struct Rectangulo {
    ancho: u32,
    alto: u32,
}

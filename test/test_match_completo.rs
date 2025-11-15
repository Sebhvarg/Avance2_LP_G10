// Test completo de match en ARust

fn main() {
    // ==================== MATCH BÁSICO ====================
    let numero = 3;

    match numero {
        1 => println!("Uno"),
        2 => println!("Dos"),
        3 => println!("Tres"),
        _ => println!("Otro número"),
    }

    // ==================== MATCH SIN COMA FINAL ====================
    let opcion = 2;
    
    match opcion {
        1 => println!("Primera opción"),
        2 => println!("Segunda opción"),
        _ => println!("Opción por defecto")
    }

    // ==================== MATCH CON BLOQUES ====================
    let valor = 5;
    
    match valor {
        1 => {
            println!("Valor es 1");
            let doble = 1 * 2;
            println!("Doble: ", doble);
        },
        5 => {
            println!("Valor es 5");
            let resultado = 5 * 5;
            println!("Resultado: ", resultado);
        },
        _ => {
            println!("Valor desconocido");
        },
    }

    // ==================== MATCH CON VARIABLES ====================
    let dia = 3;
    
    match dia {
        1 => println!("Lunes"),
        2 => println!("Martes"),
        3 => println!("Miércoles"),
        4 => println!("Jueves"),
        5 => println!("Viernes"),
        _ => println!("Fin de semana"),
    }

    // ==================== MATCH CON OPERACIONES ====================
    let x = 10;
    
    match x {
        5 => println!("Cinco"),
        10 => {
            let suma = x + 5;
            println!("Es diez, suma: ", suma);
        },
        _ => println!("Otro valor"),
    }
}

// ==================== FUNCIÓN CON MATCH ====================
fn clasificar_numero(num: i32) {
    match num {
        0 => println!("Cero"),
        1 => println!("Uno"),
        2 => println!("Dos"),
        _ => println!("Mayor que dos"),
    }
}

// ==================== MATCH CON LLAMADAS A FUNCIONES ====================
fn procesar_codigo(codigo: i32) {
    match codigo {
        100 => procesar_exito(),
        404 => procesar_error(),
        _ => procesar_desconocido(),
    }
}

fn procesar_exito() {
    println!("Operación exitosa");
}

fn procesar_error() {
    println!("Error encontrado");
}

fn procesar_desconocido() {
    println!("Código desconocido");
}

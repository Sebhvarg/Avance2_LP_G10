// Test de estructura switch-case en ARust

fn main() {
    // ==================== SWITCH CON DEFAULT ====================
    let opcion = 2;
    
    switch (opcion) {
        case 1: {
            println!("Seleccionaste la opción 1");
        }
        case 2: {
            println!("Seleccionaste la opción 2");
        }
        case 3: {
            println!("Seleccionaste la opción 3");
        }
        default: {
            println!("Opción no válida");
        }
    }
    
    // ==================== SWITCH SIN DEFAULT ====================
    let dia = 5;
    
    switch (dia) {
        case 1: {
            println!("Lunes");
        }
        case 2: {
            println!("Martes");
        }
        case 3: {
            println!("Miércoles");
        }
        case 4: {
            println!("Jueves");
        }
        case 5: {
            println!("Viernes");
        }
        case 6: {
            println!("Sábado");
        }
        case 7: {
            println!("Domingo");
        }
    }
    
    // ==================== SWITCH CON OPERACIONES ====================
    let numero = 3;
    
    switch (numero) {
        case 1: {
            let resultado = numero + 10;
            println!("Resultado: ", resultado);
        }
        case 2: {
            let resultado = numero * 5;
            println!("Resultado: ", resultado);
        }
        case 3: {
            let resultado = numero * numero;
            println!("Resultado: ", resultado);
        }
        default: {
            println!("Número no válido");
        }
    }
}

// ==================== FUNCIÓN CON SWITCH ====================
fn clasificar_edad(edad: i32) {
    switch (edad) {
        case 0: {
            println!("Recién nacido");
        }
        case 1: {
            println!("Bebé");
        }
        case 13: {
            println!("Adolescente");
        }
        case 18: {
            println!("Adulto joven");
        }
        default: {
            println!("Otra edad");
        }
    }
}

// Test de errores en switch-case

fn main() {
    let opcion = 2;
    
    // ERROR 1: Falta paréntesis de cierre
    switch (opcion {
        case 1: {
            println!("Opción 1");
        }
    }
    
    // ERROR 2: Falta llave de apertura después de case
    switch (opcion) {
        case 2:
            println!("Opción 2");
        }
    }
    
    // ERROR 3: case fuera de un switch
    case 3: {
        println!("Error");
    }
    
    // ERROR 4: default fuera de un switch
    default: {
        println!("Error");
    }
    
    // ERROR 5: break mal ubicado
    break;
    
    // ERROR 6: continue mal ubicado
    continue;
}

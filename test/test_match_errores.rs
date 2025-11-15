// Test de errores en match

fn main() {
    let numero = 3;

    // ERROR 1: Falta flecha doble =>
    match numero {
        1 println!("Uno"),
        2 => println!("Dos"),
    }

    // ERROR 2: Uso de match sin identificador
    match {
        1 => println!("Uno"),
    }

    // ERROR 3: Flecha doble fuera de match
    1 => println!("Error");

    // ERROR 4: Guion bajo fuera de match
    let x = _;
}

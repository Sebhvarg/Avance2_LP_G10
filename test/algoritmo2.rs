fn main() {
    let x = 5;

    let x = x + 1;

    {
        let x = x * 2;
        println!("The value of x in the inner scope is: {x}");
    }
    let y: i8 = 10;

    let i: char = 'A';

    let f: f32 = 2.5;
    let tupla = (123, "SI", 3.14);
    println!("{}", tupla.1); // Acceder al segundo elemento de la tupla

    let months = ["January", "Februar", "August", "September", "October", "November", "December"];


    println!("The value of x is: {x}");
}
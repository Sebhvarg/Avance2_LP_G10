fn main() {
    println!("Hello, world!");
    let x = 5;
    let mut l = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");

    let y = 10;
    if (x < y) {
        println!("x is less than y");
    } else if (x == y) {
        println!("x is equal to y");
    } else {
        println!("x is greater than y");
    }
    while (x < 20) {
        x = x + 1;
    }
    for (i = 0; i < 10; i++) {
        println!(i);
    }
}

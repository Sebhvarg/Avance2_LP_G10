fn main() {
    // Ingreso de datos por teclado
    input("Ingrese su nombre:");

    // Declaración y asignación
    let x = 10;
    let y = 5;
    let z = 3;

    // Estructura de datos (lista)
    let numeros = [1, 2, 3, 4, 5];

    // Expresión aritmética
    let suma = x + y * z;

    // Condicional con conectores lógicos
    if (x > y && z < 5 || y == 5) {
        print("Condición verdadera");
    } else {
        print("Condición falsa");
    }

    // Expresión booleana adicional
    let e = x && y;

    // Imprimir resultado final
    print(x);
    x = y && z;
}

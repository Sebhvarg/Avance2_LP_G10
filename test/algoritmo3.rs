// Algoritmo 3 - Carlos Ronquillo (carrbrus)
// Clases, propiedades y métodos — sintaxis compatible con el parser actual

class Persona {
    let nombre = "Carlos";
    let edad = 22;

    fn saludar() {
        print("Hola, mi nombre es ");
        print(nombre);
    }

    fn cumplir_anios() {
        edad = edad + 1;
        print("Ahora tengo ");
        print(edad);
        print(" años.");
    }
}

fn main() {
    Persona.saludar();
    Persona.cumplir_anios();
}



class Persona {
    let nombre = "Carlos";
    let edad = 25;

    fn saludar() {
        print("Hola, mi nombre es ");
    }

    fn cumplir_anios() {
        edad = edad + 1;
    }
}

Persona.saludar();
Persona.cumplir_anios();

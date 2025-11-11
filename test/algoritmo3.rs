struct Persona {
    nombre: String,
    edad: i32
}

impl Persona {
    fn saludar(&self) {
        println!("Hola, soy {}", self.nombre);
    }
}


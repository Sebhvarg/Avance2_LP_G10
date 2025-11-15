# Avance2_LP_G10
## Analizador Sintáctico ARust

### Integrantes:
- Derian Baque Choez (fernan0502)
- Sebastian Holguin (Sebhvarg)
- Carlos Ronquillo (carrbrus)

## Características Implementadas

### Estructuras de Control
- Condicionales: `if`, `else if`, `else`
- Ciclos: `while`, `for`
- **Match**: Expresiones de coincidencia de patrones con múltiples brazos

### Manejo de Errores
El analizador proporciona mensajes de error específicos para:

#### Errores de Puntuación
- Llaves, paréntesis y corchetes mal ubicados
- Punto y coma inesperado

#### Errores de Palabras Reservadas
- `match`: Sintaxis incorrecta de la expresión match
- `=>`: Operador de flecha doble solo puede usarse en expresiones match
- `break`: Solo puede usarse dentro de ciclos
- `continue`: Solo puede usarse dentro de ciclos
- `return`: Solo puede usarse dentro de funciones
- Y otras palabras reservadas del lenguaje

#### Errores de Operadores
- Operadores aritméticos mal ubicados
- Operadores de asignación incorrectos
- Operadores relacionales en contexto inválido

#### Errores de Tipos y Valores
- Identificadores inesperados
- Valores numéricos, cadenas y caracteres mal ubicados
- Tipos de datos en posición incorrecta

## Sintaxis de Match

### Match con expresiones simples
```rust
match variable {
    1 => println!("Uno"),
    2 => println!("Dos"),
    3 => println!("Tres"),
    _ => println!("Otro"),
}
```

### Match con bloques de código
```rust
match variable {
    1 => {
        println!("Uno");
        let x = 1 + 1;
    },
    2 => {
        println!("Dos");
        let y = 2 * 2;
    },
    _ => {
        println!("Otro valor");
    },
}
```

### Match con coma opcional al final
```rust
match variable {
    1 => println!("Uno"),
    2 => println!("Dos"),
    _ => println!("Por defecto")
}
```

### Características de Match
- Soporta múltiples brazos (arms) separados por comas
- Patrón comodín `_` para capturar todos los casos no especificados
- Coma final opcional después del último brazo
- Cada brazo puede tener una expresión simple o un bloque `{ }`
- Las expresiones pueden ser llamadas a funciones, impresión, o valores

## Uso

```bash
python sintax.py <archivo.rs>
```

## Archivos de Prueba
- `test/test_completo.rs`: Prueba completa de todas las características
- `test/test_switch.rs`: Prueba básica de match
- `test/test_match_completo.rs`: Prueba completa de expresiones match
- `test/test_match_errores.rs`: Prueba de mensajes de error en match

## Logs
Los resultados del análisis se guardan en `logs/sintactico-<usuario>-<fecha>.txt`
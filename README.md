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
- **Switch-Case**: Estructura `switch` con casos y default

### Manejo de Errores
El analizador proporciona mensajes de error específicos para:

#### Errores de Puntuación
- Llaves, paréntesis y corchetes mal ubicados
- Punto y coma inesperado

#### Errores de Palabras Reservadas
- `switch`: Sintaxis incorrecta del match/case
- `case`: Debe estar dentro de un bloque switch
- `default`: Debe estar dentro de un bloque switch
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

## Sintaxis de Switch-Case

### Con Default
```rust
switch (variable) {
    case valor1: {
        // código
    }
    case valor2: {
        // código
    }
    default: {
        // código por defecto
    }
}
```

### Sin Default
```rust
switch (variable) {
    case valor1: {
        // código
    }
    case valor2: {
        // código
    }
}
```

## Uso

```bash
python sintax.py <archivo.rs>
```

## Archivos de Prueba
- `test/test_completo.rs`: Prueba completa de todas las características
- `test/test_switch.rs`: Prueba específica de switch-case
- `test/test_switch_errores.rs`: Prueba de mensajes de error

## Logs
Los resultados del análisis se guardan en `logs/sintactico-<usuario>-<fecha>.txt`
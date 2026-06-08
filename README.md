# TP Clase 10 — Patrones de Diseño

**Materia:** Programación Avanzada (189)
**Carrera:** Licenciatura en Ciencia de Datos
**Universidad:** Universidad Nacional Guillermo Brown (UNAB)
---

## Ejercicio 1 — Críticas a los patrones de diseño

### Peter Norvig — "Design Patterns in Dynamic Languages" (1996)

Peter Norvig demostró que **16 de los 23 patrones GoF son "invisibles o significativamente más simples"** en lenguajes dinámicos como Python o Lisp. Su argumento central es que muchos patrones no resuelven problemas fundamentales de diseño, sino que compensan limitaciones de lenguajes estáticos como C++ o Java.

**Ejemplo:** el patrón Strategy en Java requiere una interfaz, clases concretas y un contexto. En Python basta con pasar una función como argumento:

```python
# Strategy en Python: una función como parámetro
resultado = ordenar_datos(mis_datos, sorted)
```

### Paul Graham — "Revenge of the Nerds"

Graham argumenta que los patrones son evidencia de un lenguaje insuficientemente poderoso. Compara al programador que aplica patrones manualmente con un "compilador humano": repite transformaciones mecánicas que un lenguaje más expresivo haría automáticamente mediante macros o funciones de primera clase.

### Sobreingeniería

Uno de los problemas más comunes en la industria es aplicar patrones donde no son necesarios. Por ejemplo, usar un Factory Method para crear objetos simples que podrían instanciarse directamente con el constructor:

```python
# Sobreingeniería innecesaria:
animal = AnimalFactory().create_animal("perro")

# Suficiente en la mayoría de los casos:
animal = Perro()
```

### El Singleton como antipatrón encubierto

El Singleton es el patrón más criticado. Aunque resuelve un problema real, introduce estado global encubierto, dificulta el testing unitario (un test "contamina" el estado de otro), y viola el Principio de Responsabilidad Única. Frameworks modernos como Spring o FastAPI manejan el ciclo de vida de objetos mediante inyección de dependencias, haciendo innecesario el Singleton en muchos contextos.

### Jeff Atwood — Los lenguajes absorben los patrones

A medida que los lenguajes evolucionan, absorben patrones como características nativas: Iterator → `for...in` y generadores; Strategy → funciones de primera clase; Decorator → decoradores `@`; Command → lambdas y closures. Los patrones no son eternos, son soluciones contextuales.

**Conclusión:** las críticas no invalidan los patrones, sino que invitan a usarlos con criterio. En lenguajes como Python, muchos se simplifican enormemente.

---

## Ejercicio 2 — Implementación de 3 patrones en Python

Se implementó un patrón de cada categoría con ejemplos funcionales:

| Patrón | Categoría | Archivo | Ejemplo |
|--------|-----------|---------|---------|
| Singleton | Creacional | `ejercicio2_singleton.py` | Configuración global de una app (instancia única) |
| Adapter | Estructural | `ejercicio2_adapter.py` | Sensores de temperatura con distintas interfaces (°F, K → °C) |
| Observer | Comportamiento | `ejercicio2_observer.py` | Tienda online con notificaciones por email y SMS |

Ejecutar con:
```bash
python ejercicio2_singleton.py
python ejercicio2_adapter.py
python ejercicio2_observer.py
```

---

## Ejercicio 3 — Problemas cotidianos y patrones de diseño

### 1. Pedido en un restaurante → Patrón Command

El cliente le dice al mozo qué quiere, el mozo anota la comanda y la lleva a la cocina. La comanda es un **objeto que encapsula la solicitud** (Command). Permite encolar pedidos, llevar un historial y cancelar órdenes, sin que el cliente necesite saber quién cocina ni cómo.

### 2. Adaptador de enchufe para viaje → Patrón Adapter

Un enchufe argentino no entra en un tomacorriente europeo. El adaptador de viaje traduce entre ambas interfaces sin modificar ni el dispositivo ni el enchufe. Exactamente lo que hace el patrón Adapter: hacer colaborar interfaces incompatibles a través de un intermediario.

### 3. Navegador GPS con rutas alternativas → Patrón Strategy

Google Maps ofrece ruta más rápida, más corta, sin peajes, etc. El destino es el mismo pero el **algoritmo de cálculo cambia** según la preferencia del usuario. Es el patrón Strategy: una familia de algoritmos intercambiables encapsulados en clases separadas, seleccionables en tiempo de ejecución.

---

## Ejercicio 4 — Nombres alternativos de los patrones de diseño

Los 23 patrones GoF tienen nombres alternativos según la fuente o contexto:

### Patrones Creacionales

| Nombre GoF | Nombres alternativos |
|---|---|
| Abstract Factory | Kit, Toolkit |
| Builder | Construction, Director/Builder |
| Factory Method | Virtual Constructor |
| Prototype | Clone, Cloning Pattern |
| Singleton | Global Access Point, Instance Manager |

### Patrones Estructurales

| Nombre GoF | Nombres alternativos |
|---|---|
| Adapter | Wrapper (Object Adapter) |
| Bridge | Handle/Body, Abstraction/Implementation |
| Composite | Part-Whole, Object Tree |
| Decorator | Wrapper (Recursive Wrapper) |
| Facade | Wrapper (High-Level Interface) |
| Flyweight | Cache, State-Sharing |
| Proxy | Surrogate, Placeholder, Token |

> **Nota:** "Wrapper" es ambiguo — se usa como sinónimo de Adapter, Decorator y Facade. En comunicación profesional hay que especificar cuál.

### Patrones de Comportamiento

| Nombre GoF | Nombres alternativos |
|---|---|
| Chain of Responsibility | Chain of Command |
| Command | Action, Transaction |
| Interpreter | Language, Grammar |
| Iterator | Cursor |
| Mediator | Controller, Hub |
| Memento | Token, Snapshot |
| Observer | Pub-Sub, Dependents, Listener |
| State | Objects for States |
| Strategy | Policy |
| Template Method | Hook, Skeleton |
| Visitor | Double Dispatch |

---

## Ejercicio 5 — Antipatrones de diseño

Un **antipatrón** es una respuesta frecuente a un problema recurrente que parece razonable a corto plazo pero genera consecuencias negativas: deuda técnica, código frágil y difícil de mantener. El término fue popularizado por Andrew Koenig (1995).

### God Object (Objeto Dios)

Una clase que concentra demasiadas responsabilidades, convirtiéndose en el centro de todo el sistema. Ejemplo: una clase `SistemaCompleto` que maneja BD, autenticación, emails, reportes y pagos.

### Spaghetti Code

Código con flujo de control enredado, sin estructura clara, con niveles excesivos de anidamiento y lógica que salta de un lugar a otro.

### Golden Hammer (Martillo de Oro)

Usar una herramienta o tecnología conocida para todos los problemas sin evaluar alternativas. Ejemplo: implementar toda la lógica de negocio como stored procedures en la BD porque "ya sabemos SQL".

### Copy-Paste Programming

Duplicar código en vez de crear abstracciones reutilizables. Un bug en la lógica original se replica en todas las copias, y un cambio (como la tasa de IVA) debe buscarse en todo el proyecto.

### Lava Flow (Flujo de Lava)

Código obsoleto que permanece en el proyecto porque nadie se atreve a eliminarlo. Como la lava que se enfría y endurece, el código muerto se solidifica y nadie lo toca.

## Material de referencia

- [Patrones de Diseño (ES)](https://refactoring.guru/es/design-patterns/what-is-pattern)
- [Patrones en Python](https://refactoring.guru/es/design-patterns/python)
- [Principios SOLID](https://profile.es/blog/principios-solid-desarrollo-software-calidad/)

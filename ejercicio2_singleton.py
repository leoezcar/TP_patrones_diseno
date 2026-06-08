"""
Ejercicio 2 — Patrón Singleton (Creacional)
Configuración global de una aplicación con instancia única.
"""


class SingletonMeta(type):
    """Metaclase que garantiza una única instancia por clase."""

    _instancias = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            instancia = super().__call__(*args, **kwargs)
            cls._instancias[cls] = instancia
        return cls._instancias[cls]


class Configuracion(metaclass=SingletonMeta):
    """Configuración global de la aplicación (Singleton)."""

    def __init__(self):
        self._configuracion = {
            "base_de_datos": "postgresql://localhost:5432/mi_app",
            "puerto_servidor": 8080,
            "modo_debug": False,
            "nivel_log": "INFO",
            "max_conexiones": 10,
        }

    def obtener(self, clave):
        return self._configuracion.get(clave, None)

    def establecer(self, clave, valor):
        self._configuracion[clave] = valor

    def mostrar_todo(self):
        for clave, valor in self._configuracion.items():
            print(f"  {clave}: {valor}")


if __name__ == "__main__":
    # Crear dos referencias a la configuración
    config_1 = Configuracion()
    config_2 = Configuracion()

    # Verificar que son la misma instancia
    print(f"config_1 id: {id(config_1)}")
    print(f"config_2 id: {id(config_2)}")
    print(f"¿Misma instancia? {config_1 is config_2}")

    # Modificar desde una referencia, leer desde la otra
    print("\nConfiguración inicial:")
    config_1.mostrar_todo()

    config_1.establecer("modo_debug", True)
    print(f"\nconfig_2 lee modo_debug: {config_2.obtener('modo_debug')}")
    print("(El cambio se refleja porque ambas son la misma instancia)")

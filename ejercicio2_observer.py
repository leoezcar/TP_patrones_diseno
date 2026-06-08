"""
Ejercicio 2 — Patrón Observer (Comportamiento)
Tienda online con notificaciones a suscriptores por email y SMS.
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Observador(ABC):
    @abstractmethod
    def actualizar(self, evento: str, datos: dict):
        pass


class TiendaOnline:
    """Sujeto observable que notifica eventos a sus suscriptores."""

    def __init__(self, nombre: str):
        self._nombre = nombre
        self._suscriptores: dict[str, list[Observador]] = {}

    def suscribir(self, evento: str, observador: Observador):
        if evento not in self._suscriptores:
            self._suscriptores[evento] = []
        if observador not in self._suscriptores[evento]:
            self._suscriptores[evento].append(observador)

    def desuscribir(self, evento: str, observador: Observador):
        if evento in self._suscriptores:
            self._suscriptores[evento] = [
                o for o in self._suscriptores[evento] if o is not observador
            ]

    def _notificar(self, evento: str, datos: dict):
        for obs in self._suscriptores.get(evento, []):
            obs.actualizar(evento, datos)

    def agregar_producto(self, nombre: str, precio: float):
        self._notificar("nuevo_producto", {
            "tienda": self._nombre, "producto": nombre, "precio": precio,
        })

    def aplicar_oferta(self, producto: str, descuento: int, precio_original: float):
        precio_nuevo = round(precio_original * (1 - descuento / 100), 2)
        self._notificar("oferta", {
            "tienda": self._nombre, "producto": producto,
            "descuento": descuento, "precio_nuevo": precio_nuevo,
        })


class ClienteEmail(Observador):
    def __init__(self, nombre: str, email: str):
        self._nombre = nombre
        self._email = email

    def actualizar(self, evento: str, datos: dict):
        if evento == "nuevo_producto":
            print(f"  [Email] {self._nombre} ({self._email}): "
                  f"Nuevo '{datos['producto']}' por ${datos['precio']}")
        elif evento == "oferta":
            print(f"  [Email] {self._nombre} ({self._email}): "
                  f"¡{datos['descuento']}% OFF en '{datos['producto']}'! "
                  f"-> ${datos['precio_nuevo']}")


class ClienteSMS(Observador):
    def __init__(self, nombre: str, telefono: str):
        self._nombre = nombre
        self._telefono = telefono

    def actualizar(self, evento: str, datos: dict):
        if evento == "nuevo_producto":
            print(f"  [SMS] {self._nombre} ({self._telefono}): "
                  f"Nuevo: '{datos['producto']}' ${datos['precio']}")
        elif evento == "oferta":
            print(f"  [SMS] {self._nombre} ({self._telefono}): "
                  f"OFERTA: '{datos['producto']}' {datos['descuento']}% OFF")


if __name__ == "__main__":
    tienda = TiendaOnline("TechStore Argentina")

    # Crear suscriptores
    ana = ClienteEmail("Ana García", "ana@email.com")
    luis = ClienteEmail("Luis Martínez", "luis@email.com")
    maria = ClienteSMS("María López", "+54 11 5555-1234")

    # Suscribir a distintos eventos
    tienda.suscribir("nuevo_producto", luis)
    tienda.suscribir("oferta", ana)
    tienda.suscribir("oferta", luis)
    tienda.suscribir("oferta", maria)

    # Nuevo producto (solo Luis recibe)
    print("Evento: nuevo producto")
    tienda.agregar_producto("Notebook Gamer RTX 4060", 1_200_000)

    # Oferta (Ana, Luis y María reciben)
    print("\nEvento: oferta")
    tienda.aplicar_oferta("Notebook Gamer RTX 4060", 20, 1_200_000)

    # María se desuscribe
    tienda.desuscribir("oferta", maria)

    # Nueva oferta (María ya no recibe)
    print("\nEvento: oferta (María desuscrita)")
    tienda.aplicar_oferta("Notebook Gamer RTX 4060", 10, 960_000)

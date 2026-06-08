"""
Ejercicio 2 — Patron Observer (Comportamiento)
Tienda online con notificaciones a suscriptores por email y SMS.
"""


class TiendaOnline:
    """Sujeto observable que notifica eventos a sus suscriptores."""

    def __init__(self, nombre):
        self.nombre = nombre
        self._suscriptores = {}

    def suscribir(self, evento, observador):
        if evento not in self._suscriptores:
            self._suscriptores[evento] = []
        if observador not in self._suscriptores[evento]:
            self._suscriptores[evento].append(observador)

    def desuscribir(self, evento, observador):
        if evento in self._suscriptores:
            self._suscriptores[evento] = [
                o for o in self._suscriptores[evento] if o is not observador
            ]

    def _notificar(self, evento, datos):
        for obs in self._suscriptores.get(evento, []):
            obs.actualizar(evento, datos)

    def agregar_producto(self, nombre, precio):
        self._notificar("nuevo_producto", {
            "tienda": self.nombre, "producto": nombre, "precio": precio,
        })

    def aplicar_oferta(self, producto, descuento, precio_original):
        precio_nuevo = round(precio_original * (1 - descuento / 100), 2)
        self._notificar("oferta", {
            "tienda": self.nombre, "producto": producto,
            "descuento": descuento, "precio_nuevo": precio_nuevo,
        })


class ClienteEmail:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def actualizar(self, evento, datos):
        if evento == "nuevo_producto":
            print(f"  [Email] {self.nombre} ({self.email}): "
                  f"Nuevo '{datos['producto']}' por ${datos['precio']}")
        elif evento == "oferta":
            print(f"  [Email] {self.nombre} ({self.email}): "
                  f"{datos['descuento']}% OFF en '{datos['producto']}' "
                  f"-> ${datos['precio_nuevo']}")


class ClienteSMS:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def actualizar(self, evento, datos):
        if evento == "nuevo_producto":
            print(f"  [SMS] {self.nombre} ({self.telefono}): "
                  f"Nuevo: '{datos['producto']}' ${datos['precio']}")
        elif evento == "oferta":
            print(f"  [SMS] {self.nombre} ({self.telefono}): "
                  f"OFERTA: '{datos['producto']}' {datos['descuento']}% OFF")


if __name__ == "__main__":
    tienda = TiendaOnline("TechStore Argentina")

    # Crear suscriptores
    ana = ClienteEmail("Ana Garcia", "ana@email.com")
    luis = ClienteEmail("Luis Martinez", "luis@email.com")
    maria = ClienteSMS("Maria Lopez", "+54 11 5555-1234")

    # Suscribir a distintos eventos
    tienda.suscribir("nuevo_producto", luis)
    tienda.suscribir("oferta", ana)
    tienda.suscribir("oferta", luis)
    tienda.suscribir("oferta", maria)

    # Nuevo producto (solo Luis recibe)
    print("Evento: nuevo producto")
    tienda.agregar_producto("Notebook Gamer RTX 4060", 1_200_000)

    # Oferta (Ana, Luis y Maria reciben)
    print("\nEvento: oferta")
    tienda.aplicar_oferta("Notebook Gamer RTX 4060", 20, 1_200_000)

    # Maria se desuscribe
    tienda.desuscribir("oferta", maria)

    # Nueva oferta (Maria ya no recibe)
    print("\nEvento: oferta (Maria desuscrita)")
    tienda.aplicar_oferta("Notebook Gamer RTX 4060", 10, 960_000)

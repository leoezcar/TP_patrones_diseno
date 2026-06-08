"""
Ejercicio 2 — Patrón Adapter (Estructural)
Sensores de temperatura con interfaces incompatibles (°F, K -> °C).
"""


# Sensor compatible (ya reporta en Celsius)
class SensorArgentino:
    def __init__(self, nombre, temperatura):
        self.nombre = nombre
        self.temperatura = temperatura

    def obtener_temperatura_celsius(self):
        return self.temperatura

    def obtener_nombre(self):
        return self.nombre


# Sensor americano — interfaz incompatible (Fahrenheit)
class SensorAmericano:
    def __init__(self, sensor_id, temp_f):
        self.sensor_id = sensor_id
        self.temp_f = temp_f


# Sensor cientifico — interfaz incompatible (Kelvin)
class SensorCientifico:
    def __init__(self, codigo, temp_kelvin):
        self.codigo = codigo
        self.temp_kelvin = temp_kelvin


# Adapter: Fahrenheit -> Celsius
class AdaptadorSensorAmericano:
    def __init__(self, sensor):
        self._sensor = sensor

    def obtener_temperatura_celsius(self):
        return round((self._sensor.temp_f - 32) * 5 / 9, 2)

    def obtener_nombre(self):
        return f"[Adaptado US] {self._sensor.sensor_id}"


# Adapter: Kelvin -> Celsius
class AdaptadorSensorCientifico:
    def __init__(self, sensor):
        self._sensor = sensor

    def obtener_temperatura_celsius(self):
        return round(self._sensor.temp_kelvin - 273.15, 2)

    def obtener_nombre(self):
        return f"[Adaptado Lab] {self._sensor.codigo}"


# Sistema que trabaja con cualquier objeto que tenga los metodos esperados
class SistemaMonitoreo:
    def __init__(self):
        self._sensores = []

    def registrar_sensor(self, sensor):
        self._sensores.append(sensor)

    def reporte(self):
        for sensor in self._sensores:
            print(f"  {sensor.obtener_nombre()}: {sensor.obtener_temperatura_celsius()} C")


if __name__ == "__main__":
    # Sensores de distintos origenes
    sensor_arg = SensorArgentino("Sensor Buenos Aires", 25.5)
    sensor_usa = SensorAmericano("US-Sensor-NYC", 98.6)
    sensor_lab = SensorCientifico("LAB-K-001", 310.15)

    # Adaptar los incompatibles
    adaptador_usa = AdaptadorSensorAmericano(sensor_usa)
    adaptador_lab = AdaptadorSensorCientifico(sensor_lab)

    # Integrar todos en el mismo sistema
    sistema = SistemaMonitoreo()
    sistema.registrar_sensor(sensor_arg)
    sistema.registrar_sensor(adaptador_usa)
    sistema.registrar_sensor(adaptador_lab)

    print("Reporte de temperaturas:")
    sistema.reporte()

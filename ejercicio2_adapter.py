"""
Ejercicio 2 — Patrón Adapter (Estructural)
Sensores de temperatura con interfaces incompatibles (°F, K → °C).
"""

from abc import ABC, abstractmethod


# Interfaz estándar que nuestro sistema espera
class SensorTemperatura(ABC):
    @abstractmethod
    def obtener_temperatura_celsius(self) -> float:
        pass

    @abstractmethod
    def obtener_nombre(self) -> str:
        pass


# Sensor compatible (ya reporta en Celsius)
class SensorArgentino(SensorTemperatura):
    def __init__(self, nombre: str, temperatura: float):
        self._nombre = nombre
        self._temperatura = temperatura

    def obtener_temperatura_celsius(self) -> float:
        return self._temperatura

    def obtener_nombre(self) -> str:
        return self._nombre


# Sensor americano — interfaz incompatible (Fahrenheit)
class SensorAmericano:
    def __init__(self, sensor_id: str, temp_f: float):
        self._sensor_id = sensor_id
        self._temp_f = temp_f

    def get_temperature_fahrenheit(self) -> float:
        return self._temp_f

    def get_sensor_id(self) -> str:
        return self._sensor_id


# Sensor científico — interfaz incompatible (Kelvin)
class SensorCientifico:
    def __init__(self, codigo: str, temp_kelvin: float):
        self._codigo = codigo
        self._temp_kelvin = temp_kelvin

    def leer_kelvin(self) -> float:
        return self._temp_kelvin

    def codigo_sensor(self) -> str:
        return self._codigo


# Adapter: Fahrenheit → Celsius
class AdaptadorSensorAmericano(SensorTemperatura):
    def __init__(self, sensor: SensorAmericano):
        self._sensor = sensor

    def obtener_temperatura_celsius(self) -> float:
        return round((self._sensor.get_temperature_fahrenheit() - 32) * 5 / 9, 2)

    def obtener_nombre(self) -> str:
        return f"[Adaptado US] {self._sensor.get_sensor_id()}"


# Adapter: Kelvin → Celsius
class AdaptadorSensorCientifico(SensorTemperatura):
    def __init__(self, sensor: SensorCientifico):
        self._sensor = sensor

    def obtener_temperatura_celsius(self) -> float:
        return round(self._sensor.leer_kelvin() - 273.15, 2)

    def obtener_nombre(self) -> str:
        return f"[Adaptado Lab] {self._sensor.codigo_sensor()}"


# Sistema que trabaja solo con la interfaz estándar
class SistemaMonitoreo:
    def __init__(self):
        self._sensores = []

    def registrar_sensor(self, sensor: SensorTemperatura):
        self._sensores.append(sensor)

    def reporte(self):
        for sensor in self._sensores:
            nombre = sensor.obtener_nombre()
            temp = sensor.obtener_temperatura_celsius()
            print(f"  {nombre}: {temp}°C")


if __name__ == "__main__":
    # Sensores de distintos orígenes
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

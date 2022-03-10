import time
import board
import adafruit_dht

class Reading:
    def __init__(self):
        self.temperature = -274
        self.humidity = -1
        self.timestamp = 0
    
    def seconds_since_last_reading(self):
        return time.time() - self.timestamp

    def update(self, temperature, humidity):
        self.temperature = temperature if temperature else -274
        self.humidity = humidity if humidity else -1
        self.timestamp = time.time()

class DhtSensor:
    def __init__(self):
        self.__latest_reading = Reading()
        # Change below line for the actual pin & sensor used
        self.__dht_device = adafruit_dht.DHT11(board.D26)

    def get_temperature(self):
        self.__read_sensor()
        return self.__latest_reading.temperature
    
    def get_humidity(self):
        self.__read_sensor()
        return self.__latest_reading.humidity
    
    def __read_sensor(self):
        if self.__latest_reading.seconds_since_last_reading() < 3:
            return None
        try:
            temperature = self.__dht_device.temperature
            humidity = self.__dht_device.humidity
            self.__latest_reading.update(temperature, humidity)
        except RuntimeError as error:
            time.sleep(1)
            self.__read_sensor()
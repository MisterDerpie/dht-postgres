from database import TemperatureDatabase
from dhtsensor import DhtSensor
from time import sleep
import traceback
import logging


dhtsensor = DhtSensor()
temperature_database = TemperatureDatabase()

while True:
    try:
        temperature_database.insert_temperature(dhtsensor.get_temperature())
        sleep(30)
    except Exception as e:
        logging.error(traceback.format_exc())
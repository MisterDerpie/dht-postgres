from database import DhtDatabase
from dhtsensor import DhtSensor
from time import sleep
import traceback
import logging


dhtsensor = DhtSensor()
dht_database = DhtDatabase()

while True:
    try:
        dht_database.insert_reading(dhtsensor.get_temperature(), dhtsensor.get_humidity())
        sleep(30)
    except Exception as e:
        logging.error(traceback.format_exc())
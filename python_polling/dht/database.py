#!/bin/python3

import psycopg2
from time import sleep

class TemperatureDatabase:
    def insert_temperature(self, temperature):
        connection = self.__get_connection()
        self.__insert_temperature(temperature, connection)
        connection.close()

    def __insert_temperature(self, temperature, connection):
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO temperature (temperature) VALUES ({temperature})')
        cursor.close()
        connection.commit()
    
    def __get_connection(self):
        try: 
            return psycopg2.connect(
                user="postgres",
                password="test",
                host="temperature_pg_db",
                port="5432",
                database="temperature"
            )
        except Exception as exception:
            print('Failed to connect, fallback and retry ...')
            sleep(1)
            return self.__get_connection()
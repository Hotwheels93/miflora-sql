# MiFlora Flower Care SQL push
# Author: Martin Hocquel (hotwheels93)
# 2019/06/13
# MIT Licence

import mysql.connector
import datetime
from miflora.miflora_poller import MiFloraPoller
from btlewrap import available_backends, BluepyBackend, GatttoolBackend, PygattBackend

mac_device_1 = 'MAC'
device_1_name = 'Plant name'
timestamp = datetime.datetime.now()
poller = MiFloraPoller(mac_device_1, BluepyBackend)

battery = poller.battery_level()
temp = poller.parameter_value('temperature')
light = poller.parameter_value('light')
moisture = poller.parameter_value('moisture')
conductivity = poller.parameter_value('conductivity')


mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password!",
  database="dbname"
)

mycursor = mydb.cursor()

table = "plants"
sql = "INSERT INTO plants (name, battery, temperature, light, moisture, conductivity, updated) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = (device_1_name, battery, temp, light, moisture, conductivity, timestamp)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "Date inserted into table: ", table )
print ("Name: ", device_1_name)
print("Battery: ", battery)
print("Temperatur: ", temp)
print("Light: ", light)
print("Moisture: ", moisture)
print("Conducitvity: ", conductivity)

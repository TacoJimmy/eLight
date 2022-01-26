import sys
import time
import serial

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import paho.mqtt.client as mqtt
import random
import json
import datetime
import codecs

import schedule
import time

import soilsensor

def send_mqtt():
    airconditioninfor.AC_contain = AC_infor('/dev/ttyS4',1)
    airconditioninfor.on_AC_publish(AC_contain)
    print(AC_contain)
    soilsensor.soil_contain = soil_infor('/dev/ttyS1')
    soilsensor.on_soil_publish(soil_contain)
    print(soil_contain)

		
#schedule.every(5).minutes.do(send_mqtt)
schedule.every(10).seconds.do(send_mqtt)

while True:
    schedule.run_pending()
    #data = soil_infor('/dev/ttyS1')
    #print(data)
    time.sleep(3)



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

import time

def read_mode():
    with open('ACctrl.json') as ACCtrlMode:
        ACOperate = json.load(ACCtrlMode)
        ACCtrlMode.close
        print (ACOperate)
    return ACOperate



if __name__ == '__main__':
    while True:
        read_mode()
        time.sleep(10)
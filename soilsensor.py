import time
import serial
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import paho.mqtt.client as mqtt
import json

import time

def on_soil_publish(soil_infor):
    try:
        client = mqtt.Client()
        client.username_pw_set("YMQQ60uho7Y2AYJU08WO","xxxx")
        client.connect('demo.thingsboard.io', 1883, 60)
        payload = {'soiltemp':soil_infor[0], 'soilhumid':soil_infor[1],'soilEC':soil_infor[2],'soilsal':soil_infor[3],'soilTDS':soil_infor[4],'soilPH':soil_infor[5],'soilNPKn':soil_infor[6],'soilNPKp':soil_infor[7],'soilNPKk':soil_infor[8]}
        print (json.dumps(payload))
        client.publish("v1/devices/me/telemetry", json.dumps(payload))
        time.sleep(5)
    except:
        print('error')

def soil_infor(PORT):
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
        master.set_timeout(5.0)
        master.set_verbose(True)
        # read NPK data
        soil_NPKSensor = master.execute(2, cst.READ_HOLDING_REGISTERS, 0, 3)
        time.sleep(0.2)
        # read Soil tempature, humidity data
        soilTemp = master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 10)
        time.sleep(0.2)
        # read Soil PH data
        soil_PHSensor = master.execute(3, cst.READ_HOLDING_REGISTERS, 0, 1)
        time.sleep(0.2)
        # make sensor infor
        soil_infor = (soilTemp[0]/100,soilTemp[1],soilTemp[2],soilTemp[3],soilTemp[4],soil_PHSensor[0]/10,soil_NPKSensor[0],soil_NPKSensor[1],soil_NPKSensor[2])

        #soil_infor = soil_PHSensor
        return (soil_infor)

    except:
        contain_infor = [0,0,0,0,0,0,0,0,0]
        return (contain_infor)

if __name__ == '__main__':
    while True:
        # read soil sensor data
        soil_contain = soil_infor('/dev/ttyS1')
        time.sleep(3)
        on_soil_publish(soil_contain)
        time.sleep(10)
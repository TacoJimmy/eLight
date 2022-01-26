import time
import serial
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import paho.mqtt.client as mqtt
import json
import time


def on_AC_publish(AC_infor):
    try:
        client = mqtt.Client()
        client.username_pw_set("U9UMevvuOaMmBDCDz3dM","xxxx")
        client.connect('thingsboard.cloud', 1883, 60)
        payload = {'Temperature' : 25 , 'humidity' : 80}
        #payload = {'Temperature' : AC_infor[0] , 'humidity' : AC_infor[1],'CO2':AC_infor[2], 'settemp':AC_infor[3], 'compressor':AC_infor[4]}
        client.publish("v1/devices/me/telemetry", json.dumps(payload))
        time.sleep(1)
    except:
        print('error')


def AC_infor(PORT,ID):
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
        master.set_timeout(5.0)
        master.set_verbose(True)
        contain_tempread = master.execute(ID, cst.READ_HOLDING_REGISTERS, 6601, 4)
        contain_compstatus = master.execute(1, cst.READ_COILS, 1006, 1)

        contain_tempset = master.execute(ID, cst.READ_HOLDING_REGISTERS, 111, 1)
        contain_infor = contain_tempread[0]/10,contain_tempread[1],contain_tempread[3],contain_tempset[0]/10,contain_compstatus[0]
        return (contain_infor)

    except:
        contain_infor = [0,0,0,0,0]

        return (contain_infor)


if __name__ == '__main__':
    while True:
        # read soil sensor data
        AC_contain = AC_infor('/dev/ttyS4',1)
        on_AC_publish(AC_contain)
        time.sleep(10)



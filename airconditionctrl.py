import time
import json
import time

def read_ComCtrl():
    with open('ComACctrl.json') as ACCtrlMode:
        ACOperate = json.load(ACCtrlMode)
        ACCtrlMode.close
        print (ACOperate)
    return ACOperate

def read_SetCtrl():
    with open('SetACctrl.json') as ACCtrlMode:
        ACOperate = json.load(ACCtrlMode)
        ACCtrlMode.close
        print (ACOperate)
    return ACOperate

if __name__ == '__main__':
    while True:
        read_ComCtrl()
        read_SetCtrl()
        time.sleep(10)
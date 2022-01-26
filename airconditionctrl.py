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

def Check_Com():
    APPCommd = read_ComCtrl()
    ACSet = read_SetCtrl()
    
    if APPCommd['ACTemp'] == ACSet['ACTemp']:
        print("chekc01")
    else:
        print("chekc02")
        

        with open('SetACctrl.json', 'w') as CtrlFuntion:
            json.dump(APPCommd['ACTemp'], CtrlFuntion['ACTemp'])

if __name__ == '__main__':
    while True:
        Check_Com()
        time.sleep(10)
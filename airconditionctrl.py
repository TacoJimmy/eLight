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
    
    #check ACTempature
    if APPCommd['ACTemp'] == ACSet['ACTemp']:
        print("chekc01")
    else:
        print("chekc02")
        
        
        ACSet['ACTemp'] = APPCommd['ACTemp']
        with open('SetACctrl.json', 'w') as CtrlFuntion:
            json.dump(ACSet, CtrlFuntion)
            CtrlFuntion.close
    
    #check FanSpeed
    if APPCommd['Fanspeed'] == ACSet['Fanspeed']:
        print("chekc03")
    else:
        print("chekc04")
        
        
        ACSet['Fanspeed'] = APPCommd['Fanspeed']
        with open('SetACctrl.json', 'w') as CtrlFuntion:
            json.dump(ACSet, CtrlFuntion)
            CtrlFuntion.close
    #check ACOnOff
    if APPCommd['ACOnOff'] == ACSet['ACOnOff']:
        print("chekc05")
    else:
        print("chekc06")
        
        
        ACSet['ACOnOff'] = APPCommd['ACOnOff']
        with open('SetACctrl.json', 'w') as CtrlFuntion:
            json.dump(ACSet, CtrlFuntion)
            CtrlFuntion.close

if __name__ == '__main__':
    while True:
        Check_Com()
        time.sleep(10)
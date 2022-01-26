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
    if APPCommd['ACTemp'] < 30 and APPCommd['ACTemp'] > 0: 
        if APPCommd['ACTemp'] == ACSet['ACTemp']:
            ACSet['ACTemp'] = APPCommd['ACTemp']
            with open('SetACctrl.json', 'w') as CtrlFuntion:
                json.dump(ACSet, CtrlFuntion)
                CtrlFuntion.close
    
    #check FanSpeed
    if APPCommd['Fanspeed'] < 70 and APPCommd['Fanspeed'] > 10:
        if APPCommd['Fanspeed'] != ACSet['Fanspeed']:
            ACSet['Fanspeed'] = APPCommd['Fanspeed']
            with open('SetACctrl.json', 'w') as CtrlFuntion:
                json.dump(ACSet, CtrlFuntion)
                CtrlFuntion.close
    #check ACOnOff
    if APPCommd['ACOnOff'] == 0 or APPCommd['ACOnOff'] == 1:
        if APPCommd['ACOnOff'] != ACSet['ACOnOff']:
            ACSet['ACOnOff'] = APPCommd['ACOnOff']
            with open('SetACctrl.json', 'w') as CtrlFuntion:
                json.dump(ACSet, CtrlFuntion)
                CtrlFuntion.close

if __name__ == '__main__':
    while True:
        Check_Com()
        time.sleep(10)
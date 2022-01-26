import time
import json
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
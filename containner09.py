
import time
import schedule

import airconditioninfor
import soilsensor

def send_mqtt():
    AC_contain = airconditioninfor.AC_infor('/dev/ttyS4',1)
    airconditioninfor.on_AC_publish(AC_contain)
    print(AC_contain)
    soil_contain = soilsensor.soil_infor('/dev/ttyS1')
    soilsensor.on_soil_publish(soil_contain)
    print(soil_contain)

		
#schedule.every(5).minutes.do(send_mqtt)
schedule.every(10).seconds.do(send_mqtt)

while True:
    schedule.run_pending()
    #data = soil_infor('/dev/ttyS1')
    #print(data)
    time.sleep(3)



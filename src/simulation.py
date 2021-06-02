from WIFI_scann import WIFI_scann
from Mqtt_manager import Mqtt_Manager
import time

wifis = Mqtt_Manager("localhost", "rssi_mac") #accelerometer_LSM303AGR

while True:
    time.sleep(0.1)
    if wifis.processed_data:
        print(wifis.processed_data[0])


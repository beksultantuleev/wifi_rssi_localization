
import sys
import os
import inspect
import numpy as np
from APmanager import APmanager
from Mqtt_manager import Mqtt_Manager
import time

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from rssi_module.rssi import RSSI_Localizer, RSSI_Scan
from rssi_module import rssi

class WIFI_Manager():
    def __init__(self, interface='wlo1'):
        self.interface = interface
        self.list_of_found_aps = []
        self.targeted_aps = []
        self.targeted_aps_sorted = []
        self.rssi_scanner = rssi.RSSI_Scan(self.interface)
        self.ap_manager = APmanager()
        # try to do smth with rssi localizer

    def localizer_instance(self):
        accessPoints = self.ap_manager.get_sorted_ap_list()
        self.rssi_localizer_instance = RSSI_Localizer(accessPoints)
        return self.rssi_localizer_instance

    def get_sorted_rssi(self, sub_li):
        "for mqtt"
        sorted_rssi = [] #to see mac as well
        srt = sorted(sub_li, key=lambda x: x[0])
        for rssi in srt:
            sorted_rssi.append(rssi[1])
        return sorted_rssi

if __name__ == "__main__":
    test = WIFI_Manager()
    "set anchors"
    test.ap_manager.add_anchor_ap(
        attenuation=2, x=2, y=0, distance=2, signal=-45, name="xzp", mac='84:c7:ea:85:d2:41')
    test.ap_manager.add_anchor_ap(
        attenuation=2, x=4, y=2, distance=2, signal=-32, name="sky", mac='00:22:3F:54:86:2A'.lower())
    test.ap_manager.add_anchor_ap(
        attenuation=2, x=0, y=1.5, distance=2, signal=-22, name="White castle 2.4Ghz", mac='C0:05:C2:AA:41:99'.lower())
    accessPoints = test.ap_manager.get_sorted_ap_list()
    # print(f"this is aps >> {accessPoints}")


    mqttCon = Mqtt_Manager("localhost", "rssi_mac")
    while True:
        time.sleep(0.2)
        if mqttCon.processed_data:
            rssis = test.get_sorted_rssi([['84:c7:ea:85:d2:41', -45+(np.random.randint(-3,3))], ['00:22:3F:54:86:2A'.lower(), -32], ['C0:05:C2:AA:41:99'.lower(), -22]])#test.get_sorted_rssi(mqttCon.processed_data)
            print(rssis)
            if len(rssis)<3:
                raise Exception("one of ap died")
            position = test.localizer_instance().getNodePosition(
                rssis)
            print(f"x={position[0][0]}, y = {position[1][0]}")
            mqttCon.publish("position", f"{[[position[0][0], position[1][0]]]}")

    


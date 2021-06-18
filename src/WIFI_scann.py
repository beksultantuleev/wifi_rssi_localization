
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

class WIFI_scann():
    def __init__(self, interface='wlo1'):
        self.interface = interface
        self.list_of_found_aps = []
        self.targeted_aps = []
        self.targeted_aps_sorted = []
        self.rssi_scanner = rssi.RSSI_Scan(self.interface)
        self.ap_manager = APmanager()
        # try to do smth with rssi localizer

    def scann_all_aps(self):
        self.list_of_found_aps = self.rssi_scanner.getAPinfo(
            networks=None, sudo=True)
        print(self.list_of_found_aps)

    def get_all_aps(self):
        return self.list_of_found_aps

    def targeted_ap_scann(self, target_list):
        self.targeted_aps = self.rssi_scanner.getAPinfo(
            networks=target_list, sudo=True)
        self.targeted_aps_sorted = sorted(
            self.targeted_aps, key=self.ap_manager.sortkeypicker(["mac"]))
        print(self.targeted_aps_sorted)

    def get_targeted_aps(self):
        return self.targeted_aps_sorted

    def localizer_instance(self):
        accessPoints = self.ap_manager.get_sorted_ap_list()
        self.rssi_localizer_instance = RSSI_Localizer(accessPoints)
        return self.rssi_localizer_instance

    def get_targeted_ap_rssi(self):
        rssi_values = []
        # ap_ssid = []
        for aps in self.get_targeted_aps():
            rssi_values.append(aps['signal'])
            # ap_ssid.append(aps['ssid'])
        return rssi_values

    def get_sorted_rssi(self, sub_li):
        "for mqtt"
        sorted_rssi = [] #to see mac as well
        srt = sorted(sub_li, key=lambda x: x[0])
        for rssi in srt:
            sorted_rssi.append(rssi[1])
        return sorted_rssi

    def get_sorted_mac(self, sub_li):
        "for mqtt"
        sorted_mac = [] #to see mac as well
        srt = sorted(sub_li, key=lambda x: x[0])
        for rssi in srt:
            sorted_mac.append(rssi[0])
        return sorted_mac

if __name__ == "__main__":
    test = WIFI_scann()
    # test.ap_manager.add_anchor_ap(
    #     attenuation=6, x=0, y=0, distance=3, signal=-48, name="mini", mac='84:00:d2:7b:03:d0')
    test.ap_manager.add_anchor_ap(
        attenuation=2, x=2, y=0, distance=2, signal=-45, name="xzp", mac='84:c7:ea:85:d2:41')
    # test.ap_manager.add_anchor_ap(
    #     attenuation=4, x=4, y=6, distance=3, signal=-53, name="vivo", mac='18:e2:9f:7f:8c:d6')

    # test.ap_manager.add_anchor_ap(
    #     attenuation=2, x=1, y=0, distance=3, signal=-48, name="xzp", mac='84:c7:ea:85:d2:41'.lower())
    test.ap_manager.add_anchor_ap(
        attenuation=2, x=4, y=2, distance=2, signal=-32, name="sky", mac='00:22:3F:54:86:2A'.lower())
    test.ap_manager.add_anchor_ap(
        attenuation=2, x=0, y=1.5, distance=2, signal=-22, name="VM24ghz", mac='C0:05:C2:AA:41:99'.lower())
    test.ap_manager.add_anchor_ap(
        attenuation=4, x=0, y=1.5, distance=2, signal=-37, name="VM5ghz", mac='C0:05:C2:AA:41:9F'.lower())
    accessPoints = test.ap_manager.get_sorted_ap_list()
    # print(f"this is aps >> {accessPoints}")

    rssi_localizer_instance = test.localizer_instance()

    # test.targeted_ap_scann(['VIVO HOTSPOT', "Xperia mini", "Xperia xzp"])
    test.targeted_ap_scann(['VM6282415', "SKY65394", "Xperia xzp"])
    mqttCon = Mqtt_Manager("localhost", "rssi_mac")
    while True:
        time.sleep(0.2)
        if mqttCon.processed_data:
            rssis = test.get_sorted_rssi(mqttCon.processed_data)
            if len(rssis)<3:
                raise Exception("one of ap died")
            position = rssi_localizer_instance.getNodePosition(
                rssis)
            print(f"x={position[0][0]}, y = {position[1][0]}")
            mqttCon.publish("position", f"{[[position[0][0], position[1][0]]]}")

    


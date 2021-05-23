import sys
import os
import inspect
import numpy as np
from APmanager import APmanager

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from rssi_module import rssi
from rssi_module.rssi import RSSI_Localizer, RSSI_Scan


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
        accessPoints = test.ap_manager.get_sorted_ap_list()
        self.rssi_localizer_instance = RSSI_Localizer(accessPoints)
        return self.rssi_localizer_instance

    def get_targeted_ap_rssi(self):
        rssi_values = []
        # ap_ssid = []
        for aps in self.get_targeted_aps():
            rssi_values.append(aps['signal'])
            # ap_ssid.append(aps['ssid'])
        return rssi_values


if __name__ == "__main__":
    test = WIFI_scann()
    test.ap_manager.add_anchor_ap(
        attenuation=6, x=0, y=0, distance=3, signal=-48, name="mini", mac='84:00:D2:7B:03:D0')
    test.ap_manager.add_anchor_ap(2, 0, 6, 4, -53, "xzp", '84:C7:EA:85:D2:41')
    test.ap_manager.add_anchor_ap(4, 4, 6, 3, -53, "vivo", '18:E2:9F:7F:8C:D6')
    accessPoints = test.ap_manager.get_sorted_ap_list()
    # print(f"this is aps >> {accessPoints}")

    rssi_localizer_instance = test.localizer_instance()

    test.targeted_ap_scann(['VIVO HOTSPOT', "Xperia mini", "Xperia xzp"])
    position = rssi_localizer_instance.getNodePosition(
        test.get_targeted_ap_rssi())
    # print(f"this is targets rssis >>{test.get_targeted_ap_rssi()}")
    distance = RSSI_Localizer.getDistancesForAllAPs(
    rssi_localizer_instance, test.get_targeted_ap_rssi())
    print(f"this is distance > {distance}")
    # print(test.ap_manager.get_sorted_ap_list()) #ancor aps
    # print(test.ap_manager.get_ap_list())
    print(f"x={position[0]}, y = {position[1]}")
    # print(accessPoints)
    # test.scann_all_aps()
    # print(test.get_all_aps())

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


class WIFI_rssi_localization():
    def __init__(self, interface='wlo1'):
        self.interface = interface
        self.list_of_found_aps = []
        self.targeted_aps = []
        self.rssi_scanner = rssi.RSSI_Scan(self.interface)
        self.ap_manager = APmanager()
        #try to do smth with rssi localizer
        # self.rssi_localizer_instance = RSSI_Localizer(accessPoints=self.ap_manager.g)

    def scann_all_aps(self):
        self.list_of_found_aps = self.rssi_scanner.getAPinfo(
            networks=None, sudo=True)

    def get_all_aps(self):
        return self.list_of_found_aps

    def targeted_ap_scann(self, target_list):
        self.targeted_aps = self.rssi_scanner.getAPinfo(
            networks=target_list, sudo=True)

    def get_targeted_aps(self):
        return self.targeted_aps
    
    # def add_ap(self, atten, x, y, dist):
    #     self.ap_manager.add_ap(atten, x, y, dist, signal, name))

if __name__ == "__main__":
    test = WIFI_rssi_localization()
    test.ap_manager.add_ap(3,4,3,43,-54,"k")
    test.ap_manager.add_ap(3,4,3,43,-54,"a")
    test.ap_manager.add_ap(3,4,3,43,-54,"b")
    accessPoints = test.ap_manager.get_sorted_ap_list()
    print(accessPoints)
    # test.scann_all_aps()
    # print(test.get_all_aps())
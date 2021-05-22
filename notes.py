from rssi_module.rssi import RSSI_Localizer, RSSI_Scan
from rssi_module import rssi
import numpy as np


interface = 'wlo1'  # wlo1
rssi_scanner = rssi.RSSI_Scan(interface)
# ssids = ['unitn-x']
ssids = ['VIVO HOTSPOT', "Xperia mini", "Xperia xzp"]

ap_info = rssi_scanner.getAPinfo(networks=None, sudo=True)

print(ap_info)
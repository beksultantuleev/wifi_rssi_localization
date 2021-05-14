from os import truncate
from rssi_module import rssi
from rssi_module.rssi import RSSI_Localizer
import json

interface = 'wlo1' #wlo1
rssi_scanner = rssi.RSSI_Scan(interface)


# ssids = ['VIVO HOTSPOT', "Xperia mini"]
ssids = ['unitn-x']
accessPoint = {
     'signalAttenuation': 3, 
     'location': {
         'y': 1, 
         'x': 1
     }, 
     'reference': {
         'distance': 4, 
         'signal': -52
     }, 
     'name': 'target_WIFI'
}
# sudo argument automatixally gets set for 'false', if the 'true' is not set manually.
# python file will have to be run with sudo privileges.
ap_info = rssi_scanner.getAPinfo(sudo=True, networks=ssids)

# target = "b4:fb:e4:c7:99:44"
# target = "b6:fb:e4:c7:95:73"
# for network in ap_info:
#     if network["mac"] == target.upper():
#         print(f'{network["signal"]} and {network["ssid"]}')
#     else:
#         print("no network found")
# rssi_values = [ap['signal'] for ap in ap_info]


signalStrength = -44
position = RSSI_Localizer.getDistanceFromAP(accessPoint, signalStrength)

print(position)
# print(ap_info)
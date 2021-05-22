from rssi_module.rssi import RSSI_Localizer, RSSI_Scan
from rssi_module import rssi
import numpy as np


interface = 'wlo1'  # wlo1
rssi_scanner = rssi.RSSI_Scan(interface)
# ssids = ['unitn-x']
ssids = ['VIVO HOTSPOT', "Xperia mini", "Xperia xzp"]

ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)


"Localizer"
accessPoints = [{
    'signalAttenuation': 3,
    'location': {
        'y': 0,
        'x': 0
    },
    'reference': {
        'distance': 3,
        'signal': -48
    },
    'name': 'mini'
},
    {
        'signalAttenuation': 2,
        'location': {
            'y': 6,
            'x': 0
        },
        'reference': {
            'distance': 4,
            'signal': -53
        },
        'name': 'xzp'
}, {
        'signalAttenuation': 2,
        'location': {
            'y': 6,
            'x': 4
        },
        'reference': {
            'distance': 3,
            'signal': -53
        },
        'name': 'vivo'
}]


"Localizer"
# change according to needs (1 or several aps)
rssi_localizer_instance = RSSI_Localizer(accessPoints=accessPoints)

# distance = RSSI_Localizer.getDistancesForAllAPs(rssi_localizer_instance, [-43,-54]) #for mult aps
# distance = RSSI_Localizer.getDistanceFromAP(accessPoint, 56)  # for single ap

# print(ap_info)

"self localization"

# rssi_values = [ap['signal'] for ap in ap_info]
# ap_ssid = [ap['ssid'] for ap in ap_info]
rssi_values = []
ap_ssid = []
for aps in ap_info:
    rssi_values.append(aps['signal'])
    ap_ssid.append(aps['ssid'])
    # print(f"ssid: {aps['ssid']}, rssi: {aps['signal']}, quality: {aps['quality']}")


ziped_v = set(zip(ap_ssid, rssi_values))
print(f"{ziped_v}")

distance = RSSI_Localizer.getDistancesForAllAPs(
    rssi_localizer_instance, rssi_values)  # for mult aps
print(f"this is distance dict> {distance}")
position = rssi_localizer_instance.getNodePosition(rssi_values)
print(f"x > {position[0]}, y > {position[1]}")
print(f"this is rssi values order >>{rssi_values}")

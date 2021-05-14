from rssi_module.rssi import RSSI_Localizer, RSSI_Scan
from rssi_module import rssi
accessPoint = {
     'signalAttenuation': 3, 
     'location': {
         'y': 10, 
         'x': 0
     }, 
     'reference': {
         'distance': 4, 
         'signal': -52
     }, 
     'name': 'dd-wrt'
}
signalStrength = -57

distance = RSSI_Localizer.getDistanceFromAP(accessPoint, signalStrength)
print(distance)
# RSSI_Localizer.getNodePosition()
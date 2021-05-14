from rssi_module.rssi import RSSI_Localizer, RSSI_Scan
from rssi_module import rssi


interface = 'wlo1' #wlo1
rssi_scanner = rssi.RSSI_Scan(interface)
ssids = ['unitn-x']

ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)
rssi_values = [ap['signal'] for ap in ap_info]
position = RSSI_Localizer.getNodePosition(rssi_values, -52)
print(position)
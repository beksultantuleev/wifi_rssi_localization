# from numpy.core.fromnumeric import sort
from WIFI_scann import WIFI_scann
from Mqtt_manager import Mqtt_Manager
import time

sim = WIFI_scann()
"set anchors"
sim.ap_manager.add_anchor_ap(
    attenuation=3, x=0, y=0, distance=3, signal=-55, name="mini", mac='84:00:D2:7B:03:D0')
sim.ap_manager.add_anchor_ap(
    attenuation=3, x=6, y=0, distance=3, signal=-45, name="xzp", mac='84:C7:EA:85:D2:41')
sim.ap_manager.add_anchor_ap(
    attenuation=3, x=6, y=3, distance=3, signal=-40, name="vivo", mac='18:E2:9F:7F:8C:D6')


"initialize localizer"
rssi_localizer_instance = sim.localizer_instance()

"set aps in the room"
targeted_list = ['VIVO HOTSPOT', "Xperia mini", "Xperia xzp"]
sim.targeted_ap_scann(targeted_list)

"start mqtt"
mqttCon = Mqtt_Manager("localhost", "rssi_mac")
while True:
    time.sleep(0.2)
    if mqttCon.processed_data:
        rssis = sim.get_sorted_rssi(mqttCon.processed_data)
        if len(rssis) < len(targeted_list):
            raise Exception("one of ap died")
        position = rssi_localizer_instance.getNodePosition(
            rssis)
        print(f"x={position[0]}, y = {position[1]}, v m x > {sim.get_sorted_rssi(mqttCon.processed_data)}")

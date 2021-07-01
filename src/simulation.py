# from numpy.core.fromnumeric import sort
from WIFI_Manager import WIFI_Manager
from Mqtt_manager import Mqtt_Manager
import time
import numpy as np
from Plot_Manager import Plot_manager

anchors = [[0, 0, "anchor1"], [10, 7, "anchor2"],
            [10, 0, "anchor3"], [0, 7, "anchor4"]]
# anchors = [[2, 0, "xzp"], [4, 2, "sky"],
#            [0, 1.5, "vm"]]
room_size = [0, 0, 7, 10]  # x1, y1, x2, y2
map = Plot_manager(topic="position", room_size=room_size, anchor_list=anchors, host="localhost") #positions position
map.run()




simulation = WIFI_Manager()
"set anchors"
simulation.ap_manager.add_anchor_ap(
    attenuation=2, x=2, y=0, distance=2, signal=-45, name="xzp", mac='84:c7:ea:85:d2:41')
simulation.ap_manager.add_anchor_ap(
    attenuation=2, x=4, y=2, distance=2, signal=-32, name="sky", mac='00:22:3F:54:86:2A'.lower())
simulation.ap_manager.add_anchor_ap(
    attenuation=2, x=0, y=1.5, distance=2, signal=-22, name="White castle 2.4Ghz", mac='C0:05:C2:AA:41:99'.lower())
accessPoints = simulation.ap_manager.get_sorted_ap_list()
# print(f"this is aps >> {accessPoints}")


mqttCon = Mqtt_Manager("localhost", "rssi_mac")
while True:
    time.sleep(0.2)
    if mqttCon.processed_data:
        rssis = simulation.get_sorted_rssi([['84:c7:ea:85:d2:41', -45+(np.random.randint(-3,3))], ['00:22:3F:54:86:2A'.lower(), -32], ['C0:05:C2:AA:41:99'.lower(), -22]])#test.get_sorted_rssi(mqttCon.processed_data)
        print(rssis)
        if len(rssis)<3:
            raise Exception("one of ap died")
        position = simulation.localizer_instance().getNodePosition(
            rssis)
        print(f"x={position[0][0]}, y = {position[1][0]}")
        mqttCon.publish("position", f"{[[position[0][0], position[1][0]]]}")

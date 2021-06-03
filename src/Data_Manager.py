
import csv
import random
import time
from Mqtt_manager import Mqtt_Manager


class Data_Manager:
    def __init__(self):
        self.fieldnames = ["index", "posX", "posY", "posZ"]
        self.x_value = 1
        self.posX = 0
        self.posY = 0
        self.posZ = 0

        with open('positions.csv', 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            csv_writer.writeheader()

    def start(self, X, Y, Z):

        with open('positions.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)

            info = {
                "index": self.x_value,
                "posX": X,
                "posY": Y,
                "posZ": Z
            }

            csv_writer.writerow(info)
            print(X, Y, Z)

            self.x_value += 1



if __name__ == "__main__":
    test = Data_Manager()
    mqtt = Mqtt_Manager("localhost", "top")
    while True:
        if len(mqtt.processed_data)>0:
            test.start(mqtt.processed_data[0], mqtt.processed_data[2], "yes")
            time.sleep(0.5)

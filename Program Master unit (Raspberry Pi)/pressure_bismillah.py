# Python code for connecting Arduino to Python
# That's Engineering
# 29/04/2020

import serial
import time
import schedule

from urllib import request
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json as jsonLib
import urllib.request


class JsonData:

    def __init__(self):
        self.URLpost = ""
        self.postingData = ""

        self.requestpostPressure = ""
        self.nilaiPressure = ""
        self.hasilPostPressure = ""

    def postData(self, URL, bar):
        self.URLpost = URL
        self.nilaiPressure = bar

        self.postingData = {'bar': self.nilaiPressure}
        # self.requestpostPressure = requests.post(
        #     url=self.URLpost, data=self.postData)

        self.requestpostPressure = Request(
            self.URLpost, urlencode(self.postingData).encode())

        self.hasilPostPressure = urlopen(
            self.requestpostPressure).read().decode()

        print("respon api input sakelar mesin {}".format(
            self.hasilPostPressure))


class SlavePressure(JsonData):

    def __init__(self):
        print("ini masuk kelas coba")
        self.insQuery = ""
        self.URLpostPressure = ""

    def main_func(self):
        self.URLpostPressure = "http://polmanpms.online/general/postpressure"
        self.arduino = serial.Serial(port='/dev/ttyUSB1', baudrate=9600)
        print('Established serial connection to Arduino')
        self.arduino_data = self.arduino.readline()
        print(self.arduino_data)

        # self.decoded_values = str(
        # self.arduino_data[0:len(self.arduino_data)].decode("utf-8"))
        self.decoded_values = str(
            self.arduino_data.decode("utf-8"))
        print(self.decoded_values)
        self.list_values = self.decoded_values.split('x')

        for self.item in self.list_values:
            list_in_floats.append(float(self.item))

        print(f'Collected readings from Arduino: {list_in_floats}')
        print("list in float adalah {}".format(self.item))

        table = "pressure_transmitter"
        super().__init__()
        super().postData(self.URLpostPressure, self.item)

        self.arduino_data = 0
        list_in_floats.clear()
        list_values.clear()

        self.arduino.close()
        print('Connection closed')
        print('<----------------------------->')
        
        # return item


# ----------------------------------------Main Code------------------------------------
# Declare variables to be used
list_values = []
list_in_floats = []

print('Program started')

# Setting up the Arduino
asd = SlavePressure().main_func()
schedule.every(2).seconds.do(SlavePressure().main_func)

while True:
    schedule.run_pending()
    time.sleep(5)

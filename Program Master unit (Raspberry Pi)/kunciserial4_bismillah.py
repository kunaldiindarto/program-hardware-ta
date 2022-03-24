# validation key for operating machine
import requests
import serial
import time

from urllib import request
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json as jsonLib
import urllib.request


class JsonData:

    def __init__(self):
        self.URLget = ""
        self.URLpost = ""
        self.postingData = ""
        self.URLloop = ""
        self.data = ""
        self.r = ""
        self.requ = ""
        self.reque = ""

        self.requestpostStatusMesin = ""
        self.statusMesin = ""
        self.hasilpostStatusMesin = ""

    def getData(self, URLget):
        self.URLget = URLget
        self.requ = urllib.request.Request(self.URLget, data=None, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        })
        self.r = urllib.request.urlopen(self.requ)
        self.data = jsonLib.loads(self.r.read())
        print("ini di dalam kelas json untuk ambil data")
        print(self.data)

    def postData(self, URLin, stating):
        self.URLpost = URLin
        self.statusMesin = stating

        self.postingData = {'status': self.statusMesin}

        self.requestpostStatusMesin = Request(
            self.URLpost, urlencode(self.postingData).encode(), headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            })

        self.hasilpostStatusMesin = urlopen(
            self.requestpostStatusMesin).read().decode()

        print("respon api input sakelar mesin {}".format(
            self.hasilpostStatusMesin))

    @property
    def getHasil(self):
        pass

    @getHasil.getter
    def getHasil(self):
        return self.data

    @getHasil.setter
    def reset6(self, resettt):
        self.data = resettt


class Komdat:
    def __init__(self, mulai):

        self.mulai = mulai
        self.arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
        # self.pressure = serial.Serial(port='COM4', baudrate=9600)

        self.data = ""
        self.hasil = ""
        self.loopback = ""
        self.result = ""

    def sendtoArduino(self, data):

        self.hasil = self.arduino.write(bytes(data, 'utf-8'))
        # print("nilai yang dikirim adalah {}".format(self.hasil))
        time.sleep(0.05)

        # print("hasil")
        # print("response dari arduino adalah {}".format(self.result))
        # print("response dari arduino adalah aaa {}".format(self.loopback))

    def receiveData(self):
        self.loopback = self.arduino.readline().strip()
        self.result = str(self.loopback.decode('utf-8', 'ignore'))

    @property
    def getSendValue(self):
        pass

    @getSendValue.getter
    def getSendValue(self):
        return self.hasil

    @getSendValue.setter
    def getSendValue(self, reset):
        self.hasil = reset

    @property
    def getResult(self):
        pass

    @getResult.getter
    def getResult(self):
        return self.result

    @getResult.setter
    def getResult(self, reset):
        self.result = reset


# void setup
json = JsonData()
serin = Komdat('connect')

URLdata = "http://polmanpms.online/general"
URLpostSta1 = "http://polmanpms.online/general/poststat1"
URLpostSta2 = "http://polmanpms.online/general/poststat2"
URLpostSta3 = "http://polmanpms.online/general/poststat3"
URLpostSta4 = "http://polmanpms.online/general/poststat4"

# void loop
while True:
    fetchData = json.getData(URLdata)

    keyM1 = str(json.getHasil['key'])

    print("status kunci m1 adalah {}".format(keyM1))
    time.sleep(2)
    if keyM1 == "lockon1":
        key1 = '1'
        kirim = serin.sendtoArduino(key1)

    else:
        key1 = '0'
        kirim = serin.sendtoArduino(key1)

    print("loop")
    serin.receiveData()
    statM1 = str(serin.getResult)
    print("status mesin adalah: {}".format(statM1))

    if statM1 == "on1":
        print("mesin 1 on")
        json.postData(URLpostSta1, statM1)

    if statM1 == 'off1':
        print("mesin 1 off")
        json.postData(URLpostSta1, statM1)

    if statM1 == "on2":
        print("mesin 2 on")
        json.postData(URLpostSta2, statM1)

    if statM1 == 'off2':
        print("mesin 2 off")
        json.postData(URLpostSta2, statM1)

    if statM1 == 'on3':
        print("mesin 3 on")
        json.postData(URLpostSta3, statM1)

    if statM1 == 'off3':
        print("mesin 3 off")
        json.postData(URLpostSta3, statM1)

    if statM1 == 'on4':
        print("mesin 4 on")
        json.postData(URLpostSta4, statM1)
    if statM1 == 'off4':
        print("mesin 4 off")
        json.postData(URLpostSta4, statM1)

    # time.sleep(0.5)

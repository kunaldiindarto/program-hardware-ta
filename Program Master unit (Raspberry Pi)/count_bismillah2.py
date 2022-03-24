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

        self.requestpostCounting = ""
        self.counting = ""
        self.hasilpostCounting = ""
        self.requ = ""
        self.reque = ""

    def getData(self, URLget):
        self.URLget = URLget
        self.requ = urllib.request.Request(self.URLget, data=None, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        })
        self.r = urllib.request.urlopen(self.requ)
        self.data = jsonLib.loads(self.r.read())
        print("ini di dalam kelas json untuk ambil data")
        print(self.data)

    def postData(self, URL, counting):
        self.URLpost = URL
        self.counting = counting

        self.postingData = {'process': self.counting}

        self.requestpostCounting = Request(
            self.URLpost, urlencode(self.postingData).encode(), headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            })

        self.hasilpostCounting = urlopen(
            self.requestpostCounting).read().decode()

        print("respon api input sakelar mesin {}".format(
            self.hasilpostCounting))

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
        self.arduino = serial.Serial(port='/dev/ttyUSB2', baudrate=9600)
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
        self.result = self.loopback.decode('utf-8', 'ignore')

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

URLdata = "http://polmanpms.online/general"
URLprocess1 = "http://polmanpms.online/general/postprocess"
URLprocess2 = "http://polmanpms.online/general/postprocess2"
URLprocess3 = "http://polmanpms.online/general/postprocess3"
URLprocess4 = "http://polmanpms.online/general/postprocess4"

serin = Komdat('connect')
out1 = 0
out2 = 0
out3 = 0
out4 = 0


# void loop
while True:
    fetchData = json.getData(URLdata)

    keyM1 = str(json.getHasil['key'])
    # time.sleep(2)

    if keyM1 == "lockon1":  # ? validasi kunci
        serin.receiveData()
        statM1 = str(serin.getResult)
        print(statM1)

        if statM1 == "count1":
            out1 += 1
            print("nilai output 1 adalah {}".format(out1))
            json.postData(URLprocess1, out1)

        elif statM1 == "count2":
            out2 += 1
            json.postData(URLprocess2, out2)

        elif statM1 == "count3":
            out3 += 1
            json.postData(URLprocess3, out3)

        elif statM1 == "count4":
            out4 += 1
            json.postData(URLprocess4, out4)

    else:
        print("kunci harus dibuka dulu coy")

    time.sleep(3)

import time
import datetime
import math

from datetime import timedelta

from urllib import request
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json as jsonLib
import urllib.request


class JsonData:

    def __init__(self):
        self.URLget = ""
        self.URLpost = ""
        self.URLloop = ""
        self.data = ""
        self.r = ""

        self.postLifetime = ""
        self.jamLifetime = 0
        self.menitLifetime = 0.0
        self.detikLifetime = 0.0
        self.deskripsiLifetime = ""

        self.hariLifetime = 0
        self.jamLifetime = 0
        self.menitLifetime = 0
        self.detikLifetime = 0
        self.requestpostLifetime = ""
        self.hasilpostLifeTime = ""

        self.statusBlink = ""

# *inisialisasi untuk getdataloop
        self.req = ""
        self.data2 = ""
        self.stat4 = ""

# *inisialisasi untuk post Blink
        self.postStatusBlink = ""
        self.postDetailBlink = ""
        self.postBlinkk = ""
        self.URLpostBlink = ""

        self.requ = ""
        self.reque = ""

    def getData(self, URLget):
        self.URLget = URLget
        self.requ = urllib.request.Request(self.URLget, data=None, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        })
        # self.r = requests.get(url=self.URLget)
        # self.data = self.r.json()
        self.r = urllib.request.urlopen(self.requ)
        self.data = jsonLib.loads(self.r.read())
        print("ini di dalam kelas json untuk ambil data")
        print(self.data)

    def getDataLoop(self, URLloop):
        self.URLloop = URLloop
        # self.req = requests.get(url=self.URLloop)
        # self.data2 = self.req.json()
        self.reque = urllib.request.Request(self.URLloop, data=None, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        })
        self.req = urllib.request.urlopen(self.reque)
        self.data2 = jsonLib.loads(self.req.read())
        # print(self.data2)
        print("ini di dalam kelas json untuk ambil data")
        self.stat4 = str(self.data2['stat1'][0]['status'])

        self.hariLifetime = int(self.data2['lifetime']['hari'])
        self.jamLifetime = int(self.data2['lifetime']['jam'])
        self.menitLifetime = int(self.data2['lifetime']['menit'])
        self.detikLifetime = int(self.data2['lifetime']['detik'])

        self.statusBlink = str(self.data2['blink'][0]['status'])

        # print("self hari {}".format(self.hariLifetime))

    def postLT(self, URLlifetime, hari, jam, menit, detik):
        self.postLifetime = URLlifetime
        self.jamLifetime = jam
        self.menitLifetime = menit
        self.detikLifetime = detik
        self.hariLifetime = hari

        self.postData = {'hari': self.hariLifetime,
                         'jam': self.jamLifetime,
                         'menit': self.menitLifetime,
                         'detik': self.detikLifetime,
                         }
        # self.requestpostLifetime = requests.post(
        #     url=self.postLifetime, data=self.postData)

        self.requestpostLifetime = Request(
            self.postLifetime, urlencode(self.postData).encode(), headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            })

        self.hasilpostLifeTime = urlopen(
            self.requestpostLifetime).read().decode()

        print("respon api input lifetime {}".format(
            self.hasilpostLifeTime))

    @property
    def getHasil(self):
        pass

    @getHasil.getter
    def getHasil(self):
        return self.data

    @getHasil.setter
    def reset6(self, resettt):
        self.data = resettt

    @property
    def getStat4(self):
        pass

    @getStat4.getter
    def getStat4(self):
        return self.stat4

    @getStat4.setter
    def getStat4(self, resettt):
        self.stat4 = resettt

    @property
    def getHari(self):
        pass

    @getHari.getter
    def getHari(self):
        return self.hariLifetime

    @getHari.setter
    def getHari(self, resettt):
        self.hariLifetime = resettt

    @property
    def getJam(self):
        pass

    @getJam.getter
    def getJam(self):
        return self.jamLifetime

    @getJam.setter
    def getJam(self, resettt):
        self.jamLifetime = resettt

    @property
    def getMenit(self):
        pass

    @getMenit.getter
    def getMenit(self):
        return self.menitLifetime

    @getMenit.setter
    def getMenit(self, resettt):
        self.menitLifetime = resettt

    @property
    def getDetik(self):
        pass

    @getDetik.getter
    def getDetik(self):
        return self.detikLifetime

    @getDetik.setter
    def getDetik(self, resettt):
        self.detikLifetime = resettt

    @property
    def getStatusBlink(self):
        pass

    @getStatusBlink.getter
    def getStatusBlink(self):
        return self.statusBlink

    @getStatusBlink.setter
    def getStatusBlink(self, resettt):
        self.statusBlink = resettt


# ? void setup
URLloop = "http://polmanpms.online/client1/loop"
URLpostLifetime = "http://polmanpms.online/client1/postlifetime"

json = JsonData()
val = 0
val2 = 0

# ? void loop
while True:
    # * baca serial arduino
    # !ganti jadi dari database buat sakelar nya
    json.getDataLoop(URLloop)

    data = str(json.getStat4)
    print(data)

    # * setting life time
    hari = json.getHari
    jam = json.getJam
    menit = json.getMenit
    status = json.getStatusBlink
    print("status blink adalah {}".format(status))

    if data == "on1" and status != "sd":
        # sekarang = datetime.datetime.now()
        sekarang = datetime.datetime.now().replace(microsecond=0)

        if val == 0:
            tujuan = sekarang + timedelta(days=hari, hours=jam, minutes=menit)
            val = val + 1

        selisihSekarang = tujuan - sekarang

        print("selisih sekarang adalah {}".format(selisihSekarang))

        detikSelisih = selisihSekarang.seconds

        hariSelisih = selisihSekarang.days
        jamSelisih = math.floor(detikSelisih // (60 * 60))
        menitSelisih = math.floor((detikSelisih // 60) % 60)

        detikHasil = math.floor(detikSelisih -
                                (jamSelisih * 60 * 60) - (menitSelisih * 60))

        if hariSelisih < 0:
            print("waktu lifetime berhenti")
            hariSelisih = 0
            jamSelisih = 0
            menitSelisih = 0
            detikHasil = 0
            json.postLifetime(URLpostLifetime, hariSelisih,
                              jamSelisih, menitSelisih, detikHasil)
            val = 0

        print("detik hasil adalah {}".format(detikHasil))

        print("countdown life time sekarang adalah {} hari {} jam {} menit {} detik".format(
            hariSelisih, jamSelisih, menitSelisih, detikHasil))

        json.postLT(URLpostLifetime, hariSelisih,
                    jamSelisih, menitSelisih, detikHasil)
    else:
        sekarang = datetime.datetime.now().replace(microsecond=0)

        tujuan = sekarang + timedelta(days=hari, hours=jam, minutes=menit)

        selisihSekarang = tujuan - sekarang

        print("selisih sekarang adalah {}".format(selisihSekarang))

        detikSelisih = selisihSekarang.seconds

        hariSelisih = selisihSekarang.days
        jamSelisih = math.floor(detikSelisih // (60 * 60))
        menitSelisih = math.floor((detikSelisih // 60) % 60)

        detikHasil = math.floor(detikSelisih -
                                (jamSelisih * 60 * 60) - (menitSelisih * 60))

        if hariSelisih < 0:
            print("waktu lifetime berhenti")
            hariSelisih = 0
            jamSelisih = 0
            menitSelisih = 0
            detikHasil = 0
            json.postLifetime(URLpostLifetime, hariSelisih,
                              jamSelisih, menitSelisih, detikHasil)
            val = 0

        if data == "off1" and val != 0 and hariSelisih > 0:
            json.postLT(URLpostLifetime, hariSelisih,
                        jamSelisih, menitSelisih, detikHasil)

            val = 0
            print("nilai val setelah di reset adalah {}".format(val))

        if status == "sd" and val2 == 0 and hariSelisih > 0:
            json.postLT(URLpostLifetime, hariSelisih,
                        jamSelisih, menitSelisih, detikHasil)
            val2 += 1
            print("nilai val2 setelah di reset adalah {}".format(val2))

        print("mesin 1 sekarang posisi off atau shutdown")

    print("program lifetime1")
    time.sleep(19)

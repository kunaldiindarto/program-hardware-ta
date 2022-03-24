import numpy as np
import time

from urllib import request
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json as jsonLib
import urllib.request

# todo inisialisasi nilai


def reset(data):
    data2 = data
    global jamFailure, menitFailure, detikFailure
    global jamMinor, menitMinor, detikMinor
    global failure, minor, freqFailure, freqMinor

    jamFailure = 0
    menitFailure = 0
    detikFailure = 0

    jamMinor = 0
    menitMinor = 0
    detikMinor = 0

    failure = 0
    minor = 0

    freqMinor = 0
    freqFailure = 0


class JsonData:

    def __init__(self):
        self.URLget = ""
        self.URLpost = ""
        self.URLloop = ""
        self.data = ""
        self.r = ""

        self.jamMinor = 0
        self.menitMinor = 0
        self.detikMinor = 0

        self.jamFailure = 0
        self.menitFailure = 0
        self.detikFailure = 0

        self.requestpostMaintenance = ""
        self.hasilpostMaintenance = ""

# *inisialisasi untuk getdataloop
        self.req = ""
        self.data2 = ""
        self.stat4 = ""

        self.mtbf = 0.0
        self.mttr = 0.0

        self.frekuensiFailure = 0
        self.frekuensiMinor = 0

        self.requ = ""
        self.reque = ""

    def getData(self, URLget):
        self.URLget = URLget
        # self.r = requests.get(url=self.URLget)
        # self.data = self.r.json()
        self.requ = urllib.request.Request(self.URLget, data=None, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        })
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
        print("ini di dalam kelas json untuk ambil data")

        print(self.data2)

        self.frekuensiFailure = self.data2['failure_id']
        self.frekuensiMinor = self.data2['minorstop_id']

        self.jamMinor = int(self.data2['minorstop']['jam'])
        self.menitMinor = int(self.data2['minorstop']['menit'])
        self.detikMinor = int(self.data2['minorstop']['detik'])

        self.jamFailure = int(self.data2['failure']['jam'])
        self.menitFailure = int(self.data2['failure']['menit'])
        self.detikFailure = int(self.data2['failure']['detik'])

    def postDataMain(self, URL, mtbf, mttr):
        self.URLpost = URL
        self.dataMTBF = mtbf
        self.dataMTTR = mttr

        self.postData = {'mtbf': self.dataMTBF,
                         'mttr': self.dataMTTR,
                         }
        # self.requestpostMaintenance = requests.post(
        #     url=self.URLpost, data=self.postData)
        self.requestpostMaintenance = Request(
            self.URLpost, urlencode(self.postData).encode(),  headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            })

        self.hasilpostMaintenance = urlopen(
            self.requestpostMaintenance).read().decode()

        print("respon api input maintenance {}".format(
            self.hasilpostMaintenance))

    @property
    def getFrekuensiFailure(self):
        pass

    @getFrekuensiFailure.getter
    def getFrekuensiFailure(self):
        return self.frekuensiFailure

    @getFrekuensiFailure.setter
    def getFrekuensiFailure(self, resettt):
        self.frekuensiFailure = resettt

    @property
    def getfrekuensiMinor(self):
        pass

    @getfrekuensiMinor.getter
    def getfrekuensiMinor(self):
        return self.frekuensiMinor

    @getfrekuensiMinor.setter
    def getfrekuensiMinor(self, resettt):
        self.frekuensiMinor = resettt

    @property
    def getHasil(self):
        pass

    @getHasil.getter
    def getHasil(self):
        return self.data

    @getHasil.setter
    def reset6(self, resettt):
        self.data = resettt


# !mulai loop

# ?mulai


    @property
    def getJamMinor(self):
        pass

    @getJamMinor.getter
    def getJamMinor(self):
        return self.jamMinor

    @getJamMinor.setter
    def getJamMinor(self, resettt):
        self.jamMinor = resettt

    @property
    def getMenitMinor(self):
        pass

    @getMenitMinor.getter
    def getMenitMinor(self):
        return self.menitMinor

    @getMenitMinor.setter
    def getMenitMinor(self, resettt):
        self.menitMinor = resettt

    @property
    def getDetikMinor(self):
        pass

    @getDetikMinor.getter
    def getDetikMinor(self):
        return self.detikMinor

    @getDetikMinor.setter
    def getDetikMinor(self, resettt):
        self.detikMinor = resettt
# ?------------------------------------

# ?mulai failure
    @property
    def getJamFailure(self):
        pass

    @getJamFailure.getter
    def getJamFailure(self):
        return self.jamFailure

    @getJamFailure.setter
    def getJamFailure(self, resettt):
        self.jamFailure = resettt

    @property
    def getMenitFailure(self):
        pass

    @getMenitFailure.getter
    def getMenitFailure(self):
        return self.menitFailure

    @getMenitFailure.setter
    def getMenitFailure(self, resettt):
        self.menitFailure = resettt

    @property
    def getDetikFailure(self):
        pass

    @getDetikFailure.getter
    def getDetikFailure(self):
        return self.detikFailure

    @getDetikFailure.setter
    def getDetikFailure(self, resettt):
        self.detikFailure = resettt
# ?------------------------------------


class Maintenance(JsonData):

    def __init__(self):

        # inisialisasi construct availability
        self.loadingTime = 0  # loading time
        self.operatingTIme = 0
        self.totalDT = 0  # total downtime
        self.A = 0

        self.total_av = 0
        self.pldt = 0
        self.setup = 0
        self.shutdown = 0
        self.setAdjustment = 0

        # *inisialisasi mtbf
        self.fFailure = 0
        self.fMinor = 0
        self.nilaiMTBF = 0.0
        self.operatingTimeMTBF = 0.0
        self.timeFailure2 = 0.0

        # *inisialisasi inheritance
        self.qNumbFailure = ""
        self.qNumbMinStop = ""
        self.konekTable = "maintenance4"

        # *inisialisasi MTTR
        self.timeMinor = 0.0
        self.timeFailure = 0.0
        self.breakdownTime = 0.0
        self.nilaiMTTR = 0.0
        self.URLpostmain = ""

    def availability(self, total_av, pldt, setup, shutdown, set_adjustment):

        self.total_av = total_av
        self.pldt = pldt
        self.setup = setup
        self.shutdown = shutdown
        self.set_adjustment = set_adjustment

        self.loadingTime = self.total_av - self.pldt
        # print("loading time {}".format(self.loadingTime))
        self.totalDT = self.setup + self.shutdown + self.set_adjustment
        # print("total downtime adalah: {}".format(self.totalDT))
        self.operatingTIme = self.loadingTime - self.totalDT

        self.A = round(((self.operatingTIme) / self.loadingTime * 100), 2)
        # print("nilai availability: {}".format(self.A))
        # print("nilai operating time updated: {}".format(self.operatingTIme))

    def MTBF(self, failure, fFailure, fMinor):

        self.fFailure = int(fFailure)
        self.fMinor = int(fMinor)
        # ! operation time pada mtbf merupokan downtime yang tidak di planning (failure aja)
        self.timeFailure2 = failure

        self.operatingTimeMTBF = self.loadingTime - self.timeFailure2
        print("self loading time {}".format(self.loadingTime))
        print("self time failure {}".format(self.timeFailure2))
        print("self time failure {}".format(self.timeFailure2))

        # self.fBreakdown = self.fFailure + self.fMinor - 1
        self.fBreakdown2 = self.fFailure + self.fMinor - 1

        # self.nilaiMTBF = round(self.operatingTIme / self.fBreakdown, 2)
        if self.fFailure > 1:
            self.fFailure -= 1

        print("self failure {}".format(self.fFailure))
        self.nilaiMTBF = round((self.operatingTimeMTBF) / self.fFailure, 2)
        print("nilai operating time adalah {}".format(self.operatingTimeMTBF))
        # print("nilai frekuensi breakdown total adalah {}".format(self.fBreakdown2))
        print("nilai MTBF adalah {}".format(self.nilaiMTBF))

    def MTTR(self, URL, minor, failure):

        super().__init__()
        self.URLpostmain = URL
        self.timeMinor = float(minor)
        self.timeFailure = failure
        self.breakdownTime = round(self.timeMinor + self.timeFailure, 2)

        # self.nilaiMTTR = round(self.breakdownTime / self.fBreakdown, 2)
        self.nilaiMTTR = round(self.timeFailure / self.fFailure, 2)
        print("nilai mttr adalah {}".format(self.nilaiMTTR))

        # ? masukin ke database nilai mtbf dan mttr
        super().postDataMain(self.URLpostmain, self.nilaiMTBF, self.nilaiMTTR)
    # def restValue(self):
    #     self.fFailure = 0
    #     self.fMinor = 0
    #     self.fBreakdown = 0
    #     self.nilaiMTBF = 0.0
    #     print("reset nilai mtbf berhasil")

    @ property
    def getAvailability(self):
        pass

    @ getAvailability.getter
    def getAvailability(self):
        return self.A

    @ getAvailability.setter
    def getAvailability(self, reset):
        self.A = reset

    @ property
    def getOperatingTime(self):
        pass

    @ getOperatingTime.getter
    def getOperatingTime(self):
        return self.operatingTIme

    @ getOperatingTime.setter
    def getOperatingTime(self, reset):
        self.operatingTIme = reset


# void setup
URLweb = "http://polmanpms.online/client3"
URLloop = "http://polmanpms.online/client3/loop"
URLpostMaintenance = "http://polmanpms.online/client3/postmaintenance"

json = JsonData()
fetchData = json.getData(URLweb)
qAvailability = json.getHasil

total_av = int(qAvailability['oee'][0]['total_av'])
pldt = int(qAvailability['oee'][0]['pldt'])
setup_loss = int(qAvailability['oee'][0]['setup_loss'])
set_adjustment = int(qAvailability['oee'][0]['set_adjustment'])
shutdown_loss = int(qAvailability['oee'][0]['shutdown_loss'])

main = Maintenance()

# void loop
while True:

    json.getDataLoop(URLloop)

    jamFailure = json.getJamFailure * 60
    menitFailure = json.getMenitFailure
    detikFailure = round(json.getDetikFailure / 60, 2)

    print("jamfailure {}".format(jamFailure))

    jamMinor = json.getJamMinor * 60
    menitMinor = json.getMenitMinor
    detikMinor = round(json.getDetikMinor / 60, 2)

    failure = jamFailure + menitFailure + detikFailure
    minorstop = jamMinor + menitMinor + detikMinor

    avail = main.availability(
        total_av, pldt, setup_loss, shutdown_loss, set_adjustment)

    freqFailure = json.getFrekuensiFailure
    freqMinor = json.getfrekuensiMinor
    print("frekuensi failure {}".format(freqFailure))
    print("frekuensi Minor {}".format(freqMinor))
    main.MTBF(failure, freqFailure, freqMinor)

    main.MTTR(URLpostMaintenance, minorstop, failure)

    print("program mtbfmttr3")
    time.sleep(22)
    # mainten.restValue()
    reset(0)
    # db.resetValue()  # !reset value jangan lupa harus dimasukin

    # db.postData("INSERT INTO `{}` (availability, performance, quality, oee, speed_loss, breakdown_loss, downtime_loss, defecttime_loss) VALUES ({}, {}, {}, {}, {}, {}, {}, {})".format(
    # konek, availability, performance, quality, nilaiOEE, speedLoss, breakdownLoss, downtimeLoss, defecttimeLoss))

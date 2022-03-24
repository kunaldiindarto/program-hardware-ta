import numpy as np
import time

from urllib import request
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json as jsonLib
import urllib.request

# inisialisasi


def resetTrue(reset):
    global sum_hours, sum_minutes, sum_seconds, minorstop
    global Fhours, Fminutes, Fseconds
    global failure, olMPhours, olMPminutes, olMPseconds, otherlossMP
    global olAnginhours, olAnginhours, olAnginminutes, olAnginseconds, otherlossAngin, otherloss
    global olAnginhours, olAnginhours, olAnginminutes, olAnginseconds, otherlossAngin, otherloss
    global olTotalhours, olTotalhours, olTotalminutes, olTotalseconds, otherlossTotal
    global Process, availability
    global performance, qual, quality
    global nilaiOEE, losses, speedLoss, breakdownLoss, downtimeLoss, defecttimeLoss, balancing
    global pLoss, losses2, dtLoss, balancingWahyu

    if reset == 0:
        print("pass resetTRue")
        sum_hours = 0.0
        sum_minutes = 0.0
        sum_seconds = 0.0
        minorstop = 0.0

        Fhours = 0
        Fminutes = 0
        Fseconds = 0
        failure = 0

        olMPhours = 0
        olMPminutes = 0
        olMPseconds = 0
        otherlossMP = 0

        olAnginhours = 0
        olAnginminutes = 0
        olAnginseconds = 0
        otherlossAngin = 0

        olTotalhours = 0
        olTotalminutes = 0
        olTotalseconds = 0
        otherlossTotal = 0
        otherloss = 0

        Process = 0
        availability = 0

        performance = 0
        qual = 0
        quality = 0

        nilaiOEE = 0
        losses = 0
        speedLoss = 0
        breakdownLoss = 0
        downtimeLoss = 0.0
        defecttimeLoss = 0

        balancing = 0

        pLoss = 0
        dtLoss = 0
        balancingWahyu = 0


class JsonData:

    def __init__(self):
        self.URLget = ""
        self.URLpost = ""
        self.URLloop = ""
        self.data = ""
        self.r = ""

        self.stat4 = ""
        self.pressure = 0.0

        self.jamMinor = 0
        self.menitMinor = 0
        self.detikMinor = 0

        self.jamFailure = 0
        self.menitFailure = 0
        self.detikFailure = 0

        # self.jamOlMP = 0
        # self.menitOlMP = 0
        # self.detikOlMP = 0

        # self.jamOlAngin = 0
        # self.menitOlAngin = 0
        # self.detikOlAngin = 0

        self.jamOlTotal = 0
        self.menitOlTotal = 0
        self.detikOlTotal = 0

        self.process = 0
        self.quality = 0
        self.pressure = 0.0

        self.requestpostOEE = ""
        self.statusBlink = ""

# *inisialisasi untuk getdataloop
        self.req = ""
        self.data2 = ""
        self.stat4 = ""

        self.URLOee = ""
        self.a = 0.0
        self.p = 0.0
        self.q = 0.0
        self.oee = 0.0
        self.speedLoss = 0.0
        self.breakdownLoss = 0.0
        self.dowtimeLoss = 0.0
        self.defectLoss = 0.0
        self.hasilPostOee = ""

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
        self.stat4 = str(self.data2['stat1'][0]['status'])
        self.process = int(self.data2['process']['process'])
        self.quality = int(self.data2['quality'][0]['defect'])

        print(self.quality)

        self.pressure = float(self.data2['pressure'][0]['bar'])

        print(self.stat4)
        self.statusBlink = str(self.data2['blink'][0]['status'])
        print("status blink sekarang adalah {}".format(self.statusBlink))

        self.jamMinor = int(self.data2['minorstop']['jam'])
        self.menitMinor = int(self.data2['minorstop']['menit'])
        self.detikMinor = int(self.data2['minorstop']['detik'])

        self.jamFailure = int(self.data2['failure']['jam'])
        self.menitFailure = int(self.data2['failure']['menit'])
        self.detikFailure = int(self.data2['failure']['detik'])

        # self.jamOlMP = int(self.data2['otherloss_mp']['jam'])
        # self.menitOlMP = int(self.data2['otherloss_mp']['menit'])
        # self.detikOlMP = int(self.data2['otherloss_mp']['detik'])

        # self.jamOlAngin = int(self.data2['otherloss_angin']['jam'])
        # self.menitOlAngin = int(self.data2['otherloss_angin']['menit'])
        # self.detikOlAngin = int(self.data2['otherloss_angin']['detik'])

        self.jamOlTotal = int(self.data2['otherloss_total']['jam'])
        self.menitOlTotal = int(self.data2['otherloss_total']['menit'])
        self.detikOlTotal = int(self.data2['otherloss_total']['detik'])

    def OEEposting(self, URLpostOEE, a, p, q, oee, speedLoss, breakdownLoss, downtimeLoss, defectLoss):
        self.URLOee = URLpostOEE
        self.a = a
        self.p = p
        self.q = q
        self.oee = oee
        self.speedLoss = speedLoss
        self.breakdownLoss = breakdownLoss
        self.downtimeLoss = downtimeLoss
        self.defectLoss = defectLoss

        self.postData = {'availability': self.a,
                         'performance': self.p,
                         'quality': self.q,
                         'oee': self.oee,
                         'breakdown_loss': self.breakdownLoss,
                         'downtime_loss': self.downtimeLoss,
                         'defecttime_loss': self.defectLoss,
                         'speed_loss': self.speedLoss,
                         }
        # self.requestpostOEE = requests.post(
        #     url=self.URLOee, data=self.postData)

        self.requestpostOEE = Request(
            self.URLOee, urlencode(self.postData).encode(), headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            })

        self.hasilPostOee = urlopen(self.requestpostOEE).read().decode()

        print("respon api input lifetime {}".format(
            self.hasilPostOee))

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
    def getprocess(self):
        pass

    @getprocess.getter
    def getprocess(self):
        return self.process

    @getprocess.setter
    def getprocess(self, resettt):
        self.process = resettt

    @property
    def getquality(self):
        pass

    @getquality.getter
    def getquality(self):
        return self.quality

    @getquality.setter
    def getquality(self, resettt):
        self.quality = resettt

    @property
    def getStatusBlink(self):
        pass

    @getStatusBlink.getter
    def getStatusBlink(self):
        return self.statusBlink

    @getStatusBlink.setter
    def getStatusBlink(self, resettt):
        self.statusBlink = resettt


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
# # ?------------------------------------
# # ?mulai otherloss MP

#     @property
#     def getJamOlMP(self):
#         pass

#     @getJamOlMP.getter
#     def getJamOlMP(self):
#         return self.jamOlMP

#     @getJamOlMP.setter
#     def getJamOlMP(self, resettt):
#         self.jamOlMP = resettt

#     @property
#     def getMenitOlMP(self):
#         pass

#     @getMenitOlMP.getter
#     def getMenitOlMP(self):
#         return self.menitOlMP

#     @getMenitOlMP.setter
#     def getMenitOlMP(self, resettt):
#         self.menitOlMP = resettt

#     @property
#     def getDetikOlMP(self):
#         pass

#     @getDetikOlMP.getter
#     def getDetikOlMP(self):
#         return self.detikOlMP

#     @getDetikOlMP.setter
#     def getDetikOlMP(self, resettt):
#         self.detikOlMP = resettt
# # ?------------------------------------
# # ?mulai otherloss tidak ada sumber angin

#     @property
#     def getJamOlAngin(self):
#         pass

#     @getJamOlAngin.getter
#     def getJamOlAngin(self):
#         return self.jamOlAngin

#     @getJamOlAngin.setter
#     def getJamOlAngin(self, resettt):
#         self.jamOlAngin = resettt

#     @property
#     def getMenitOlAngin(self):
#         pass

#     @getMenitOlAngin.getter
#     def getMenitOlAngin(self):
#         return self.menitOlAngin

#     @getMenitOlAngin.setter
#     def getMenitOlAngin(self, resettt):
#         self.menitOlAngin = resettt

#     @property
#     def getDetikOlAngin(self):
#         pass

#     @getDetikOlAngin.getter
#     def getDetikOlAngin(self):
#         return self.detikOlAngin

#     @getDetikOlAngin.setter
#     def getDetikOlAngin(self, resettt):
#         self.detikOlAngin = resettt
# # ?------------------------------------
# ?mulai otherloss total

    @property
    def getJamOlTotal(self):
        pass

    @getJamOlTotal.getter
    def getJamOlTotal(self):
        return self.jamOlTotal

    @getJamOlTotal.setter
    def getJamOlTotal(self, resettt):
        self.jamOlTotal = resettt

    @property
    def getMenitOlTotal(self):
        pass

    @getMenitOlTotal.getter
    def getMenitOlTotal(self):
        return self.menitOlTotal

    @getMenitOlTotal.setter
    def getMenitOlTotal(self, resettt):
        self.menitOlTotal = resettt

    @property
    def getDetikOlTotal(self):
        pass

    @getDetikOlTotal.getter
    def getDetikOlTotal(self):
        return self.detikOlTotal

    @getDetikOlTotal.setter
    def getDetikOlTotal(self, resettt):
        self.detikOlTotal = resettt
# ?------------------------------------


class Oee:

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
        self.failure = 0.0

        # inisialisasi performance
        self.teoriCT = 0
        self.__performanceLoss = 0.0
        self.netOT = 0
        self.P = 0.0

        self.minorStop = 0.0
        self.otherLoss = 0.0
        self.otherLoss2 = 0.0
        self.idealCT = 0
        self.process = 0

        # inisialisasi quality
        self.defectLoss = 0
        self.jmlProcess = 0
        self.goodProduct = 0
        self.netOT2 = 0.0
        self.vot = 0.0
        self.Q = 0.0

        # inisialisasi losses
        self.__speedLoss = 0.0
        self.__speedLoss2 = 0.0
        self.__breakdownLoss = 0.0
        self.__downtimeLoss = 0.0
        self.__defectTimeLoss = 0.0
        print("speed loss di dalam class yang udh di reset: {}".format(
            self.__speedLoss))

        #! inisialisasi untuk losses dari pak wahyu
        self.__perfLoss = 0.0
        self.__dtLoss = 0.0

    def availability(self, total_av, pldt, setup, shutdown, set_adjustment, failure, otherloss):

        self.total_av = total_av
        self.pldt = pldt
        self.setup = setup
        self.shutdown = shutdown
        self.set_adjustment = set_adjustment
        self.failure = failure
        self.otherLoss2 = float(otherloss)

        # self.loadingTime = self.total_av - self.pldt
        # print("loading time {}".format(self.loadingTime))
        # self.totalDT = self.setup + self.shutdown + self.set_adjustment + self.failure
        # print("total downtime adalah: {}".format(self.totalDT))
        # self.operatingTIme = self.loadingTime - self.totalDT

        self.loadingTime = self.total_av - self.pldt
        print("loading time {}".format(self.loadingTime))
        self.totalDT = self.setup + self.shutdown + \
            self.set_adjustment + self.failure + self.otherLoss2

        print("total downtime adalah: {}".format(self.totalDT))
        self.operatingTIme = self.loadingTime - self.totalDT

        self.A = round(((self.operatingTIme) / self.loadingTime * 100), 2)
        # print("nilai availability: {}".format(self.A))
        print("nilai operating time updated: {}".format(self.operatingTIme))
        print(self.operatingTIme)

    def performance(self, minor, other, idealCT, proses):

        self.minorStop = float(minor)
        self.otherLoss = float(other)
        self.idealCT = idealCT
        self.process = proses

        self.teoriCT = self.idealCT * self.operatingTIme
        self.__performanceLoss = self.minorStop + self.otherLoss
        print("performance loss: {}".format(self.__performanceLoss))
        print("minor loss: {}".format(self.minorStop))
        print("other loss: {}".format(self.otherLoss))
        self.netOT = round((self.process / self.idealCT), 2)

        print("net operating time: {}".format(self.netOT))

        self.P = round(((self.process / self.teoriCT) * 100), 2)
        print("nilai performance: {}".format(self.P))

    def quality(self, process, defect):
        self.jmlProcess = process
        self.defectLoss = defect
        self.netOT2 = self.netOT

        self.goodProduct = self.jmlProcess - self.defectLoss
        self.vot = self.goodProduct/self.jmlProcess * self.netOT2

        self.Q = round((self.vot/self.netOT2 * 100), 2)

        # print("defect loss {}".format(self.jmlProcess))
        print("nilai quality sebesar: {}".format(self.Q))

    def losses(self):
        self.__speedLoss = (self.operatingTIme - self.netOT -
                            self.__performanceLoss) / self.loadingTime * 100

        self.__speedLoss2 = self.operatingTIme - self.netOT - self.minorStop

        self.__breakdownLoss = (self.totalDT/self.loadingTime) * 100

        self.__downtimeLoss = (self.__performanceLoss/self.loadingTime) * 100

        self.__defectTimeLoss = (
            self.defectLoss/self.idealCT) / self.loadingTime * 100

    def losses2(self):
        self.__perfLoss = (self.minorStop + self. __speedLoss2) / \
            self.loadingTime * 100
        self.__dtLoss = (self.setup + self.shutdown + self.set_adjustment +
                         self.failure + self.otherLoss) / self.loadingTime * 100

    def resetVal(self):
        print("masuk ke method reset")
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
        self.failure = 0.0

        # inisialisasi performance
        self.teoriCT = 0
        self.__performanceLoss = 0.0
        self.netOT = 0
        self.P = 0.0

        self.minorStop = 0.0
        self.otherLoss = 0.0
        self.otherLoss2 = 0.0
        self.idealCT = 0
        self.process = 0

        # inisialisasi quality
        self.defectLoss = 0
        self.jmlProcess = 0
        self.goodProduct = 0
        self.netOT2 = 0.0
        self.vot = 0.0
        self.Q = 0.0
        print("masuk ke method reset {}".format(self.minorStop))

        # inisialisasi losses
        self.__speedLoss = 0.0
        self.__speedLoss2 = 0.0
        self.__breakdownLoss = 0.0
        self.__downtimeLoss = 0.0
        self.__defectTimeLoss = 0.0

        #! inisialisasi untuk losses dari pak wahyu
        self.__perfLoss = 0.0
        self.__dtLoss = 0.0

    @property
    def getAvailability(self):
        pass

    @getAvailability.getter
    def getAvailability(self):
        return self.A

    @getAvailability.setter
    def getAvailability(self, reset):
        self.A = reset
#

    @property
    def getPerformance(self):
        pass

    @getPerformance.getter
    def getPerformance(self):
        return self.P

    @getPerformance.setter
    def getPerformance(self, reset):
        self.P = reset
#

    @property
    def getQuality(self):
        pass

    @getQuality.getter
    def getQuality(self):
        return self.Q

    @getQuality.setter
    def getQuality(self, reset):
        self.Q = reset
#

    @property
    def getSpeedLoss(self):
        pass

    @getSpeedLoss.getter
    def getSpeedLoss(self):
        return self.__speedLoss

    @getSpeedLoss.setter
    def getSpeedLoss(self, reset):
        self.__speedLoss = reset
#

    @property
    def getBreakdownLoss(self):
        pass

    @getBreakdownLoss.getter
    def getBreakdownLoss(self):
        return self.__breakdownLoss

    @getBreakdownLoss.setter
    def getBreakdownLoss(self, reset):
        self.__breakdownLoss = reset
#

    @property
    def getDowntimeLoss(self):
        pass

    @getDowntimeLoss.getter
    def getDowntimeLoss(self):
        return self.__downtimeLoss

    @getDowntimeLoss.setter
    def getDowntimeLoss(self, reset):
        self.__downtimeLoss = reset
#

    @property
    def getDefectTimeLoss(self):
        pass

    @getDefectTimeLoss.getter
    def getDefectTimeLoss(self):
        return self.__defectTimeLoss

    @getDefectTimeLoss.setter
    def getDefectTimeLoss(self, reset):
        self.__defectTimeLoss = reset
#

    @property
    def getPerformanceLoss(self):
        pass

    @getPerformanceLoss.getter
    def getPerformanceLoss(self):
        return self.__performanceLoss

    @getPerformanceLoss.setter
    def getPerformanceLoss(self, reset):
        self.__performanceLoss = reset

# ? losses versi dua pak wahyu
    @property
    def getPerfLoss(self):
        pass

    @getPerfLoss.getter
    def getPerfLoss(self):
        return self.__perfLoss

    @getPerfLoss.setter
    def getPerfLoss(self, reset):
        self.__perfLoss = reset

    @property
    def getDTLoss(self):
        pass

    @getDTLoss.getter
    def getDTLoss(self):
        return self.__dtLoss

    @getDTLoss.setter
    def getDTLoss(self, reset):
        self.__dtLoss = reset


# void setup
URLweb = "http://polmanpms.online/client1"
URLloop = "http://polmanpms.online/client1/loop"
URLOee = "http://polmanpms.online/client1/postoee"

json = JsonData()

fetchData = json.getData(URLweb)
qAvailability = json.getHasil


total_av = int(qAvailability['oee'][0]['total_av'])
pldt = int(qAvailability['oee'][0]['pldt'])
setup_loss = int(qAvailability['oee'][0]['setup_loss'])
set_adjustment = int(qAvailability['oee'][0]['set_adjustment'])
shutdown_loss = int(qAvailability['oee'][0]['shutdown_loss'])


ideal_ct = int(qAvailability['performance'][0]['ideal_ct'])

print("Nilai total available: {}".format(total_av))
print("Nilai planned downtime: {}".format(pldt))
print("Nilai setup loss: {}".format(setup_loss))
print("Nilai setup adjustment: {}".format(set_adjustment))
print("Nilai shutdown loss: {}".format(shutdown_loss))

print("Nilai ideal cycle time: {}".format(ideal_ct))

# ----------
# buat di void loop
while True:
    fetchLoop = json.getDataLoop(URLloop)
    # time.sleep(1)
    status = json.getStatusBlink

    if status != "sd":
        defect = json.getquality
        print("quality adalah {}".format(defect))

        print("program hitung oee")
        # Minor stop
        sum_hours = json.getJamMinor * 60
        sum_minutes = json.getMenitMinor
        sum_seconds = round(json.getDetikMinor / 60, 2)

        minorstop = sum_hours + sum_minutes + sum_seconds

        print("jumlah total jam di konversi ke menit adalah: {}".format(sum_hours))
        print("jumlah total menit adalah: {}".format(sum_minutes))
        print("jumlah total detik di konversi menit adalah: {}".format(sum_seconds))
        print("minor stop adalah: {} menit".format(minorstop))

    # -----------------------------------------------------

        Fhours = json.getJamFailure * 60
        Fminutes = json.getMenitFailure
        Fseconds = round(json.getDetikFailure / 60, 2)

        failure = Fhours + Fminutes + Fseconds

        print("jumlah total jam di konversi ke menit adalah: {}".format(Fhours))
        print("jumlah total menit adalah: {}".format(Fminutes))
        print("jumlah total detik di konversi menit adalah: {}".format(Fseconds))
        print("failure adalah: {} menit".format(failure))

        # --------------
        # olMPhours = json.getJamOlMP * 60
        # olMPminutes = json.getMenitOlMP
        # olMPseconds = round(json.getDetikOlMP / 60, 2)

        # otherlossMP = olMPhours + olMPminutes + olMPseconds

        # print("jumlah total jam di konversi ke menit adalah: {}".format(olMPhours))
        # print("jumlah total menit adalah: {}".format(olMPminutes))
        # print("jumlah total detik di konversi menit adalah: {}".format(olMPseconds))
        # print("other loss adalah: {} menit".format(otherlossMP))

        # # --------------
        # olAnginhours = json.getJamOlAngin * 60
        # olAnginminutes = json.getMenitOlAngin

        # olAnginseconds = round(json.getDetikOlAngin / 60, 2)

        # otherlossAngin = olAnginhours + olAnginminutes + olAnginseconds
        olTotalhours = json.getJamOlTotal * 60
        olTotalminutes = json.getMenitOlTotal

        olTotalseconds = round(json.getDetikOlTotal / 60, 2)

        otherlossTotal = olTotalhours + olTotalminutes + olTotalseconds

        otherloss = otherlossTotal

        # print("jumlah total jam di konversi ke menit adalah: {}".format(olAnginhours))
        # print("jumlah total menit adalah: {}".format(olAnginminutes))
        # print("jumlah total detik di konversi menit adalah: {}".format(olAnginseconds))
        # print("other loss adalah: {} menit".format(otherlossAngin))
        print("total other loss adalah: {} menit".format(otherloss))
        print("------------------------------------------")
        # -------------
        Process = json.getprocess
        print("produk diproses sebesar: {} pcs".format(Process))

        # ngitung oee nih boss
        oee = Oee()  # !diluat aja, masukin ke setup

        avail = oee.availability(
            total_av, pldt, setup_loss, shutdown_loss, set_adjustment, failure, otherloss)

        availability = oee.getAvailability

        print("nilai availability di luar adalah: {}".format(availability))

        perf = oee.performance(minorstop, otherloss, ideal_ct, Process)
        performance = oee.getPerformance
        print("nilai performance di luar adalah: {}".format(performance))

        qual = oee.quality(Process, defect)
        quality = oee.getQuality
        print("nilai quality di luar adalah: {}".format(quality))

        nilaiOEE = availability * performance * quality / 10000
        losses = oee.losses()
    # !
    #     speedLoss = oee.getSpeedLoss
    #     breakdownLoss = oee.getBreakdownLoss
    #     downtimeLoss = oee.getDowntimeLoss
    # !----------------------------------
        defecttimeLoss = round(oee.getDefectTimeLoss, 2)

        nilaiOEE = round(nilaiOEE, 2)
    #     speedLoss = round(speedLoss, 2)
    #     breakdownLoss = round(breakdownLoss, 2)
    #     downtimeLoss = round(downtimeLoss, 2)
    #     defecttimeLoss = round(defecttimeLoss, 2)

    #     balancing = nilaiOEE + speedLoss + breakdownLoss + downtimeLoss + defecttimeLoss

    #     print("\n")
    #     print("OEE adalah: {}".format(nilaiOEE))
    #     print("speed loss adalah: {}".format(speedLoss))
    #     print("Breakdown loss adalah: {}".format(breakdownLoss))
    #     print("downtime loss adalah: {}".format(downtimeLoss))
    #     print("defect time loss adalah: {}".format(defecttimeLoss))
    #     print("balancing -> {}".format(balancing))

    #     print("Nilai defect loss: {}".format(defect))

        losses2 = oee.losses2()
        pLoss = oee.getPerfLoss
        pLoss = round(pLoss, 2)

        dtLoss = oee.getDTLoss
        dtLoss = round(dtLoss, 2)

        balancingWahyu = nilaiOEE + pLoss + dtLoss + defecttimeLoss
        print("nilai performance loss. P wahyu {}".format(pLoss))
        print("nilai downtime loss. P wahyu {}".format(dtLoss))
        print("nilai defect loss. P wahyu {}".format(defecttimeLoss))
        print("oee adalah {}".format(nilaiOEE))
        print("balancing wahyu adalah {}".format(balancingWahyu))

    #     # ! notes ini pakai yang pa wahyu teori nya ada di catetan, agar tidak merubah struktur database juga
    #     # *speed_loss = pLoss (performance loss), breakdown_loss = 0 (tidak digunakan), downtimeLoss = dtLoss (downtime loss pa wahyu)
        dummy = 0
        # json insert to database
        json.OEEposting(URLOee, availability, performance,
                        quality, nilaiOEE, pLoss, dummy, dtLoss, defecttimeLoss)

        # reset nilai untuk perhitungan selanjutnya
        oee.getSpeedLoss = 0.0
        oee.getBreakdownLoss = 0.0
        oee.getDowntimeLoss = 0.0
        oee.getDefectTimeLoss = 0.0
        oee.getPerformanceLoss = 0.0

        # perhitungan selesai reset semua nilai
        resetTrue(0)
        rest = oee.resetVal()
    else:
        print("tidak hitung oee karena sudah shutdown")
        # db.resetValue()
    print("program hitung oee1")
    time.sleep(17)

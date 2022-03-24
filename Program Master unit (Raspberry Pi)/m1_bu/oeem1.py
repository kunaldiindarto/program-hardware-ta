import time
import datetime
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

# *inisialisasi untuk post data breakdown
        self.postBreakdown = ""
        self.jamBreakdown = 0
        self.menitBreakdown = 0.0
        self.detikBreakdown = 0.0
        self.deskripsiBreakdown = ""
        self.hasilPostBreakdown = ""

# *inisialisasi untuk getdataloop
        self.req = ""
        self.data2 = ""
        self.stat4 = ""
        self.pressure = 0.0

# *inisialisasi untuk post Blink
        self.postStatusBlink = ""
        self.postDetailBlink = ""
        self.postBlinkk = ""
        self.URLpostBlink = ""
        self.hasilPostBlink = ""

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

    def getDataLoop(self, URLloop):
        self.URLloop = URLloop
        self.reque = urllib.request.Request(self.URLloop, data=None, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        })
        self.req = urllib.request.urlopen(self.reque)
        self.data2 = jsonLib.loads(self.req.read())
        # print("ini di dalam kelas json untuk ambil data {}".format(self.data2))
        print("ini di dalam kelas json untuk ambil data")
        self.stat4 = str(self.data2['stat1'][0]['status'])
        self.pressure = float(self.data2['pressure'][0]['bar'])

    def postAlarm(self, URL, status, detail):
        self.URLpostBlink = URL
        self.postStatusBlink = status
        self.postDetailBlink = detail

        self.postBlinkk = {'status': self.postStatusBlink,
                           'detail': self.postDetailBlink
                           }

        self.requestPostBlink = Request(
            self.URLpostBlink, urlencode(self.postBlinkk).encode(), headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            })

        self.hasilPostBlink = urlopen(self.requestPostBlink).read().decode()

        print("hasil post blink adalah {}".format(self.hasilPostBlink))

    def postBreakdown(self, URLbreakdown, jam, menit, detik, deskripsi):
        self.postBreakdown = URLbreakdown
        self.jamBreakdown = jam
        self.menitBreakdown = menit
        self.detikBreakdown = detik
        self.deskripsiBreakdown = deskripsi

        self.postData = {'jam': self.jamBreakdown,
                         'menit': self.menitBreakdown,
                         'detik': self.detikBreakdown,
                         'deskripsi': self.deskripsiBreakdown
                         }
        # self.requestPostBreakdown=requests.post(
        #     url=self.postBreakdown, data=self.postData)

        self.requestPostBreakdown = Request(
            self.postBreakdown, urlencode(self.postData).encode(), headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            })

        self.hasilPostBreakdown = urlopen(
            self.requestPostBreakdown).read().decode()

        print("respon api input breakdown {}".format(
            self.hasilPostBreakdown))

    @ property
    def getHasil(self):
        pass

    @ getHasil.getter
    def getHasil(self):
        return self.data

    @ getHasil.setter
    def reset6(self, resettt):
        self.data = resettt

    @ property
    def getStat4(self):
        pass

    @ getStat4.getter
    def getStat4(self):
        return self.stat4

    @ getStat4.setter
    def getStat4(self, resettt):
        self.stat4 = resettt

    @ property
    def getPressure(self):
        pass

    @ getPressure.getter
    def getPressure(self):
        return self.pressure

    @ getPressure.setter
    def getPressure(self, resettt):
        self.pressure = resettt


class Waktu(JsonData):

    def __init__(self):
        self.tombol = ""
        self.val = ""
        self.val2 = 0

        self.x = ""
        self.jam_start = 0
        self.menit_start = 0
        self.detik_start = 0

        self.y = ""
        self.jam_end = 0
        self.menit_end = 0
        self.detik_end = 0
        self.valuee = 0
        self.value2 = 0
        self.value3 = 0
        self.value4 = 0
        self.value5 = 0
        self.value6 = 0

        self.z = ""
        self.jam_startup = ""
        self.n = ""
        self.jam_rumus = 0
        self.menit_rumus = 0
        self.detik_rumus = 0

        self.n = ""
        self.jam_on = 0
        self.menit_on = 0
        self.detik_on = 0

        print(self.tombol)

        self.persiapan = 1

        self.total_av = 0
        self.pldt = 0
        self.alpha = ""
        self.jam_off = ""
        self.jam_shutdown = ""
        self.shutdown_loss = 0

        self.jam_starting = 0
        self.menit_starting = 0
        self.jam_shutting = 0
        self.menit_shutting = 0

        self.sensor = ""
        self.jam_sensor = 0
        self.menit_sensor = 0

        self.jam_in = 0
        self.menit_in = 0
        self.detik_in = 0.0
        # ? kondisi apakah trouble melebihi berhenti di shutdown
        self.kondisi = 0
        self.URLotherloss = ""
        self.URLotherloss2 = ""
        self.URLminor = ""
        self.URLfailure = ""

    def operatingTime(self, total_av, pldt, shutdown_loss):
        self.total_av = total_av  # 1 hari full dikonversi ke menit
        self.pldt = pldt
        self.shutdown_loss = shutdown_loss

        # jam awal
        self.waktu_tempuh = (self.total_av - self.pldt) / 60

        print("waktu tempuh antara total_av dan pldt: {}".format(self.waktu_tempuh))

        if __name__ == '__main__':
            # print("di dalam mehod saveTime -> {}".format(self.ngimput))
            self.alpha = datetime.datetime.now()
            print("now is (di dalam method operating Time): {}".format(self.alpha))

            # konversi jam ke int agar bisa dibandingkan ke waktu operasional mesin
            self.jam_starting = int(self.alpha.strftime("%H"))
            print("jam starting proses: {}".format(self.jam_starting))

            self.menit_starting = int(self.alpha.strftime("%M"))
            print("menit starting proses: {}".format(self.menit_starting))
            ##--------------------selesai---------------------------------###

            self.jam_off = self.alpha + timedelta(hours=self.waktu_tempuh)
            print("jam off proses produksi adalah: {}".format(self.jam_off))

            # konversi jam ke int agar bisa dibandingkan ke waktu operasional mesin
            self.jam_shutting = int(self.jam_off.strftime("%H"))
            print("jam shutting proses: {}".format(self.jam_shutting))

            self.menit_shutting = int(self.jam_off.strftime("%M"))
            print("menit shutting proses: {}".format(self.menit_shutting))
            ##--------------------selesai---------------------------------###

    def sensorJam(self):

        if __name__ == '__main__':
            self.sensor = datetime.datetime.now()
            # print("masuk ke method sensor {}".format(self.sensor))
            # konversi jam ke int agar bisa dibandingkan ke waktu operasional mesin
            self.jam_sensor = int(self.sensor.strftime("%H"))
            # print("jam starting proses: {}".format(self.jam_sensor))

            self.menit_sensor = int(self.sensor.strftime("%M"))
            # print("menit starting proses: {}".format(self.menit_sensor))
            ##--------------------selesai---------------------------------###

    def saveTime(self, ngimput, pressure, kondisi, URLotherloss2):
        # global value
        self.URLotherloss2 = URLotherloss2
        print("nilai value buat nahan awal {} ".format(self.valuee))
        self.ngimput = ngimput
        self.pressure = pressure
        self.kondisi = kondisi
        print("ini di dalam method savetTIme buat menampilkan pressure: {}".format(
            self.pressure))
        if __name__ == '__main__':
            if self.ngimput == 'off1' and self.valuee == 0 and self.pressure > 1.5:
                # print("di dalam mehod saveTime -> {}".format(self.ngimput))
                # self.x = str(datetime.datetime.now().time())
                self.x = datetime.datetime.now()
                print("now is: {}".format(self.x))

                # self.jam_start = self.x.strptime('%H:%M:%S')

                self.jam_start = int(self.x.strftime("%H"))
                print("jam mulai: {}".format(self.jam_start))

                self.menit_start = int(self.x.strftime("%M"))
                print("menit: {}".format(self.menit_start))
                self.detik_start = int(self.x.strftime("%S"))
                print("detik_start: {}".format(self.detik_start))

                # print("nilai value buat nahan {} ".format(self.value))
                self.valuee += 1
                print("nilai value buat nahan updated {} ".format(self.valuee))
                time.sleep(1)

            if self.ngimput == 'on1' and self.valuee != 0 and self.value2 == 0 and self.pressure > 1.5 or self.kondisi != 0:
                # print("di dalam mehod saveTime -> {}".format(self.ngimput))
                self.y = datetime.datetime.now()
                # float(self)
                self.jam_end = int(self.y.strftime("%H"))
                # self.jam_end = self.y.strftime("%H:%M:%S")
                # self.jam_end = datetime.strptime('%H:%M:%S')

                print("jam update: {}".format(self.jam_end))

                self.menit_end = int(self.y.strftime("%M"))
                print("menit update: {}".format(self.menit_end))

                self.detik_end = int(self.y.strftime("%S"))
                print("detik_update: {}".format(self.detik_end))
                self.value2 += 1
                time.sleep(1)
                a = self.y - timedelta(hours=self.jam_start,
                                       minutes=self.menit_start, seconds=self.detik_start)
                print("downtime other loss selama: {} ".format(a.time()))

                # untuk query insert ke database
                self.jam_in = int(a.strftime("%H"))
                self.menit_in = int(a.strftime("%M"))
                self.detik_in = float(a.strftime("%S"))

                print("untuk query -> jam {}, menit {}, detik{}".format(self.jam_in,
                      self.menit_in, self.detik_in))

                status = "tidak ada MP"
                super().__init__()
                super().postBreakdown(self.URLotherloss2, self.jam_in,
                                      self.menit_in, self.detik_in, status)

                # print(db.hasil)

    def otherloss2(self, ngimput, pressure, kondisi, URLotherloss):
        print("nilai value buat nahan awal {} ".format(self.valuee))
        self.ngimput = ngimput
        self.pressure = pressure
        self.kondisi = kondisi
        self.URLotherloss = URLotherloss
        print("ini di dalam method otherloss tidak ada sumber buat menampilkan pressure: {}".format(
            self.pressure))
        if __name__ == '__main__':
            if self.ngimput == 'off1' and self.value3 == 0 and self.pressure <= 1.5:
                # print("di dalam mehod saveTime -> {}".format(self.ngimput))
                # self.x = str(datetime.datetime.now().time())
                self.x = datetime.datetime.now()
                print("now is: {}".format(self.x))

                # self.jam_start = self.x.strptime('%H:%M:%S')

                self.jam_start = int(self.x.strftime("%H"))
                print("jam mulai: {}".format(self.jam_start))

                self.menit_start = int(self.x.strftime("%M"))
                print("menit: {}".format(self.menit_start))
                self.detik_start = int(self.x.strftime("%S"))
                print("detik_start: {}".format(self.detik_start))

                # print("nilai value buat nahan {} ".format(self.value))
                self.value3 += 1
                print("nilai value buat nahan updated {} ".format(self.valuee))
                time.sleep(1)

            if self.ngimput == 'off1' and self.value3 != 0 and self.value4 == 0 and self.pressure > 1.5 or kondisi != 0:
                # print("di dalam mehod saveTime -> {}".format(self.ngimput))
                self.y = datetime.datetime.now()
                # float(self)
                self.jam_end = int(self.y.strftime("%H"))
                # self.jam_end = self.y.strftime("%H:%M:%S")
                # self.jam_end = datetime.strptime('%H:%M:%S')

                print("jam update: {}".format(self.jam_end))

                self.menit_end = int(self.y.strftime("%M"))
                print("menit update: {}".format(self.menit_end))

                self.detik_end = int(self.y.strftime("%S"))
                print("detik_update: {}".format(self.detik_end))
                self.value4 += 1
                time.sleep(1)
                a = self.y - timedelta(hours=self.jam_start,
                                       minutes=self.menit_start, seconds=self.detik_start)
                print(
                    "downtime other loss tidak ada sumber angin selama: {} ".format(a.time()))

                # untuk query insert ke database
                self.jam_in = int(a.strftime("%H"))
                self.menit_in = int(a.strftime("%M"))
                self.detik_in = float(a.strftime("%S"))

                print("untuk query -> jam {}, menit {}, detik{}".format(self.jam_in,
                                                                        self.menit_in, self.detik_in))

                super().__init__()
                # db2 = Database('ok')
                status = "tidak ada sumber angin"
                super().postBreakdown(self.URLotherloss, self.jam_in,
                                      self.menit_in, self.detik_in, status)

                # print(db.hasil)

    def breakdown(self, ngimput, pressure, kondisi, URLmin, URlfail):
        # global value
        print("nilai value buat nahan awal {} ".format(self.valuee))
        self.ngimput = ngimput
        self.pressure = pressure
        self.kondisi = kondisi
        self.URLminor = URLmin
        self.URLfailure = URlfail
        print("ini di dalam method breakdown buat menampilkan pressure: {}".format(
            self.pressure))
        if __name__ == '__main__':
            if self.ngimput == 'on1' and self.value5 == 0 and self.pressure <= 1.5:
                # print("di dalam mehod saveTime -> {}".format(self.ngimput))
                # self.x = str(datetime.datetime.now().time())
                self.x = datetime.datetime.now()
                print("now is: {}".format(self.x))

                # self.jam_start = self.x.strptime('%H:%M:%S')

                self.jam_start = int(self.x.strftime("%H"))
                print("jam mulai: {}".format(self.jam_start))

                self.menit_start = int(self.x.strftime("%M"))
                print("menit: {}".format(self.menit_start))
                self.detik_start = int(self.x.strftime("%S"))
                print("detik_start: {}".format(self.detik_start))

                # print("nilai value buat nahan {} ".format(self.value))
                self.value5 += 1
                print("nilai value buat nahan updated {} ".format(self.valuee))
                time.sleep(1)

            if self.ngimput == 'on1' and self.value5 != 0 and self.value6 == 0 and self.pressure > 1.5 or self.kondisi != 0:
                # print("di dalam mehod saveTime -> {}".format(self.ngimput))
                self.y = datetime.datetime.now()
                # float(self)
                self.jam_end = int(self.y.strftime("%H"))
                # self.jam_end = self.y.strftime("%H:%M:%S")
                # self.jam_end = datetime.strptime('%H:%M:%S')

                print("jam update: {}".format(self.jam_end))

                self.menit_end = int(self.y.strftime("%M"))
                print("menit update: {}".format(self.menit_end))

                self.detik_end = int(self.y.strftime("%S"))
                print("detik_update: {}".format(self.detik_end))
                self.value6 += 1
                time.sleep(1)
                a = self.y - timedelta(hours=self.jam_start,
                                       minutes=self.menit_start, seconds=self.detik_start)
                print("downtime other loss selama: {} ".format(a.time()))

                # untuk query insert ke database
                self.jam_in = int(a.strftime("%H"))
                self.menit_in = int(a.strftime("%M"))
                self.detik_in = float(a.strftime("%S"))

                print("untuk query -> jam {}, menit {}, detik{}".format(self.jam_in,
                      self.menit_in, self.detik_in))

                if self.menit_in >= 2:

                    status = "Trouble mesin 4 besar"

                    super().__init__()
                    super().postBreakdown(self.URLfailure, self.jam_in,
                                          self.menit_in, self.detik_in, status)

                elif self.menit_in < 2:

                    status = "Trouble mesin 4 ringan"
                    super().__init__()
                    super().postBreakdown(self.URLminor, self.jam_in,
                                          self.menit_in, self.detik_in, status)

    def startup(self, setup, URL):
        self.setup = setup
        self.z = datetime.datetime.now()
        self.URLBlink = URL

        # based on rumus dari ->jam awal + setup loss
        self.jam_startup = self.z + timedelta(minutes=self.setup)

        self.jam_rumus = int(self.jam_startup.strftime("%H"))
        print("jam rumus mulai: {}".format(self.jam_rumus))

        self.menit_rumus = int(self.jam_startup.strftime("%M"))
        print("menit rumus mulai: {}".format(self.menit_rumus))

        self.detik_rumus = int(self.jam_startup.strftime("%S"))
        print("detik_start: {}".format(self.detik_rumus))

        print("self. z: {}".format(self.z))
        print("jam selesai startup: {}".format(self.jam_startup))
        print("ini udah masuk method startup | setup loss-> : {} menit".format(self.setup))
        delay = self.setup * 60  # konversi ke detik

        super().__init__()
        # inisialisasi alarm blink mesin
        blinkalarmStartup = "on"
        blinkalarmStartup2 = "off"
        detailStartup = "startup"
        doneStartup = "running"

        super().postAlarm(self.URLBlink, blinkalarmStartup, detailStartup)
        time.sleep(delay)
        super().postAlarm(self.URLBlink, blinkalarmStartup2, doneStartup)

        # dipakai based on delay time sleep
        self.n = datetime.datetime.now()

        self.jam_on = int(self.n.strftime("%H"))
        print("jam on: {}".format(self.jam_on))

        self.menit_on = int(self.n.strftime("%M"))
        print("menit on: {}".format(self.menit_on))

        self.detik_on = int(self.n.strftime("%S"))
        print("detik on: {}".format(self.detik_on))

        if self.jam_on == self.jam_rumus and self.menit_on == self.menit_rumus:
            print("jam running: {}".format(self.n))
            print(
                "setup loss ok selama {}, silahkan mesin langsung pake.".format(self.setup))
            self.persiapan += 1

    def shutdown(self):
        self.jam_shutdown = self.jam_off - \
            timedelta(minutes=self.shutdown_loss)
        print("masuk di method shutdown")
        print("jam dimulainya shutdown yaitu : {}".format(self.jam_shutdown))

    @ property
    def info(self):
        return self.persiapan

    @ property
    def reset1(self):
        pass

    @ reset1.getter
    def reset1(self):
        return self.valuee

    @ reset1.setter
    def reset1(self, resetter):
        self.valuee = resetter

    @ property
    def reset2(self):
        pass

    @ reset2.getter
    def reset2(self):
        return self.value2

    @ reset2.setter
    def reset2(self, reset):
        self.value2 = reset

    # -------
    @ property
    def reset3(self):
        pass

    @ reset3.getter
    def reset3(self):
        return self.value3

    @ reset3.setter
    def reset3(self, reseting):
        self.value3 = reseting

    @ property
    def reset4(self):
        pass

    @ reset4.getter
    def reset4(self):
        return self.value4

    @ reset4.setter
    def reset4(self, resetor):
        self.value4 = resetor

    # ----
    @ property
    def reset5(self):
        pass

    @ reset5.getter
    def reset5(self):
        return self.value5

    @ reset5.setter
    def reset5(self, resetr):
        self.value5 = resetr

    @ property
    def reset6(self):
        pass

    @ reset6.getter
    def reset6(self):
        return self.value6

    @ reset6.setter
    def reset6(self, resettt):
        self.value6 = resettt
# ------------------------------------------

    @ property
    def lengkapSensor(self):
        return self.sensor

    @ property
    def down(self):
        return self.jam_shutdown

    @ property
    def getWaktuOff(self):
        pass

    @ getWaktuOff.getter
    def getWaktuOff(self):
        return self.jam_off

    @ getWaktuOff.setter
    def getWaktuOff(self, reset):
        self.jam_off = reset


########----Program Utama----------########
# void Setup
# Ambil data di database
time.sleep(12)
URL = "http://polmanpms.online/client1"
URLloop = "http://polmanpms.online/client1/loop"

URLpostBlink = "http://polmanpms.online/client1/postblink"
URLpostOtherloss = "http://polmanpms.online/client1/postotherloss"
URLpostMinor = "http://polmanpms.online/client1/postminorstop"
URLpostFailure = "http://polmanpms.online/client1/postfailure"

json = JsonData()

json.getData(URL)
result = json.getHasil

setup_loss = int(result['oee'][0]['setup_loss'])
print("setup loss: {}".format(setup_loss))

shutdown_loss = int(result['oee'][0]['shutdown_loss'])
print("setup loss: {}".format(shutdown_loss))

total_av = int(result['oee'][0]['total_av'])
print("total availability: {}".format(total_av))

pldt = int(result['oee'][0]['pldt'])
print("setup loss: {}".format(pldt))


# inisialisasi menjalankan objek waktu
val = 0
zidane = Waktu()

# inisialisasi waktu untuk shutdown

zidane.operatingTime(total_av, pldt, shutdown_loss)
# inisialisasi untuk method menjalankan setup dan shutdown

print(zidane.info)
zidane.startup(setup_loss, URLpostBlink)
c = zidane.info  # waktu persiapan ok
print("nilai dimasukan di dalam C : {}".format(c))
zidane.shutdown()

# jamMulai = zidane.jamStarting
# menitMulai = zidane.menitStarting

sd = zidane.down  # jam shutdown
timeShutdown = sd.replace(second=0, microsecond=0)

timeOff = zidane.getWaktuOff.replace(second=0, microsecond=0)
print("sd adalah :{}".format(timeShutdown))
print("time off adalah {}".format(timeOff))
# jamFinish = zidane.jamShutting
# menitFinish = zidane.menitShutting

# inisialisasi untuk menghitung failure dkk
if c == 2:
    zidane = Waktu()
# #

# inisialisasi alarm blink mesin
blinkalarmMesin = ""
# insertAlarmTable = "blink_m4"
messageDone = "running"
messageOTAngin = "Otherloss tidak ada sumber"
messageOTMP = "Otherloss Tidak ada MP"
messageMinFal = "Mesin 1 Breakdown"
kondisi = 0

while True:
    print("program downtime")

    json.getDataLoop(URLloop)
    a = json.getStat4  # ? sakelar
    data = json.getPressure  # ? data pressure

    print("nilai pressure {}".format(data))
    print(a)

# nilai untuk reset dan nahan
    value = zidane.reset1
    value2 = zidane.reset2
    value3 = zidane.reset3
    value4 = zidane.reset4
    value5 = zidane.reset5
    value6 = zidane.reset6

    zidane.sensorJam()
    lengkapSensor = zidane.lengkapSensor.replace(second=0, microsecond=0)
    print("nilai sensor jam adalah : {}".format(lengkapSensor))

# # ini kondisi ketika startup loss sudah terpenuhi
    if lengkapSensor != timeShutdown and kondisi == 0:
        # ketika trouble, menjalankan fungsi berikutsatu paket dengan elif elif nya

        # ? ---- cek otherloss tidak ada sumber tekanan angin-----
        if a == 'off1' and value3 == 0 and value4 == 0 and data <= 1.5:
            # bikin fungsi baru copas aja dari savetime cuma namanya spesifik
            zidane.otherloss2(a, data, kondisi, URLpostOtherloss)
            blinkalarmMesin = "on"

            json.postAlarm(URLpostBlink, blinkalarmMesin, messageOTAngin)

        elif a == 'off1' and value3 == 1 and value4 == 0 and data > 1.5:  # repeat if
            print("ini perhitungan downtime otherloss tdak ada sumber sudah selesai")
            zidane.otherloss2(a, data, kondisi, URLpostOtherloss)
            blinkalarmMesin = "off"
            # !yang ditambahin setiap program
            if value == 1 and value2 == 0:
                json.postAlarm(URLpostBlink, blinkalarmMesin, messageOTMP)
            else:
                json.postAlarm(URLpostBlink, blinkalarmMesin, messageDone)
            # !--------------------------------

        elif a == 'off1' and value3 == 1 and value4 == 1 and data > 1.5:  # repeat if
            print("mesin sudah oke, reset nilai value dan value 2")
            zidane.reset3 = 0
            zidane.reset4 = 0
            blinkalarmMesin = ""
            print("nilai value reset 3 adalah : {}, \n\t nilai value reset 4 adalah : {}".format(
                zidane.reset3, zidane.reset4))
    # selesai counting trouble

        # ?---- cek otherloss tidak ada orang-----
        if a == 'off1' and value == 0 and value2 == 0 and data > 1.5:  # tambahin diantara jam proses
            zidane.saveTime(a, data, kondisi, URLpostOtherloss)
            print("ini perhitungan downtime awal")
            blinkalarmMesin = "on"
            json.postAlarm(URLpostBlink, blinkalarmMesin, messageOTMP)

        elif a == 'on1' and value == 1 and value2 == 0 and data > 1.5:  # repeat if
            print("ini perhitungan downtime sudah selesai")
            zidane.saveTime(a, data, kondisi, URLpostOtherloss)
            blinkalarmMesin = "off"
            # ?kondisi yang dua otherloss jalan berbarengan
            # if value3 == 1 and value4 == 0:
            #     db.postAlarm("INSERT INTO `{}` (status, detail) VALUES ('{}', '{}')".format(
            #         insertAlarmTable, blinkalarmMesin, messageOTAngin))
            # else:
            #     db.postAlarm("INSERT INTO `{}` (status, detail) VALUES ('{}', '{}')".format(
            #         insertAlarmTable, blinkalarmMesin, messageDone))

            json.postAlarm(URLpostBlink, blinkalarmMesin, messageDone)

        elif a == 'on1' and value == 1 and value2 == 1 and data > 1.5:  # repeat if
            print("mesin sudah oke, reset nilai value dan value 2")
            zidane.reset1 = 0
            zidane.reset2 = 0
            blinkalarmMesin = ""
            print("nilai value reset 1 adalah : {}, \n\t nilai value reset 2 adalah : {}".format(
                zidane.reset1, zidane.reset2))
    # selesai counting trouble
        elif a == 'on1' and value == 0 and value2 == 0 and data > 1.5:  # repeat if
            print("mesin sedang running, nilai value dan value 2 tetap di awal")

        # ? -------cek minor stop atau failure----------
        if a == 'on1' and value5 == 0 and value6 == 0 and data <= 1.5:  # tambahin diantara jam proses
            zidane.breakdown(a, data, kondisi, URLpostMinor, URLpostFailure)
            print("ini perhitungan downtime awal")

            # !query untuk insert blink alarm
            # *nyala blink kirim data on
            blinkalarmMesin = "on"
            json.postAlarm(URLpostBlink, blinkalarmMesin, messageMinFal)

        elif a == 'on1' and value5 == 1 and value6 == 0 and data > 1.5:  # repeat if
            print("ini perhitungan downtime sudah selesai")
            zidane.breakdown(a, data, kondisi, URLpostMinor, URLpostFailure)
            blinkalarmMesin = "off"
            json.postAlarm(URLpostBlink, blinkalarmMesin, messageDone)

        elif a == 'on1' and value5 == 1 and value6 == 1 and data > 1.5:  # repeat if
            print("mesin sudah oke, reset nilai value dan value 2")
            zidane.reset5 = 0
            zidane.reset6 = 0
            print("nilai value reset 5 adalah : {}, \n\t nilai value reset 6 adalah : {}".format(
                zidane.reset5, zidane.reset6))
            blinkalarmMesin = ""

        print("nilai value 1 adalah : {}".format(value))
        print("nilai value 2 adalah : {}".format(value2))
        print("nilai value 3 adalah : {}".format(value3))
        print("nilai value 4 adalah : {}".format(value4))
        print("nilai value 5 adalah : {}".format(value5))
        print("nilai value 6 adalah : {}".format(value6))
        time.sleep(0.05)
    # todo ini elif ketika waktu operating time habis
    elif lengkapSensor == timeShutdown and kondisi == 0:
        print("sekarang sudah diwaktu mesin shutdown ")

        kondisi += 1  # *kondisi satu menunjukan untuk shutdown

        # ? statement untuk mendata downtime sampai shudown loss
        # * otherloss tidak ada sumber angin
        if a == 'off1' and value3 == 1 and value4 == 0 and kondisi != 0:  # repeat if
            print("ini perhitungan downtime sudah selesai")
            zidane.otherloss2(a, data, kondisi, URLpostOtherloss)
            blinkalarmMesin = "olair"
            messageOlAngin = "waktu shutdown"
            json.postAlarm(URLpostBlink, blinkalarmMesin, messageOlAngin)

        value3 = zidane.reset3
        value4 = zidane.reset4

        if a == 'off1' and value3 == 1 and value4 == 1 and kondisi != 0:  # repeat if
            print("mesin sudah oke, reset nilai value dan value 2")
            zidane.reset3 = 0
            zidane.reset4 = 0
            value3 = 0
            value4 = 0
            blinkalarmMesin = ""
            print("nilai value reset 3 adalah : {}, \n\t nilai value reset 4 adalah : {}".format(
                zidane.reset3, zidane.reset4))
# ?----------------------------------------------------

        # * otherloss tidak ada orang
        if a == 'off1' and value == 1 and value2 == 0 and kondisi != 0:  # repeat if
            print("ini perhitungan downtime sudah selesai")
            zidane.saveTime(a, data, kondisi, URLpostOtherloss)
            blinkalarmMesin = "olmp"
            messageOlMp = "waktu shutdown"

            json.postAlarm(URLpostBlink, blinkalarmMesin, messageOlMp)

        value = zidane.reset1
        value2 = zidane.reset2

        if a == 'off1' and value == 1 and value2 == 1 and kondisi != 0:  # repeat if
            print("mesin sudah oke, reset nilai value dan value 2")
            zidane.reset1 = 0
            zidane.reset2 = 0
            value = 0
            value2 = 0
            blinkalarmMesin = ""
            print("nilai value reset 1 adalah : {}, \n\t nilai value reset 2 adalah : {}".format(
                zidane.reset1, zidane.reset2))

# ?-------------------------------------------------------------
        # *minorstop / failure loss
        if a == 'on1' and value5 == 1 and value6 == 0 and kondisi != 0:  # repeat if
            print("ini perhitungan downtime sudah selesai")
            zidane.breakdown(a, data, kondisi, URLpostMinor, URLpostFailure)
            blinkalarmMesin = "mf"
            messageMinFalsd = "waktu shutdown"
            json.postAlarm(URLpostBlink, blinkalarmMesin, messageMinFalsd)

        value5 = zidane.reset5
        value6 = zidane.reset6

        if a == 'on1' and value5 == 1 and value6 == 1 and kondisi != 0:  # repeat if
            print("mesin sudah oke, reset nilai value dan value 2")
            zidane.reset5 = 0
            zidane.reset6 = 0
            value5 = 0
            value6 = 0
            print("nilai value reset 5 adalah : {}, \n\t nilai value reset 6 adalah : {}".format(
                zidane.reset5, zidane.reset6))
            blinkalarmMesin = ""

        if value == 0 and value2 == 0 and value3 == 0 and value4 == 0 and value5 == 0 and value6 == 0:
            blinkalarmMesin = "sd"
            messageShutdown = "waktu shutdown "
            json.postAlarm(URLpostBlink, blinkalarmMesin, messageShutdown)
# ?-----------------selesai----------------------
        print(value)
        print(value2)
        print(value3)
        print(value4)
        print(value5)
        print(value6)

        time.sleep(shutdown_loss*60)

        if value == 0 and value2 == 0 and value3 == 0 and value4 == 0 and value5 == 0 and value6 == 0:
            blinkalarmMesin = "sd"
            messageShutdown = "mesin shutdown "
            json.postAlarm(URLpostBlink, blinkalarmMesin, messageShutdown)

    if lengkapSensor == timeOff and kondisi != 0:
        print("sekarang mesin off dan perhitungan untuk downtime tidak bisa")

    print("program oeem1")
    time.sleep(13)

# reset tombol nah ini mesinnya udah running jalan terus
# ketika mesin running jalan terus

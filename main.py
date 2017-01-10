inp_file = open("input.txt", "r")
out_file = open("output.txt", "w")
num_lines = sum(1 for line in open('input.txt'))  # dosyada kaç satır var


class Pilot:
    def __init__(self, fullname, lap_time_list=[], lap=16):
        """ Construction methodu. İçinde her pilotla ilgili bilgileri tutar"""
        self.fullname = fullname
        self.lap = lap
        self.lap_time_list = lap_time_list
        self.total_lap_time = 0
        self.average = 0
        self.finish_line = 0

    def total_lap_time_setter(self):
        """Pilotların datalarından toplam tur süresini milisaniye cinsinden hesaplar"""
        for k in self.lap_time_list:
            mt, sn_ms = k.split(":")
            sn, ms = sn_ms.split(".")
            total_lap_time = int(mt) * 60000 + int(sn) * 1000 + int(ms)
        self.total_lap_time = total_lap_time

    def average_lap_time_setter(self):
        """ Pilorların tur sürelerinin ortalamasınu bulur"""
        self.average = (self.total_lap_time/self.lap)

    def __str__(self):
        return "{} adli pilot bu yarista {} milisaniye sureyle {}.siradadir".format(self.fullname, self.total_lap_time, (siralanmis_pilotlar.index(self))+1 )

pilots = []
deneme_listesi = []
for i in range(num_lines):
    line = inp_file.readline().strip().split(",")
    pilots.append(Pilot(line[0], line[1:]))
    pilots[i].total_lap_time_setter()
    pilots[i].average_lap_time_setter()
    deneme_listesi.append(pilots[i].total_lap_time)

siralanmis = sorted(deneme_listesi)
siralanmis_pilotlar = []
for i in siralanmis:
    for k in range(num_lines):
        if i == pilots[k].total_lap_time:
            siralanmis_pilotlar.append(pilots[k])

for i in range(num_lines):
    out_file.write(str(siralanmis_pilotlar[i]))
    out_file.write("\n")
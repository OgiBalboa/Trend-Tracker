#--------------------------------------------
# Name:         Data Supervisor Settings
# Author :      ogulcan@AISIN
# Date :        13.12.2019
# Licence :     <GNU GCC>
#--------------------------------------------
import os
class settings():
    def __init__(self,): 
        self.first_peak_value = 10          # İLK PEAK İÇİN MİN DEĞER ( Default = 14 degrees)

        self.last_peak_value = 20           # SON PEAK İÇİN MİN DEĞER ( Default = 20 degrees)

        self.min_enj_time = 5               # ENJEKSİYON SÜRESİ ( Default = 5 sec)

        self.max_pressure = 20              # MAX BASINÇ ( Default = 20 MPa)

        self.wait_for_data = 1             #Verinin oluşması için bekleme süresi (Default = 38 sec)

        self.min_angle = 10                 # ( Default = 10 degrees)

        self.max_angle = 20                 # Doğrultalacak olan veri için aralık belirtilir. ( Default = 20)

        self.amp = 20                       # 3000 ve aşağı sayıdaki veriler için genlik değeri ( Default = 20)

#------------------------------EK AYARLAR--------------------------------------
        self.wait_for_next_peak = 1         # Peak bulduktan sonra bekleme süresi(default = 1)

        self.amp1 = 100                     # 3000 den fazla veri sayısı için genlik değeri ( Default = 100)

        self.jump = 20                      # düzensiz veriler için atlanacak süre miktarı
                                            #( Default = 20 *t. t, birim zamandır. veri sayısına göre değişir.)

        self.sample_range_start = 3        #Doğrultma için alınan örneğin başlama zamanı (30sn/veri sayısı)* range_start (Default :  1500 veri için 30. -0.06 . saniye-)

        self.sample_range_stop = 101        # Doğrultma bitiş zamanı ( Default : 1500 veri için 101 -2. saniye-)
        
        self.default_path = os.getcwd()     #Programın varsayılan çalışma dosyası.

        self.default_peak_count = 2         # Minimum peak sayısı

        self.process_time = 30              # Proses Süresi
#------------------------------PROGRAM İÇİ PARAMETRELER ( DOKUNMAYIN ! )--------------------------------------
        self.paralel_stop = None
#------------------------------PROGRAM DOSYA YOLLARINI TANITAN CLASS-------------------------------------
class program_files:
    def __init__(self,):
        self.main = os.getcwd()
        os.chdir("Datas")
        self.datas = os.getcwd()
        os.chdir("..")
        os.chdir("Errors")
        self.errors = os.getcwd()
        os.chdir("Auto")
        self.auto_errors = os.getcwd()
        os.chdir("..")
        os.chdir("Manual")
        self.manu_errors = os.getcwd()
        os.chdir(self.main)
        os.chdir("bin/Errors")
        self.perrors = os.getcwd()
        os.chdir(self.main)
            

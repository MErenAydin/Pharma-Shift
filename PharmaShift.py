import urllib.request
import datetime
import time
import sys
import os
import tkinter
from datetime import datetime
from urllib.request import urlopen

CURRENT_VERSION = "1.2"
LAST_UPDATE_TIME = "03.03.2020"

    # pharmacy on duty
url = 'https://www.istanbuleczaciodasi.org.tr/print/nobetciler_print.php?t=b&bid=28&d=0&z=17&map_show=1'

    # pharmacy on duty tomorrow
url2 = 'http://www.istanbuleczaciodasi.org.tr/print/nobetciler_print.php?t=b&bid=28&d=1&z=17&map_show=1'

application_path = os.path.join(os.environ["HOME"], "NöbetUygulaması")

AUTHOR_INFO = """
****NÖBETÇİ ECZANE UYGULAMASI****

    MUHAMMET EREN AYDIN
    Yazılım Tarihi: 30.9.2017
    Son Güncelleme Tarihi: {}
    Güncel Versiyon : {}""".format(LAST_UPDATE_TIME, CURRENT_VERSION)

    # Trying to enter google.com to check internet connection
	
def internet_accessible():
    try:
        urllib.request.urlopen("https://www.google.com", timeout=5)
        return True
    except urllib.error.URLError:
        return False

	# Logging Errors

def log(string):

    dateTimeObj = datetime.now()
    print(string)
	# Add Timestamp
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
	# Append String to File
    with open(os.path.join(application_path, "logs.txt"), "a") as file:
        file.write(timestampStr + " -> \t" + string + "\n")

	# Taking PDF from Internet
		
def takepdf(url):

    file_name = os.path.join(application_path, "nobetciler_print.pdf")
    try:
        urllib.request.urlretrieve(url, file_name)
    except urllib.error.URLError:
        log("PDF alınamadı")
        time.sleep(10)
        return False

    # Converting PDF Pages to Pictures

    with Image1(filename=os.path.join(application_path, "nobetciler_print.pdf[0]")) as img:
        img.save(filename=os.path.join(
            application_path, "tempFiles", "temp.jpg"))
    with Image1(filename=os.path.join(application_path, "nobetciler_print.pdf[1]")) as img:
        img.save(filename=os.path.join(
            application_path, "tempFiles", "temp1.jpg"))

    file = open(os.path.join(application_path, "dayofmonth.txt"), "w")
    file.write(str(datetime.datetime.now().day))
    file.close()
    return True
	
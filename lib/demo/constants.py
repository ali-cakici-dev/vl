# -*- coding: utf-8 -*-
import os



isInProcess = False
listen_vending_is_starting = True
listen_vending_is_busy = False
displayIsInProcess = False
displayWait = False
chooseIsInProcess = False
cardDetectedControl = False
serialReadInProcess = False
otherInProcess = False
ccrSerialReadInProcess = False
ccrOtherInProcess = False
indexKey = None  # Otomat Kind içerisindeki değer (row col farklılığı için)
firm = None
isHot = None
isCatchVendStarted = False
cvsPacket = None
kill_lvt = True
kill_main = False
automatMaxPrice = 0
user = None

dir_path = os.getcwd()


screenText = ""


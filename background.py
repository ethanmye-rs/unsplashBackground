import ctypes
import requests
import json
import os
import accessKey
import time

#Hey, it works!
#Currently, this script and accesskey.py live together, and make a folder in the user's documents for the backgrounds. The two are not neccessarilly in the same place. 
#Somehow, when using cx_freeze to build an exe, I'm missing the ctype DLL. So I just copied it over manually. Wtf, but it works now.

#add a scheduler -- could use win32com
    
#add run in the background
#add catagories
#add verficiation/check to make sure unsplash is up

#Pic Folder setup
username = os.getlogin()
documentsPath = os.path.join('C:\\Users', username, 'Documents')
picPath = os.path.isdir(os.path.join(documentsPath, 'unsplashBackground'))
if not picPath:
    os.chdir(documentsPath)
    os.mkdir("unsplashBackground")
    os.chdir(os.path.join(documentsPath, 'unsplashBackground'))
    
if picPath:
    os.chdir(os.path.join(documentsPath, 'unsplashBackground'))

def getPictureURL(orientation = 'landscape'):
    unsplashapi = "https://api.unsplash.com/photos/random"
    payload = {'orientation': orientation, 'client_id': accessKey.key}
    r = requests.get(url = unsplashapi, params=payload)
    return r

def dowloadPicture(r):
    img_data = requests.get(r.json()['urls']['raw']).content
    with open('backgroundimage.jpg', 'wb') as handler:
        handler.write(img_data)
    
dowloadPicture(getPictureURL()) #actually download the pic from given url

#make a desktop
SPI_SETDESKWALLPAPER = 0x14     #which command (20)
SPIF_UPDATEINIFILE   = 0x2 #forces instant update
src = os.path.join(documentsPath, 'unsplashBackground','backgroundimage.jpg')
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, src, SPIF_UPDATEINIFILE)

time.sleep(15)
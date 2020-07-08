import os
import sys
from time import sleep

a ='\033[92m'
b ='\033[91m'
c ='\033[0m'

def printx(x):
	col = {'m':31,'h':32,'k':33,'b':34,'p':35,'c':36,'p':37}
	for i in col:
		x=x.replace('\r%s'%i,'\033[%s;1m'%col[i])
	x+='\033[0m'
	x=x.replace('\r0','\033[0m')
	print(x)

os.system('clear')
printx('''\rm
   ______   ______________________ ____
    /  _ \  /____   //  ____//  / _/_/
   /  / \ \ ____/  //  /    /  /_/_/   ___
  /  /  / // __   //  /    /  _  /    /__/
 /  /__/ // /_/  //  /    /  / \ \\
/_______//______//__/    /__/   \_\\
    _____    ___________________ ____
    /  /     /  //  ___   //  / _/_/
   /  /     /  //  /  /  //  /_/_/
  /  /     /  //  /  /  //  _  /
 /  /____ /  //  /  /  //  / \ \\
/_______//__//__/  /__//__/   \_\\''')
sleep(2)
printx('\rp___________________________________________')
printx(' ')
printx('''\rp[+]\rh Like halaman facebook
\rp |_> \rh"\rmTermux Tutorial - DarkLink\rh"
\rp |_> \rm(https://facebook.com/105933597851208)''')
printx('\rp___________________________________________')

sleep(4.5)
os.system('xdg-open https://facebook.com/105933597851208')

printx ('\rh[*] Retrieve the default termux file')

try:
	os.mkdir('/data/data/com.termux/files/home/.termux')
except:
	pass

key = "extra-keys = [['ESC','TAB','UP','DOWN','HOME','BACKSPACE'],['CTRL','ALT','LEFT','RIGHT','END','DELETE'],['PGUP','PGDN','FN','/','D A R K -','- L I N K']]"
c = open('/data/data/com.termux/files/home/.termux/termux.properties','w') 
c.write(key)
c.close()
printx ('\rh[!] Please waitt...')

os.system('termux-reload-settings')
sleep(2.5)
printx ('\rh[*] Success ')
sleep(1)
printx ('\rh[*] Additional buttons have been added')














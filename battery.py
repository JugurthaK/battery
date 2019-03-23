import sys
import notify2
from time import sleep

def sendNotif(title, message):
    notify2.init('Test')
    notice = notify2.Notification(title, message)
    notice.show()
    return
def getBattery():
    f = open('/sys/class/power_supply/BAT0/capacity', 'r')
    content = int(f.read())
    f.close()
    return content

level = getBattery()
while 1 == 1:
    if level <= 20:
        sendNotif('Il faut te brancher', 'Tu as %d de batterie' % level)
    elif level >= 80 :
        sendNotif('Il faut te debrancher', ' ')
    sleep(300)
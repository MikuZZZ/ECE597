from subprocess import call
from Adafruit_I2C import Adafruit_I2C
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

#ALERT_1 = "P8_45"
ALERT_1 = "P9_41"
ALERT_2 = "P8_43"
ALERT_LED = "P9_12"
TMP_1 = Adafruit_I2C(0x48)
TMP_2 = Adafruit_I2C(0x4a)

TMP_1.write8(3, 0x1c)
TMP_1.write8(2, 0x1a)
TMP_1.write8(1, 0x04)

TMP_2.write8(3, 0x1c)
TMP_2.write8(2, 0x1a)
TMP_2.write8(1, 0x04)

GPIO.setup(ALERT_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ALERT_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ALERT_LED, GPIO.OUT)

GPIO.add_event_detect(ALERT_1, GPIO.BOTH)

while(True):
    print "TMP1: ", TMP_1.readU8(0)
    if GPIO.event_detected(ALERT_1):
        sleep(0.2)
        print "ALERT1 detected"


import Adafruit_BBIO.GPIO as GPIO
from time import sleep

BUTTON_1 = "P9_12"; BUTTON_2 = "P9_25"; BUTTON_3 = "P9_29"; BUTTON_4 = "P9_41"
LED_1 = "P9_13"; LED_2 = "P9_26"; LED_3 = "P9_30"; LED_4 = "P9_42"
ST_1 = 0; ST_2 = 0; ST_3 = 0; ST_4 = 0

GPIO.setup(BUTTON_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(LED_1, GPIO.OUT)
GPIO.setup(LED_2, GPIO.OUT)
GPIO.setup(LED_3, GPIO.OUT)
GPIO.setup(LED_4, GPIO.OUT)

GPIO.add_event_detect(BUTTON_1, GPIO.RISING)
GPIO.add_event_detect(BUTTON_2, GPIO.RISING)
GPIO.add_event_detect(BUTTON_3, GPIO.RISING)
GPIO.add_event_detect(BUTTON_4, GPIO.RISING)

while (True):
	if GPIO.event_detected(BUTTON_1):
		sleep(0.1)
		GPIO.output(LED_1, ST_1)
		ST_1 = not ST_1
	if GPIO.event_detected(BUTTON_2):
		sleep(0.1)
		GPIO.output(LED_2, ST_2)
		ST_2 = not ST_2
	if GPIO.event_detected(BUTTON_3):
		sleep(0.1)
		GPIO.output(LED_3, ST_3)
		ST_3 = not ST_3
	if GPIO.event_detected(BUTTON_4):
		sleep(0.1)
		GPIO.output(LED_4, ST_4)
		ST_4 = not ST_4


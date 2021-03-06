import Adafruit_BBIO.GPIO as GPIO
from time import sleep

BUTTON_1 = "P9_12"
BUTTON_2 = "P9_25"
BUTTON_3 = "P9_29"
BUTTON_4 = "P9_41"

LED_1 = "P9_14"
LED_2 = "P9_26"
LED_3 = "P9_30"
LED_4 = "P9_42"

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

size = 8
currentX = 0
currentY = 0
board = [[0 for col in range(size)] for row in range(size)]
board[currentX][currentY] = 1

def printBoard():
	for i in range(0, size):
		for j in  range(0, size):
			print board[i][j],
		print
	print

printBoard()
while (True):
	if GPIO.event_detected(BUTTON_1):
		if currentX != 0:
			GPIO.output(LED_1, not GPIO.input(LED_1))
			currentX = currentX - 1
			board[currentX][currentY] = 1
			board[currentX][currentY] = 1
			board[currentX][currentY] = 1
			printBoard()
			sleep(0.2)
	if GPIO.event_detected(BUTTON_2):
		if currentX != size - 1:
			GPIO.output(LED_2, not GPIO.input(LED_2))
			currentX = currentX + 1
			board[currentX][currentY] = 1
			printBoard()
			sleep(0.2)
	if GPIO.event_detected(BUTTON_3):
		if currentY != 0:
			GPIO.output(LED_3, not GPIO.input(LED_3))
			currentY = currentY - 1
			board[currentX][currentY] = 1
			printBoard()
			sleep(0.2)
	if GPIO.event_detected(BUTTON_4):
		if currentY != size - 1:
			GPIO.output(LED_4, not GPIO.input(LED_4))
			currentY = currentY + 1
			board[currentX][currentY] = 1
			printBoard()
			sleep(0.2)


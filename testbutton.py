import RPi.GPIO as GPIO
import time
import websocket

MOTOR_PIN = 19
BUTTON_PIN = 21

socket = websocket.WebSocket()
socket.connect("localhost:3000")

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)

while True:
    button = GPIO.input(BUTTON_PIN)
    if button == True:
        GPIO.output(MOTOR_PIN, GPIO.HIGH)
        print("mo cua")
        message = "mo cua"
        socket.send(str(message))
        time.sleep = 1
    if button == False:
        GPIO.output(MOTOR_PIN, GPIO.LOW)
        print ("dong cua")
        message = "dong cua"
        socket.send(str(message))
        time.sleep = 1
    if KeyboardInterrupt:
        GPIO.cleanup
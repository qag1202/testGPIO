import RPi.GPIO as GPIO
import time
import websocket

MQ_PIN = 19

socket = websocket.WebSocket()
socket.connect("loaclhost:3000")

GPIO.setmode(GPIO.BCM)
GPIO.setup(MQ_PIN, GPIO.IN)

def read():
    try:
        while True:
            alcohol = GPIO.input(MQ_PIN)
            print("nong do con",alcohol)
            message="nong do con", alcohol
            socket.send (str(message))
            time.sleep = 1
    except KeyboardInterrupt:
        GPIO.cleanup
if __name__ == "__main__":
    read



import serial
import time

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)  # let the Arduino finish resetting after the port opens

alarm_on = False

def start_alarm():
    global alarm_on
    if not alarm_on:
        arduino.write(b'1')
        alarm_on = True
        print("Alarm started")

def stop_alarm():
    global alarm_on
    if alarm_on:
        arduino.write(b'0')
        alarm_on = False
        print("Alarm stopped")

def close():
    arduino.close()

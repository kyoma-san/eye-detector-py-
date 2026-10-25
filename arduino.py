import serial
import asyncio
import threading
import serial.tools.list_ports
import time

arduino = serial.Serial('/dev/ttyACM0',9600)
alarm_states = ("STARTED", "STARTING", "STOPPED", "STOPPING")
current_state = alarm_states[2]

def start():
    global current_state
    print("Current state: ", current_state)
    current_state = alarm_states[1]
    open_stream()
    if arduino.is_open:
        arduino.write(("1" + '\n').encode())
        arduino.flush()
        time.sleep(2)
        close_stream()
    print("Alarm started")
    current_state = alarm_states[0]

def stop():
    global current_state
    print("Current state: ", current_state)
    current_state = alarm_states[3]
    open_stream()
    print("Stopping alarm")
    if arduino.is_open:
        arduino.write(("0" + '\n').encode())
        arduino.flush()
        time.sleep(2)
        close_stream()
    print("Alarm stopped")
    current_state = alarm_states[2]

def open_stream():
    try:
        arduino.open()
    except:
        print("Port already open!")
def close_stream():
    try:
        arduino.close()
    except:
        print("Port is already closed!")

def start_alarm():
    if current_state == alarm_states[2]:
        print("Starting the alarm")
        threading.Thread(target=start).start()
def stop_alarm():
    if current_state == alarm_states[0]:
        print("Stopping the alarm")
        threading.Thread(target=stop).start()


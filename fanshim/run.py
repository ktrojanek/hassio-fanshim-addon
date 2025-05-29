import time
from fanshim import FanShim
import psutil

fan = FanShim()
fan.set_led(0, 255, 0)

THRESHOLD = 60
HYSTERESIS = 5

def get_cpu_temp():
    with open("/sys/class/thermal/thermal_zone0/temp") as f:
        return int(f.read()) / 1000

fan_on = False

while True:
    temp = get_cpu_temp()
    print(f"CPU Temp: {temp}°C")

    if not fan_on and temp > THRESHOLD:
        fan.set_fan(True)
        fan_on = True
        fan.set_led(255, 0, 0)
    elif fan_on and temp < (THRESHOLD - HYSTERESIS):
        fan.set_fan(False)
        fan_on = False
        fan.set_led(0, 255, 0)

    time.sleep(10)

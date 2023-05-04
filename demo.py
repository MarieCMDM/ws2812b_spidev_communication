import spi_led as led
import time

def blink():
    print("Starting demo... show grbw")
    print("red")
    led.showColor([255, 0, 0])
    time.sleep(2)

    print("green")
    led.showColor([0, 255, 0])
    time.sleep(2)

    print("blue")
    led.showColor([0, 0, 255])
    time.sleep(2)

    print("white")
    led.showColor([255, 255, 255])
    time.sleep(2)

    print("off")
    led.showColor([0, 0, 0])
    print("Exiting demo...")

def fade():
    r = 255
    g = 0
    b = 0
    speed = 0.3

    while True:
        while (r > 0):
            led.showColor([r, g, b])
            r -= 5
            g += 5
            time.sleep(speed)

        while (g > 0):
            led.showColor([r, g, b])
            g -= 5
            b += 5
            time.sleep(speed)

        while (b > 0):
            led.showColor([r, g, b])
            b -= 5
            r += 5
            time.sleep(speed)

if __name__ == '__main__':
    
    try:
        #blink()
        fade()
    except KeyboardInterrupt:
        led.showColor([0, 0, 0])

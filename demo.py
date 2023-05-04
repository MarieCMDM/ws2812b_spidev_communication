import spi_led as led
import time

def demo():
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

if __name__ == '__main__':
    demo()

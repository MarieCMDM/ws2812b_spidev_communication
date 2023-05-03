import spidev
import time

NUM_OF_LEDS = 1
OFF_SIGNAL = [0b1000] * 24

spi = spidev.SpiDev()
spi.open(0, 0)

spi.max_speed_hz = 8000000
spi.mode = 0b00

def color_parsing(grb):
    g, r, b = grb 

    # Create byte array with color data
    color_data = []
    for i in range(8):
        if (g >> (7-i)) & 0b1:
            color_data.append(0b1110)
        else:
            color_data.append(0b1000)
    for i in range(8):
        if (r >> (7-i)) & 0b1:
            color_data.append(0b1110)
        else:
            color_data.append(0b100)
    for i in range(8):
        if (b >> (7-i)) & 0b1:
            color_data.append(0b1110)
        else:
            color_data.append(0b1000)

    return color_data

def demo():
    print("Starting demo... show grbw")
    print("green")
    color_data = color_parsing([255, 0, 0]) * NUM_OF_LEDS
    spi.xfer(color_data)
    time.sleep(1)

    print("red")
    color_data = color_parsing([0, 255, 0]) * NUM_OF_LEDS
    spi.xfer(color_data)
    time.sleep(1)

    print("blue")
    color_data = color_parsing([0, 0, 255]) * NUM_OF_LEDS
    spi.xfer(color_data)
    time.sleep(1)

    print("white")
    color_data = color_parsing([255, 255, 255]) * NUM_OF_LEDS
    spi.xfer(color_data)
    time.sleep(1)

    print("off")
    off_data = OFF_SIGNAL * NUM_OF_LEDS
    spi.xfer(off_data)
    print("Exiting demo...")

if __name__ == '__main__':
    demo()
    spi.close()

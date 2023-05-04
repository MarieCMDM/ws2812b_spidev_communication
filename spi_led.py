import spidev
import sys

# NUM_OF_LEDS = 1

rgb =[]
if(len(sys.argv) == 4):
    for i in sys.argv[1:]:
        rgb.append(int(i))
else:
    rgb=[0,0,0]

spi = spidev.SpiDev()
spi.open(0, 0)

spi.max_speed_hz = 8000000
spi.mode = 0b00

def color_parsing(rgb):
    r, g, b = rgb 
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

def showColor(rgb):
    color_data = color_parsing(rgb) # * NUM_OF_LEDS # enable if using more leds
    spi.xfer(color_data)

if __name__ == '__main__':
    showColor(rgb)
    spi.close()

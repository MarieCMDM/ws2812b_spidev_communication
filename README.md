# ws2812b_spidev_communication
example code to send messages to a ws2812b addressable led using spi port.  
  
tested on NanoPi with Armbian bullseye.  
if the sample is not working try to channge the ```spi.max_speed_hz \ message [{ speedHz: }]``` to match the one required by your led strip (only need to try untill find the right one)

## requirements:
Enable spi port editing ```/boot/armbianEnv.txt``` need to add the following lines 
```
overlays=spi-spidev
param_spidev_spi_bus=0
```

### Python
https://pypi.org/project/spidev/
```
sudo pip3 install spidev
```
### NodeJs
https://www.npmjs.com/package/spi-device
```
npm install spi-device
```


// On Test, only make the led green

const spi = require('spi-device');
const upvalue = 0b1110//0b11111100;
const downvalue = 0b1000//0b10000000;

// The MCP3008 is on bus 0 and it's device 0
const spiPort = spi.open(0, 0, err => {
  // An SPI message is an array of one or more read+write transfers
  const message = [{
    sendBuffer: Buffer.from([upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue]),
    byteLength: 4,
    speedHz: 8000000 
  }];

  if (err) throw err;

  spiPort.transfer(message, (err, message) => {
    if (err) throw err;

    console.log("fatto");
  });
});

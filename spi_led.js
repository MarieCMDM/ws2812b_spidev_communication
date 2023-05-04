// On Test, only make the led green

const spi = require('spi-device');
const upvalue = 0b1110;
const downvalue = 0b1000;

//rgb = [255, 255, 255]

const spiPort = spi.open(0, 0, err => {
  // An SPI message is an array of one or more read+write transfers
  const message = [{
    sendBuffer: Buffer.from([downvalue, downvalue, downvalue, downvalue, downvalue, downvalue, downvalue, downvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue, upvalue]),
    byteLength: 24,
    speedHz: 8000000 
  }];

  spiPort.transfer(message, (err, message) => {
    if (err) throw err;

    console.log("fatto");
  });
});


/*
function messageParser(rgb) {
  // def color_parsing(rgb):
  r = rgb[0]; 
  g = rgb[1];
  b = rgb[2];
  // r, g, b = rgb

  //Create byte array with color data
  color_data = []
  // color_data = []
  for(int i=0, i<8, i++){
    if ( (g >> (7-i)) & 0b1 ){
      color_data.append(0b1110)
    }else{
      color_data.append(0b1000)
    }
  }
  for(int i=0, i<8, i++){
    if ( (r >> (7-i)) & 0b1 ){
      color_data.append(0b1110)
    }else{
      color_data.append(0b1000)
    }
  }
  for(int i=0, i<8, i++){
    if ( (b >> (7-i)) & 0b1 ){
      color_data.append(0b1110)
    }else{
      color_data.append(0b1000)
    }
  }

  // return color_data

  console.log("alc");
};
*/

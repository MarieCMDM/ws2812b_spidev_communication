const spi = require('spi-device');
const LED_NUM = 1;

const args = process.argv;
if (args.length == 5){
  rgb = [args[2], args[3], args[4]]
}else{
  rgb = [0, 0, 0]
}
const spiPort = spi.open(0, 0, err => {
  // An SPI message is an array of one or more read+write transfers
  const message = [{
    sendBuffer: Buffer.from(messageParser(rgb)),
    byteLength: 24 * LED_NUM,
    speedHz: 8000000 
  }];

  spiPort.transfer(message, (err, message) => {
    if (err) throw err;
  });
});

function messageParser(rgb) {
  message = []
  basemessage=colorParser(rgb);
  i=1;
  while (i<=LED_NUM){
    message = message.concat(basemessage);
    i++;
  }
  return message;
};

function colorParser(rgb){
  r = rgb[0]; 
  g = rgb[1];
  b = rgb[2];
  //Create byte array with color data
  color_data = []
  for(let i=0; i<8; i++){
      if ( (g >> (7-i)) & 0b1 ){
      color_data.push(0b1110);
      }else{
      color_data.push(0b1000);
      }
  }
  for(let i=0; i<8; i++){
      if ( (r >> (7-i)) & 0b1 ){
      color_data.push(0b1110);
      }else{
      color_data.push(0b1000);
      }
  }
  for(let i=0; i<8; i++){
      if ( (b >> (7-i)) & 0b1 ){
      color_data.push(0b1110);
      }else{
      color_data.push(0b1000);
      }
  }
  return color_data;
};


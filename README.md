# nixie-weather
This project seeks to upgrade my original internet enabled nixie weather clock with a raspberry Pi. I already have the internet, nixies, and time code working. I need to interface with the lcd screen via serial commands and read analog data from potentiometer knobs transfered over the i2c interface via an adafruit trinket.

This code the following libraries

REQUESTS

git clone git://github.com/kennethreitz/requests.git
cd requests
python setup.py install


SPI

sudo apt-get install python-dev
mkdir python-spi
cd python-spi
wget https://raw.github.com/doceme/py-spidev/master/setup.py
wget https://raw.github.com/doceme/py-spidev/master/spidev_module.c
sudo python setup.py install

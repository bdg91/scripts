## Raspberry Pi

### DHT22 Humidity Sensor
Reads the humidity and temperature from a DHT22 sensor every 30 seconds and sends the results to InfluxDB.

#### Prerequisites
- Python 3.7 installed
- `sudo pip3.7 install Adafruit_DHT`
- `sudo pip3.7 install schedule`
- `sudo pip3.7 install influxdb_client`

### Run Python scripts in background
-  `sudo apt-get install screen`
- `screen python3.7 <YOUR_SCRIPT.py> &`

### Install Python 3.7
`sudo apt-get update -y && sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev -y && wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz && tar xf Python-3.7.0.tar.xz && cd Python-3.7.0 && ./configure && make -j 4 && sudo make altinstall && cd .. && sudo rm -r Python-3.7.0 && rm Python-3.7.0.tar.xz && sudo apt-get --purge remove build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev -y && sudo apt-get autoremove -y && sudo apt-get clean`

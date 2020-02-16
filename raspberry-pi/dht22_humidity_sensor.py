import schedule
import time
import Adafruit_DHT
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

ORGANIZATION = '<ORGANIZATION>'
BUCKET = 'raspberry_pi_bucket'

CLIENT = InfluxDBClient(url="<INFLUX_URL>",
                        token="<INFLUX_TOKEN>")
WRITE_API = CLIENT.write_api(write_options=SYNCHRONOUS)


# Read measurement from DHT22 and write results to Influx DB.
def write_data_to_influx():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        p = Point("DHT22").tag("location", "Huiskamer")\
            .field("temperature", round(temperature, 1))\
            .field("humidity", round(humidity, 1))
        WRITE_API.write(bucket=BUCKET, org=ORGANIZATION, record=p)
    else:
        print("Failed to retrieve data from DHT22 sensor")


if __name__ == '__main__':
    schedule.every(30).seconds.do(write_data_to_influx)
    while True:
        schedule.run_pending()
        time.sleep(1)

# ESP32AsyncioReading2Sensor
Reading double sensor values (DHT22 and HC-SR04) at the same time with ESP32 using the MicroPython-uasyncio

# Specifications

The following table shows the key features and specifications of the HC-SR04 ultrasonic sensor. For a more in-depth analysis of these sensors, please check the sensors’ datasheet.

| Parameter            | Description                                  |
|----------------------|----------------------------------------------|
| Power Supply         | 5V DC                                        |
| Working Current      | 15 mA                                        |
| Working Frequency    | 40 kHz                                       |
| Maximum Range        | 4 meters                                     |
| Minimum Range        | 2 cm                                         |
| Measuring Angle      | 15º                                          |
| Resolution           | 0.3 cm                                       |
| Trigger Input Signal | 10 uS TTL pulse                              |
| Echo Output Signal   | TTL pulse proportional to the distance range |
| Dimensions           | 45mm x 20mm x 15mm                           |

Ref: [HC-SR04 Ultrasonic Sensor Datasheet 📑](https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf)

The following table shows the important specifications of the DHT22 temperature and humidity sensors. For a more in-depth analysis of these sensors, please check the sensors’ datasheet.

| Parameter                 | Description                                              |     
|---------------------------|----------------------------------------------------------|
| Model                     | DHT22                                                    |
| Power Supply              | 3.3-6V DC                                                |
| Output Signal             | Digital signal via Single-bus                            |
| Sensing Element           | Polymer Capacitor                                        |
| Operating Range           | Humidity 0-100 %RH <br> Temperature -40~80 °C            |
| Accuracy                  | Humidity ±2 %RH (Max ±5 %RH) <br> Temperature <±0.5 °C   |
| Resolution or Sensitivity | Humidity 0.1 %RH <br> Temperature 0.1 °C                 |
| Repeatability             | Humidity ±1 %RH <br> Temperature ±0.2 °C                 |
| Humidity Hysteresis       | ±0.5 %RH/year                                            |
| Long-term Stability       | ±0.5 %RH/year                                            |
| Sensing Period            | 2 s                                                      |
| Interchangeability        | Fully Interchangeable                                    |
| Dimensions                | 14mm x 18mm x 5.5mm                                      |

Ref: [DHT22 Temperature and Humidity Sensors Datasheet 📑](https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf)
# Usage


| HC-SR04 | ESP32   |
|---------|---------|
| VCC     | VIN     |
| Trig    | GPIO 5  |
| Echo    | GPIO 18 |
| GND     | GND     |

First, you need to import the HCSR04 class from the hcsr04 library. Additionally, you also need to import the time library to add delays to our code.
```python
from hcsr04 import HCSR04
from time import sleep
```
Then, create an HCSR04 object called sensor that refers to the HCSR04 sensor. Pass as arguments the trigger pin, the echo pin, and the timeout (maximum travel time of the sound wave, when the sensor is probably out of range).
```python
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
```
To get the distance in cm, you just need to call the distance_cm method on the sensor object. Save the result in the distance variable.
```python
distance = sensor.distance_cm()
```
The library also provides a method to get the distance in millimeters without floating point. You just need to call.
```python
distance = sensor.distance_mm()
```
Print the distance on the Micropython shell.
```python
print("Distance:", distance, "cm")
```
In the end, you need to add a delay of one second (the distance is updated every second).
```python
sleep(1)
```
Ref: [How the Code Works (HC-SR04)](https://randomnerdtutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266)

| DHT22 | ESP32 |
|-------|-------|
| VCC   | 3.3 V |
| GPIO  | 14    |
| GND   | GND   |

Before requesting temperature and humidity, you need to use the measure() method on the sensor object.
```python
sensor.measure()
```
Then, read the temperature with sensor.temperature() and the humidity with sensor.humidity(). Save those readings on the temp and hum variables.
```python
temp = sensor.temperature()
```
The following command converts the temperature to Fahrenheit degrees.
```python
temp_f = temp * (9/5) + 32.0
```
Finally, print all the readings on the MicroPython shell using the print() function.
```python
print("Temperature: %3.1f C" %temp)
print("Temperature: %3.1f F" %temp_f)
print("Humidity: %3.1f %%" %hum)
```
Ref: [How the Code Works (DHT22)](https://randomnerdtutorials.com/esp32-esp8266-dht11-dht22-micropython-temperature-humidity-sensor)

## Results in 10 seconds
```
Temperature: 26.2 C
Temperature: 79.2 F:
Humidity: 56.3 %

Distance: 11.40893 cm

Temperature: 26.2 C
Temperature: 79.2 F:
Humidity: 56.6 %

Distance: 16.70103 cm

Temperature: 26.3 C
Temperature: 79.3 F:
Humidity: 56.8 %

Distance: 8.625429 cm

Temperature: 26.3 C
Temperature: 79.3 F:
Humidity: 59.0 %

Distance: 9.19244 cm

Temperature: 26.4 C
Temperature: 79.5 F:
Humidity: 62.0 %

Distance: 6.941581 cm

Temperature: 26.4 C
Temperature: 79.5 F:
Humidity: 65.6 %

Distance: 8.230241 cm

Temperature: 26.5 C
Temperature: 79.7 F:
Humidity: 69.4 %

Distance: 24.00344 cm

Temperature: 26.6 C
Temperature: 79.9 F:
Humidity: 73.0 %

Distance: 21.11684 cm

Executed in 10.00 seconds.
```

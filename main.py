from machine import Pin 
from machine import Pin, I2C
import machine
import ssd1306 
import dht
import time

DHT_PIN = 4  # DHT22 data pin

# Initialize DHT22 sensor
dht_sensor = dht.DHT22(machine.Pin(DHT_PIN)) # change DHT11 for physical device

# Initialize OLED display
i2c = machine.I2C(scl=machine.Pin(9), sda=machine.Pin(8))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Function to animate the text character by character with inverted color effect
def display_text_animated(text, y_position, delay=0.2, invert=False):
    oled.fill(0)  # Clear the screen before printing
    for i in range(len(text) + 1):
        oled.text(text[:i], 24, y_position)
        if invert:
            oled.invert(True)  # Invert the screen (changes white text to black and vice versa)
        oled.show()
        time.sleep(delay)

# Main loop
while True:
    try:
        dht_sensor.measure()
        time.sleep(0.2)
        temp = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        # print(temp, humidity)
        oled.fill(0)  # Clear the screen before printing
        
        # Simulate printing "Faisal Chan" one character at a time with inverted text color
        display_text_animated("Faisal Chan", 28, delay=0.1, invert=True)
        
        oled.show()

    except Exception as e:
        print("Error reading DHT22 sensor:", e)
    
    time.sleep(1)  # Update every 1 second

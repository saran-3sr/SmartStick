from gpiozero import DistanceSensor
import time

# Define the GPIO pins for your sensors
sensor1 = DistanceSensor(echo=17, trigger=4)  # Change these pin numbers as needed
sensor2 = DistanceSensor(echo=27, trigger=22)
sensor3 = DistanceSensor(echo=6, trigger=5)

try:
    while True:
        # Read distances from the sensors
        distance1 = sensor1.distance * 100  # Convert to centimeters
        distance2 = sensor2.distance * 100
        distance3 = sensor3.distance * 100

        if distance1<100:
            print("Object on left")
        if distance2<100:
            print("Object on front")
        if distance3<100:
            print("Object on Right")
finally:
    print("Working")
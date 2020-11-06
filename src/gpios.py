from gpiozero import LED, Button

#(GPIOs)
#leds cars
green_cars = LED(7)
orange_cars = LED(24)
red_cars = LED(10)

#buttons
pedestrian_button_1 = Button(17)
pedestrian_button_2 = Button(4)

#active button led
led_button = LED(11)

#leds pedestrians
green_pedestrian = LED(25)
red_pedestrian = LED(22)

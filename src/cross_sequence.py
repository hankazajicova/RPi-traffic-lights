import time
from src.gpios import green_cars, green_pedestrian
from src.gpios import orange_cars, red_pedestrian, red_cars, led_button

#    time sleep (in seconds)

def wait_for_green(delay: int):
    """button light is initiated and process is waiting depending on delay

    Args:
        delay (int): delay time, depending on the time of the last crossing
    """
    led_button.on()
    time.sleep(delay)


def stop_cars():
    """
    green light is blinking for 5 seconds, then is off
    orange light on and off
    finally red light is initiated
    """
    green_cars.blink()
    time.sleep(5)
    green_cars.off()
    orange_cars.on()
    time.sleep(2)
    orange_cars.off()
    red_cars.on()
    time.sleep(2)


def pedestrian_go():
    """
    red light s swaped for green and button light is off
    after 5 seconds green starts blinking
    after another 5 seconds is green light swaped for red
    """
    red_pedestrian.off()
    green_pedestrian.on()
    led_button.off()
    time.sleep(5)
    green_pedestrian.blink()
    time.sleep(5)
    green_pedestrian.off()
    red_pedestrian.on()
    time.sleep(2)


def cars_go():
    """
    orange light is initiated for a second
    red light is off and green on
    """
    orange_cars.on()
    time.sleep(2)
    orange_cars.off()
    red_cars.off()
    green_cars.on()


def tl_sequence(delay: int) -> None:
    """
    crosswalk sequence
    """
    wait_for_green(delay)
    stop_cars()
    pedestrian_go()
    cars_go()

import time
from gpiozero import LED, Button
from src.cross_sequence import tl_sequence
from src.gpios import *


def get_delay(last_time_traffic_started: float) -> int:
    """
    calculator for the crossing sequence delay - can start at least 20 seconds after last crossing

    Args:
        last_time_traffic_started (float): time of the end of last sequence

    Returns:
        int: time delay for crosswalk sequence
    """
    time_limit = 20
    difference = time_limit - (time.time() - last_time_traffic_started)
    if difference < 5:
        return 5
    else:
        return int(difference)


def traffic_lights() -> None:
    """
    method for traffic lights pedestrian crosswalk
    """
    last_time_traffic_started = 0
    try:
        while True:
            if pedestrian_button_1.is_pressed or pedestrian_button_2.is_pressed:
                diff = get_delay(last_time_traffic_started)
                tl_sequence(diff)
                last_time_traffic_started = time.time()
            else:
                green_cars.on()
                red_pedestrian.on()
                    
    except KeyboardInterrupt:
        pass


def main():
    traffic_lights()
    
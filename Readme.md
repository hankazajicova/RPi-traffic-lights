# Traffic-lights-for-pedestrian-crosswalk

- sequence for pedestrian crosswalk
- defaultly green lights for cars and red lights for pedestrians
- sequence reacts on one of the buttons pressed

- Run with:

    ```bash
    ./run.py
    ```

- debugged with Python extension for Visual Studio Code
- cleaned with mypy and pylint using:

    ```bash
    pylint *.py **/*.py
    mypy *.py **/*.py
    ```

- disabled missing-module-docstring in .pylintrc

## Doveloped for

- Raspberry Pi 1 with GPIO led diods and buttons
- led diods and buttons switched in GPIO pins as specified in gpios.py and in scheme below

![traffic_scheme](https://user-images.githubusercontent.com/11961745/98423484-0159b300-208f-11eb-9f64-46026f50c545.jpg)

## Links

[RaspberryPi](https://www.raspberrypi.org/)

[Debugging](https://code.visualstudio.com/docs/python/debugging)

[Pylint](https://www.pylint.org/)

[Mypy](https://mypy.readthedocs.io/en/stable/)

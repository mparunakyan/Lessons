import time
from termcolor import colored, cprint


class TrafficLight:
    __color = "red"

    def running(self):
        my_dict = {"red": 7, "yellow": 2, "green": 7}
        # print(my_dict.keys())
        while True:
            for i in my_dict:
                self.__color = i
                print(f"{colored(self.__color, i)}")
                time.sleep(my_dict.get(i))


tr_light = TrafficLight()
tr_light.running()

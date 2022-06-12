from time import sleep
from itertools import cycle


class TrafficLight:
    __colors = ('Red', 'Yellow', 'Green', 'Yellow')

    def __init__(self, red_duration=None, yellow_duration=None, green_duration=None, is_limit=True):
        self.is_limit = is_limit
        self.duration = {'Red': 7, 'Yellow': 2, 'Green': 5}
        if red_duration is not None:
            self.duration['Red'] = red_duration
        if yellow_duration is not None:
            self.duration['Yellow'] = yellow_duration
        if green_duration is not None:
            self.duration['Green'] = green_duration

    def state(self, color):
        return color

    def running(self):
        for i, color in enumerate(cycle(self.__colors)):
            try:
                print(self.state(color))
                sleep(self.duration[color])
                if self.is_limit:
                    if i > 8:
                        break
            except KeyboardInterrupt:
                print('Stop by user')
                break


TrafficLight_simple = TrafficLight()
TrafficLight_simple.running()

TrafficLight_adv = TrafficLight(1, 1, 1, False)
TrafficLight_adv.running()

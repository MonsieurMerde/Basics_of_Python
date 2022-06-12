class Car:

    def __init__(self, color, is_police=False):
        self.speed = 0
        self.color = color
        self.name = Car.__name__
        self.is_police = is_police
        self.limit = {'TownCar': 60, 'WorkCar': 40}
        self.direction = {'Направо': 0.9, 'Налево': 0.93}

    def go(self, time):
        for time in range(1, time):
            speed = self.speed + time*2
            self.speed = speed
        print('Машина поехала')

    def stop(self, time):
        for time in range(time+1):
            speed = round(self.speed + time * -1.5, 1)
            if speed <= 0:
                self.speed = 0
                print('Машина остановилась')
                break
            self.speed = speed

    def turn(self, direction_by_user):
        self.speed *= round(self.direction[direction_by_user], 1)
        print(f'Поворот {direction_by_user.lower()}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed}')


class TownCar(Car):

    def __init__(self, color):
        super().__init__(color)
        self.name = TownCar.__name__

    def go(self, time):
        for time in range(1, time+1):
            speed = self.speed + time*2
            self.speed = speed
        print('Машина поехала')
        if self.speed > self.limit[self.name]:
            print('Превышение скорости')


class SportCar(Car):
    def __init__(self, color):
        super().__init__(color)
        self.name = SportCar.__name__


class WorkCar(Car):

    def __init__(self, color):
        super().__init__(color)
        self.name = WorkCar.__name__

    def go(self, time):
        for time in range(1, time+1):
            speed = self.speed + time*2
            self.speed = speed
        print('Машина поехала')
        if self.speed > self.limit[self.name]:
            print('Превышение скорости')


class PoliceCar(Car):
    def __init__(self, color):
        super().__init__(color, is_police=True)
        self.name = PoliceCar.__name__


town_car = TownCar('Red')
print(town_car.color)
print(town_car.name)
print(town_car.is_police)
print(town_car.speed)
town_car.show_speed()
town_car.go(1)
town_car.show_speed()
town_car.go(10)
town_car.show_speed()
town_car.turn('Направо')
town_car.show_speed()
town_car.go(5)
town_car.show_speed()
town_car.stop(10)
town_car.show_speed()
town_car.stop(200)
town_car.show_speed()

sport_car = SportCar('Yellow')
print(sport_car.color)
print(sport_car.name)
print(sport_car.is_police)
print(sport_car.speed)
sport_car.show_speed()
sport_car.go(25)
sport_car.show_speed()
sport_car.turn('Налево')
sport_car.show_speed()
sport_car.stop(20)
sport_car.show_speed()
sport_car.stop(50)
sport_car.show_speed()

work_car = WorkCar('Green')
print(work_car.color)
print(work_car.name)
print(work_car.is_police)
print(work_car.speed)
work_car.show_speed()
work_car.go(10)
work_car.show_speed()
work_car.stop(5)
work_car.show_speed()
work_car.turn('Направо')
work_car.show_speed()
work_car.stop(10)
work_car.show_speed()

police_car = PoliceCar('Black & White')
print(police_car.color)
print(police_car.name)
print(police_car.is_police)
print(police_car.speed)
police_car.show_speed()
police_car.go(20)
police_car.show_speed()
police_car.turn('Налево')
police_car.show_speed()
police_car.stop(10)
police_car.show_speed()


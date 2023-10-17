class Vehicle:
    can_jump = False

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._started = False

    def start(self):
        print("Starting engine...")
        self._started = True

    def stop(self):
        print("Stopping engine...")
        self._started = False

    def jump(self):
        if self.can_jump:
            print("Jumping...")
        else:
            raise ValueError(f"Vehicle of type {type(self)} can't jump")


class Car(Vehicle):
    def __init__(self, make, model, year, num_seats):
        super().__init__(make, model, year)
        self.num_seats = num_seats

    def drive(self):
        print(f'Driving my "{self.make} - {self.model}" on the road')

    def __str__(self):
        return f'"{self.make} - {self.model}" has {self.num_seats} seats'


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def ride(self):
        print(f'Riding my "{self.make} - {self.model}" on the road')

    def __str__(self):
        return f'"{self.make} - {self.model}" has {self.num_wheels} wheels'


class Horse(Vehicle):
    can_jump = True

    def __init__(self, model, year):
        super().__init__(None, model, year)


if __name__ == '__main__':
    toyota_prado = Car('Toyota', 'Prado', 2006, 5)
    print(toyota_prado.can_jump)

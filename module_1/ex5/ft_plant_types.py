class Plant:
    def __init__(self, name: str, height: float, days: int,
                 growth: float) -> None:
        self.name = name
        self._height = 0.0
        self._days = 0
        self.set_height(height)
        self.set_age(days)
        self.growth = growth

    def set_height(self, new_height: float) -> None:
        if (new_height < 0):
            print(f"{self.name}: Error, height can't be negative")
            print('Height update rejected')
        else:
            self._height = new_height

    def get_height(self) -> float:
        return (self._height)

    def set_age(self, new_age: int) -> None:
        if (new_age < 0):
            print(f"{self.name}: Error, age can't be negative")
            print('Age update rejected')
        else:
            self._days = new_age

    def get_age(self) -> int:
        return (self._days)

    def grow(self) -> None:
        self._height += self.growth

    def age(self) -> None:
        self._days += 1

    def show(self) -> None:
        print(
            f"{self.name}: {round(self._height, 1)}cm, {self._days} days old"
            )

class Flower(Plant):
    def __init__(self, name: str, _height: float, _days: int, growth: float, color: str, bloomed: bool) -> None:
        super().__init__(name, _height, _days, growth)
        self.color = color
        self.bloomed = False
        self.bloomed = bloomed

    def bloom(self) -> None:
        if (self.bloomed == False):
            print(f'{self.name}: has not bloomed yet')
            print('[asking the rose to bloom]')
            self.bloomed = True
        elif (self.bloomed == True):
            self.show()
            print(f'{self.name} is blooming beautifully!')

class Tree(Plant):
    def __init__(self, name: str, _height: float, _days: int, growth: float, trunk_diameter: float) -> None:
        super().__init__(name, _height, _days, growth)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print('[asking the oak to produce shade]')
        print(f'Tree Oak now produces a shade of {self._height} long and {self.trunk_diameter} wide.')

class Vegetable(Plant):
    def __init__(self, name: str, _height: float, _days: int, growth: float, harvest_season, nutritional_value) -> None:
        super().__init__(name, _height, _days, growth)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":

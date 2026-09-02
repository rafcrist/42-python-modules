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
    def __init__(self, name: str, height: float, days: int,
                 growth: float, color: str) -> None:
        super().__init__(name, height, days, growth)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f'Color: {self.color}')
        if (self.bloomed is True):
            print(f'{self.name} is blooming beautifully!')
        elif (self.bloomed is False):
            print(f'{self.name} has not bloomed yet')


class Tree(Plant):
    def __init__(self, name: str, height: float, days: int, growth: float,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, days, growth)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f'Trunk diameter: {self.trunk_diameter}cm')

    def produce_shade(self) -> None:
        print(
              f'Tree {self.name} now produces a shade of '
              f'{self._height}cm long and {self.trunk_diameter}cm wide.'
        )


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days: int, growth: float,
                 harvest_season: str) -> None:
        super().__init__(name, height, days, growth)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f'Harvest season: {self.harvest_season}')
        print(f'Nutritional value: {self.nutritional_value}')

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1


if __name__ == "__main__":
    print('=== Garden Plant Types ===')
    print('=== Flower')
    rose = Flower('Rose', 15.0, 10, 0, 'red')
    rose.show()
    print('[asking the rose to bloom]')
    rose.bloom()
    rose.show()
    print('\n')
    print('=== Tree')
    oak = Tree('Oak', 200.0, 365, 0, 5.0)
    oak.show()
    print('[asking the oak to produce shade]')
    oak.produce_shade()
    print('\n')
    print('=== Vegetable')
    tomato = Vegetable('Tomato', 5.0, 10, 2.10, 'April')
    tomato.show()
    print('[make tomato grow and age for 20 days]')
    for _ in range(0, 20):
        tomato.age()
        tomato.grow()
    tomato.show()

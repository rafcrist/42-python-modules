class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

    def __init__(self, name: str, height: float, days: int,
                 growth: float) -> None:
        self.name = name
        self._height = 0.0
        self._days = 0
        self.set_height(height)
        self.set_age(days)
        self.growth = growth
        self.stats = Plant.Stats()

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
        self.stats.grow_calls += 1

    def age(self) -> None:
        self._days += 1
        self.stats.age_calls += 1

    def show(self) -> None:
        print(
            f"{self.name}: {round(self._height, 1)}cm, {self._days} days old"
            )
        self.stats.show_calls += 1

    @staticmethod
    def is_older(days: int) -> bool:
        if (days > 365):
            return (True)
        return (False)

    @classmethod
    def empty_plant(cls) -> "Plant":
        new_plant = cls('Unknown plant', 0.0, 0, 0.0)
        return (new_plant)


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
    class StatsTree(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self.shade_calls = 0

    def __init__(self, name: str, height: float, days: int, growth: float,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, days, growth)
        self.stats = Tree.StatsTree()
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f'Trunk diameter: {self.trunk_diameter}cm')

    def produce_shade(self) -> None:
        print(
              f'Tree {self.name} now produces a shade of '
              f'{self._height}cm long and {self.trunk_diameter}cm wide.'
        )
        self.stats.shade_calls += 1


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


class Seed(Flower):
    def __init__(self, name: str, height: float, days: int,
                 growth: float, color: str) -> None:
        super().__init__(name, height, days, growth, color)
        self.seeds = 0

    def show(self) -> None:
        super().show()
        print(f'Seeds: {self.seeds}')

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42


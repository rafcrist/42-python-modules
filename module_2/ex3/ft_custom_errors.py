class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "The tomato plant is wilting!") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


def raiser_function(string: str) -> None:
    if (string == "PlantError"):
        raise PlantError()
    elif (string == "WaterError"):
        raise WaterError()
    elif (string == "GardenError"):
        raise GardenError()


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        raiser_function("PlantError")
    except PlantError as error:
        print(f"Caught PlantError: {error}\n")
    print("Testing WaterError...")
    try:
        raiser_function("WaterError")
    except WaterError as error:
        print(f"Caught WaterError: {error}\n")
    print("Testing catching all garden errors...")
    try:
        raiser_function("PlantError")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        raiser_function("WaterError")
    except GardenError as error:
        print(f"Caught GardenError: {error}\n")
    print("All custom error types work correctly!")
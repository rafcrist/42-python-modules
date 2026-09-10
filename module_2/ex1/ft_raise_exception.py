def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if (temp_int < 0):
        raise ValueError(f"{temp_int} is too cold for plants (min 0°C)")
    elif (temp_int > 40):
        raise ValueError(f"{temp_int} is too hot for plants (max 40°C)")
    else:
        return (temp_int)


def test_temperature() -> None:
    temp_int = input_temperature("25")
    print(f"Input data is '{temp_int}'")    
    print(f"Temperature is now {temp_int}°C\n")
    print("Input data is 'abc'")
    try:
        temp_int = input_temperature("abc")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")
    print("Input data is '100'")
    try:
        temp_int = input_temperature("100")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")
    print("Input data is '-50'")
    try:
        temp_int = input_temperature("-50")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()

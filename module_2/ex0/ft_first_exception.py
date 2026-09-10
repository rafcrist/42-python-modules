def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    return (temp_int)


def test_temperature() -> None:
    temp_int = input_temperature("25")
    print(f"Input data is '{temp_int}'")
    print(f"Temperature is now {temp_int}°C\n")
    print("Input data is 'abc'")
    try:
        temp_int = input_temperature("abc")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()

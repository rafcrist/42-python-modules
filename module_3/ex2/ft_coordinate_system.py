import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        valid = True
        coord = input("Enter new coordinates as floats in format 'x,y,z': ")
        splitted_coord = coord.split(",")
        float_coord = []
        try:
            x, y, z = splitted_coord
        except ValueError:
            print("Invalid syntax")
            continue
        for parameter in x, y, z:
            try:
                float_coord.append(float(parameter))
            except ValueError:
                print(
                    f"Error on parameter '{parameter}': "
                    f"could not convert string to float: '{parameter}'"
                )
                valid = False
                break
        if not (valid):
            continue
        f_x, f_y, f_z = float_coord
        return (f_x, f_y, f_z)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first_coord = get_player_pos()
    float_x, float_y, float_z = first_coord
    print(f"Got a first tuple: ({float_x}, {float_y}, {float_z})")
    print(f"It includes: X={float_x}, Y={float_y}, Z={float_z}")
    result = math.sqrt(float_x**2 + float_y**2 + float_z**2)
    print(f"Distance to center: {result:.4f}")
    print("Get a second set of coordinates")
    second_coord = get_player_pos()
    float_x2, float_y2, float_z2 = second_coord
    result2 = math.sqrt((float_x2 - float_x)**2 +
                        (float_y2 - float_y)**2 +
                        (float_z2 - float_z)**2)
    print(f"Distance between the 2 sets of coordinates: {result2:.4f}")

import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = {}
    for arg in sys.argv[1:]:
        try:
            item, quantity = arg.split(':')
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
            continue
        try:
            quantity = int(quantity)
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")
            continue
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue
        inventory[item] = quantity
    print(f"Got inventory: {inventory}")
    keys = list(inventory.keys())
    print(f"Item list: {keys}")
    quant = list(inventory.values())
    total = sum(quant)
    print(f"Total quantity of the {len(keys)} items: {total}")
    i = 0
    if (inventory):
        max_item = keys[0]
        min_item = keys[0]
        for item in inventory:
            if (inventory[item] < inventory[min_item]):
                min_item = item
            if (inventory[item] > inventory[max_item]):
                max_item = item
            if (total > 0):
                percent = (quant[i] / total) * 100
                print(f"Item {keys[i]} represents {round(percent, 1)}%")
            i += 1
        print(
            "Item most abundant: "
            f"{max_item} with quantity {inventory[max_item]}"
        )
        print(
            "Item least abundant: "
            f"{min_item} with quantity {inventory[min_item]}"
        )
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")

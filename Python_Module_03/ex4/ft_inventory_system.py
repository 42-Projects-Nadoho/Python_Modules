import sys


def ft_inventory_system() -> None:
    """The main function of this part
    """
    print("=== Inventory System Analysis ===")
    invent = {item.split(":")[0]: int(item.split(":")[1])
              for item in sys.argv[1:]}
    total = sum(invent.values())
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(invent.keys())}")

    print("\n=== Current Inventory ===")
    [print(f"{i}: {j} units ({(j / total) * 100:.2f}%)")
     for i, j in invent.items()]

    max_val = float('-inf')
    for k, v in invent.items():
        if v > max_val:
            max_val = v
            max_key = k

    min_val = float('inf')
    for k, v in invent.items():
        if v < min_val:
            min_val = v
            min_key = k
    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {max_key} ({invent[max_key]} "
          f"unit{'s' if invent[max_key] > 1 else ''})")
    print(f"Least abundant: {min_key} ({invent[min_key]} "
          f"unit{'s' if invent[min_key] > 1 else ''})")

    moderate = {k: v for k, v in invent.items() if v == max_val}
    scarce = {k: v for k, v in invent.items() if v != max_val}
    print("\n=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    restock = [k for k, v in invent.items() if v <= 1]
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {[k for k in invent]}")
    print(f"Dictionary values: {[k for k in invent.values()]}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in invent}")


if __name__ == "__main__":
    ft_inventory_system()

# import sys
import math


def ft_parse_coordinates(coord_str: str) -> tuple[int, int, int] | None:
    """This is a function used to parse coordinates in a tuple and catch error
    with them

    Args:
        coord_str (str): the coordonates in this format : "1,2,3"

    Raises:
        ValueError: All error in corrds formats like : "A,1, 4" and "1,5,6,7"

    Returns:
        tuple[int, int, int] | None: The tuple of coordinates or a
        error in certains cases
    """
    try:
        coords = tuple(int(x) for x in coord_str.split(","))
        if len(coords) != 3:
            raise ValueError("Coordinates must have exactly 3 values")
        return coords
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return None


def ft_distance(coord1: tuple, coord2: tuple) -> float:
    """This function calculate the distanceof two tuples of coordinates

    Args:
        coord1 (tuple):
        coord2 (tuple):

    Returns:
        float: the distance of the two coordinates
    """
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return dist


def ft_coordinate_system() -> None:
    """the main function of the exercice
    """
    print("=== Game Coordinate System ===")
    origin = (0, 0, 0)

    position = (10, 20, 5)
    print(f"\nPosition created: {position}")
    dist = ft_distance(origin, position)
    print(f"Distance between {origin} and {position}: {dist:.2f}")

    str_position = "3,4,0"
    print(f"\nParsing coordinates: {str_position}")
    pars_str_position = ft_parse_coordinates(str_position)
    dis_str_position = ft_distance(origin, pars_str_position)
    print(f"Parsed position: {pars_str_position}")
    print(f"Distance between {origin} and {pars_str_position}: "
          f"{dis_str_position:.1f}")

    err1_position = "abc,def,ghi"
    print(f"\nParsing coordinates: {err1_position}")
    ft_parse_coordinates(err1_position)

    err2_position = "3,4,0, 10"
    print(f"\nParsing coordinates: {err2_position}")
    ft_parse_coordinates(err1_position)

    print("\nUnpacking demonstration:")
    print(f"Player at x={pars_str_position[0]}, y={pars_str_position[1]}, "
          f"z={pars_str_position[2]}")
    print(f"Coordinates: X={pars_str_position[0]}, Y={pars_str_position[1]}, "
          f"Z={pars_str_position[2]}")

    # if len(sys.argv) == 1:
    #     print("\nNo coordinates provided!")
    #     return

    # for arg in sys.argv[1:]:
    #     print(f'\nParsing coordinates: "{arg}"')
    #     parsed = ft_parse_coordinates(arg)
    #     if parsed:
    #         print(f"Parsed position: {parsed}")
    #         dist = ft_distance(origin, parsed)
    #         print(f"Distance between {origin} and {parsed}: {dist:.1f}")
    #         print("Unpacking demonstration:")
    #         x, y, z = parsed
    #         print(f"Player at x={x}, y={y}, z={z}")
    #         print(f"Coordinates: X={x}, Y={y}, Z={z}")
    #     print()


if __name__ == "__main__":
    ft_coordinate_system()

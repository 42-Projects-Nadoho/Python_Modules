import sys


def ft_print_params(params_list: list[str]) -> None:
    """
    This is a function for print all elemets is a list

    :param params_list: list of
    :type params_list: list[str]
    """
    print(f"Arguments received: {len(params_list)}")
    [print(f"Argument {i + 1}: {w}") for i, w in enumerate(params_list)]


def ft_command_quest() -> None:
    """
    ft_command_quest is a function that shows the art
    of receiving external data
    """
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) > 1:
        ft_print_params(sys.argv[1:])
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest()

import sys


def ft_score_analytics2(params_list: list[str]) -> None:
    """ft_score_analytics2 is a function using to
    print statistics of a a list of players

    Args:
        params_list (list[str]): A list of players
    """
    print(f"Scores processed: {params_list}")
    print(f"Total players: {len(params_list)}")
    print(f"Total score: {sum(params_list)}")
    print(f"Average score: {sum(params_list) / len(params_list)}")
    print(f"High score: {max(params_list)}")
    print(f"Low score: {min(params_list)}")
    print(f"Score range: {max(params_list) - min(params_list)}")


def ft_score_analytics() -> None:
    """the primary function ft_score_analytics that used to handle errors
    and make the analysis
    """
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        line = "No scores provided. "
        line += "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        print(line)
    else:
        try:
            params_list = [int(param) for param in sys.argv[1:]]
            ft_score_analytics2(params_list)
        except ValueError as e:
            print(f"Error : {e}")


if __name__ == "__main__":
    ft_score_analytics()

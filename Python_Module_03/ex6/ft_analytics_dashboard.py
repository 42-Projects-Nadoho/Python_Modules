def ft_analytics_dashboard() -> None:
    """_summary_
    """
    print("=== Game Analytics Dashboard ===")
    players = {
        "alice": {
            "score": 2300,
            "achievements": {
                'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'
            },
            "activity": True,
            "region": "north"
        },
        "bob": {
            "score": 1800,
            "achievements": {
                'first_kill', 'level_10', 'boss_slayer', 'collector'
            },
            "activity": True,
            "region": "east"
        },
        "charlie": {
            "score": 2150,
            "achievements": {
                'level_10', 'treasure_hunter', 'boss_slayer',
                'speed_demon', 'perfectionist'
            },
            "activity": True,
            "region": "central"
        },
        "diana": {
            "score": 1900,
            "achievements": {
                'first_kill', 'collector'
            },
            "activity": False,
            "region": "north"
        }
    }

    print("\n=== List Comprehension Examples ===")
    high_scorers = [p for p, d in players.items() if d["score"] > 2000]
    scores_doubled = [d["score"] * 2 for d in players.values()]
    active_players = [p for p, d in players.items() if d.get("activity")]
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {p: d["score"] for p, d in players.items()}
    player_categories = {
        p: ("high" if s > 2000 else "medium" if s >= 1500 else "low")
        for p, s in player_scores.items()
    }
    score_categories = {
        cat: sum(1 for v in player_categories.values() if v == cat)
        for cat in ("high", "medium", "low")
    }
    achv_counts = {p: len(d["achievements"]) for p, d in players.items()}
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achv_counts}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {p for p in players}
    unique_achievements = {ach for d in players.values()
                           for ach in d["achievements"]}
    active_regions = {d["region"]
                      for d in players.values() if d.get("activity")}
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    tt_players = len(players)
    total_unique_ach = len(unique_achievements)
    avg_scr = sum(player_scores.values()) / tt_players if tt_players else 0
    top_performer = max(player_scores, key=player_scores.get)
    top_score = player_scores[top_performer]
    top_achievements = len(players[top_performer]["achievements"])
    print(f"Total players: {tt_players}")
    print(f"Total unique achievements: {total_unique_ach}")
    print(f"Average score: {avg_scr}")
    print(f"Top performer: {top_performer} "
          f"({top_score} points, {top_achievements} achievements)")


if __name__ == "__main__":
    ft_analytics_dashboard()

def ft_achievement_tracker() -> None:
    """The main function of this part
    """
    print("=== Achievement Tracker System ===")
    alice = {'first_kill', 'level_10', 'treasure_hunter',
             'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer',
           'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
               'speed_demon', 'perfectionist'}
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    uni = alice.union(bob, charlie)
    print(f"All unique achievements: {uni}")
    print(f"Total unique achievements: {len(uni)}")

    common = alice.intersection(bob, charlie)
    print(f"\nCommon to all players: {common}")

    rare = (alice - bob - charlie) | (bob - alice - charlie) | \
           (charlie - alice - bob)
    print(f"Rare achievements (1 player): {rare}")

    print(f"\nAlice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    ft_achievement_tracker()

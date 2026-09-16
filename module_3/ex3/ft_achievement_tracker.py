import random


def achievements() -> list[str]:
    achievements = [
        'Crafting Genius', 'Strategist', 'World Savior',
        'Speed Runner', 'Survivor', 'Master Explorer',
        'Treasure Hunter', 'Unstoppable', 'First Steps',
        'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer', 'Hidden Path Finder'
        ]
    return (achievements)


def gen_player_achievements() -> set[str]:
    all_achievements = achievements()
    amount = random.randint(3, 10)
    picked = random.sample(all_achievements, amount)
    picked = set(picked)
    return (picked)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    all_achievements = achievements()
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")
    everyone = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {everyone}\n")
    common = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common}\n")
    alice_difference = alice.difference(bob, charlie, dylan)
    bob_difference = bob.difference(alice, charlie, dylan)
    charlie_difference = charlie.difference(alice, bob, dylan)
    dylan_difference = dylan.difference(charlie, bob, alice)
    print(f"Only Alice has: {alice_difference}")
    print(f"Only Bob has: {bob_difference}")
    print(f"Only Charlie has: {charlie_difference}")
    print(f"Only Dylan has: {dylan_difference}\n")
    set_achiev = set(all_achievements)
    alice_miss = set_achiev.difference(alice)
    bob_miss = set_achiev.difference(bob)
    charlie_miss = set_achiev.difference(charlie)
    dylan_miss = set_achiev.difference(dylan)
    print(f"Alice is missing: {alice_miss}")
    print(f"Bob is missing: {bob_miss}")
    print(f"Charlie is missing: {charlie_miss}")
    print(f"Dylan is missing: {dylan_miss}")

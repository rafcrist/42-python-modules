import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    players_list = ['Alice', 'bob', 'Charlie', 'dylan',
                    'Emma', 'Gregory', 'john', 'kevin', 'Liam'
                    ]
    print(f"Initial list of players: {players_list}")
    cap_list = [name.capitalize() for name in players_list]
    print(f"New list with all names capitalized: {cap_list}")
    cap_only = [name for name in players_list if name == name.capitalize()]
    print(f"New list of capitalized names only: {cap_only}\n")
    score_list = {name: random.randint(1, 100) for name in cap_list}
    print(f"Score dict: {score_list}")
    values = [score_list[value] for value in score_list]
    average = round(sum(values) / len(score_list), 2)
    print(f"Score average is {average}")
    high_scores = {
        value: score_list[value]
        for value in score_list if score_list[value] > average
    }
    print(f"High scores: {high_scores}")

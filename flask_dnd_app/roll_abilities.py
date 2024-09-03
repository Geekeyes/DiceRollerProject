import d20

def roll_ability_scores():
    scores = []
    for _ in range(6):  # Roll for each of the 6 abilities
        roll = d20.roll("4d6kh3")  # Roll 4d6 and keep the highest 3
        scores.append(roll.total)  # Append the total of the roll to the list
    return scores

if __name__ == "__main__":
    ability_scores = roll_ability_scores()
    print("Your rolled ability scores are:", ability_scores)

def get_answers():
    with open("input.txt", "r") as file:
        grouped_answers = file.read().split("\n\n")
        grouped_answers = [answers.split("\n") for answers in grouped_answers]
    return grouped_answers


def calculate_score(groups_answers):
    score = 0
    for char in "abcdefghijklmnopqrstuvwxyz":
        for persons_answers in groups_answers:
            if char not in persons_answers:
                break
        else:
            score += 1
    return score


def sum_of_scores(grouped_answers):
    total = 0
    for groups_answers in grouped_answers:
        total += calculate_score(groups_answers)
    return total


grouped_answers = get_answers()
print(sum_of_scores(grouped_answers))

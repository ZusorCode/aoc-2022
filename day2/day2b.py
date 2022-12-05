from aocd import lines, submit


shape_scores = {
    "A": 1,
    "B": 2,
    "C": 3
}

you_win = {
    "A": "B",
    "B": "C",
    "C": "A"
}

you_lose = {
    "A": "C",
    "B": "A",
    "C": "B"
}


score = 0
for line in lines:
    enemy = line.split(" ")[0]
    goal_strategy = line.split(" ")[1]
    if goal_strategy == "X":
        score += 0
        score += shape_scores.get(you_lose.get(enemy))
    elif goal_strategy == "Y":
        score += 3
        score += shape_scores.get(enemy)
    elif goal_strategy == "Z":
        score += 6
        score += shape_scores.get(you_win.get(enemy))


submit(score)

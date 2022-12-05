from aocd import lines, submit

beats = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

shape_scores = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

identicals = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}


score = 0
for line in lines:
    opponent = line.split(" ")[0]
    you = line.split(" ")[1]
    score += shape_scores.get(you)
    if beats[opponent] == you:
        score += 0
    elif identicals[opponent] == you:
        score += 3
    else:
        score += 6

submit(score)

from aocd import lines, submit

score = 0
for line in lines:
    a, b = line.split(",")
    a1, a2 = [int(x) for x in a.split("-")]
    b1, b2 = [int(x) for x in b.split("-")]
    a_nums = set(range(a1, a2 + 1))
    b_nums = set(range(b1, b2 + 1))
    if len(a_nums.intersection(b_nums)) > 0:
        score += 1
submit(score)

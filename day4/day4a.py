from aocd import lines, submit


score = 0
for line in lines:
    a, b = line.split(",")
    a1, a2 = [int(x) for x in a.split("-")]
    b1, b2 = [int(x) for x in b.split("-")]
    a_nums = set(range(a1, a2 + 1))
    b_nums = set(range(b1, b2 + 1))
    if a_nums.issubset(b_nums) or b_nums.issubset(a_nums):
        score += 1
submit(score)

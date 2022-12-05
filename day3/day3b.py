from aocd import lines, submit
import string

score = 0


groups = []
for group in range(len(lines) // 3):
    groups.append(lines[group * 3:group * 3 + 3])
print(groups)
for group in groups:
    for char in group[0]:
        if char in group[1] and char in group[2]:
            print(char)
            score += string.ascii_letters.index(char) + 1
            break


submit(score)

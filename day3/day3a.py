from aocd import lines, submit
import string

score = 0
for line in lines:
    a, b = line[:len(line)//2], line[len(line)//2:]
    for char_a in a:
        if char_a in b:
            score += string.ascii_letters.index(char_a) + 1
            break

submit(score)

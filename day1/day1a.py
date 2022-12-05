from aocd import data, submit

elves = data.split("\n\n")
elves = [e.split("\n") for e in elves]
elves = [(int(num) for num in e) for e in elves]
elves = [sum(e) for e in elves]

submit(max(elves))

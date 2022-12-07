from aocd import data, submit

for i in range(len(data) - 4):
    if len(set(data[i:i+4])) == 4:
        submit(i + 4)
        break

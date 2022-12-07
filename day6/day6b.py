from aocd import data, submit

for i in range(len(data) - 14):
    if len(set(data[i:i+14])) == 14:
        submit(i + 14)
        break

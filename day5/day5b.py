from aocd import data, submit

stacks_diagram, instructions = data.split("\n\n")
stack_count = int(stacks_diagram.split("\n")[-1].strip()[-1])

stacks = {}
for stack_num in range(stack_count):
    stacks[stack_num] = [row[1 + stack_num * 4] for row in stacks_diagram.split("\n")[:-1]]
    stacks[stack_num] = [letter for letter in stacks[stack_num] if letter != " "]

for instruction in instructions.split("\n"):
    _, count, _, start, _, target = instruction.split(" ")
    count, start, target = int(count), int(start) - 1, int(target) - 1
    for i in range(count, 0, -1):
        stacks[target].insert(0, stacks[start].pop(i - 1))

output = "".join([stack[0] for stack in stacks.values()])
submit(output)
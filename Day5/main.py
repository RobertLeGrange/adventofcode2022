data = open("Day5\input.txt").read()
lines = data.split("\n")

positions = [lines[8].index(str) for str in lines[8] if str.isdigit()]


stacks = []
stack = []
for position in positions:
    for line in reversed(lines[:9]):
        for str in line[position]:
            if str.isalpha():
                stack.append(str)
    stacks.append(stack)
    stack = []


print(stacks)

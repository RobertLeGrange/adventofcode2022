import re

data = open("Day5\input.txt").read().rstrip()
lines = data.split("\n")

stacklines, positionlines, commandlines = lines[:8], lines[8], lines[10:]

positions = [positionlines.index(str) for str in positionlines if str.isdigit()]

stacks = []
stack = []
for position in positions:
    for line in reversed(stacklines):
        for str in line[position]:
            if str.isalpha():
                stack.append(str)
    stacks.append(stack)
    stack = []

pattern = re.compile("move | from | to ")

#CrateMover 9000
for line in commandlines:
    numcrate, fromcrate, tocrate = list(map(int, re.split(pattern, line)[1:]))
    for i in range(numcrate):
        tempcrate = stacks[fromcrate - 1].pop()
        stacks[tocrate - 1].append(tempcrate)

topstack = ''
for stack in stacks:
    topstack += stack[-1]
print(topstack)

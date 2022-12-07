import re

def stackloader(stacklines, positions):
    stacks = []
    stack = []
    for position in positions:
        for line in reversed(stacklines):
            for str in line[position]:
                if str.isalpha():
                    stack.append(str)
        stacks.append(stack)
        stack = []
    return stacks

def CrateMover9000(stacks, commandlines):
    pattern = re.compile("move | from | to ")
    for line in commandlines:
        numcrate, fromcrate, tocrate = list(map(int, re.split(pattern, line)[1:]))
        for i in range(numcrate):
            tempcrate = stacks[fromcrate - 1].pop()
            stacks[tocrate - 1].append(tempcrate)
    return stacks

def CrateMover9001(stacks, commandlines):
    pattern = re.compile("move | from | to ")
    for line in commandlines:
        numcrate, fromcrate, tocrate = list(map(int, re.split(pattern, line)[1:]))
        tempcrate = stacks[fromcrate - 1][-1*numcrate:]
        del stacks[fromcrate - 1][-1*numcrate:]
        stacks[tocrate - 1].extend(tempcrate)
    return stacks

def topstackprinter(stacks):
    topstack = "".join(stack[-1] for stack in stacks if stack)
    print("The top crate of each stack spells " + topstack)

if __name__ == "__main__":
    data = open("Day5\input.txt").read().rstrip()
    lines = data.split("\n")
    stacklines, positionlines, commandlines = lines[:8], lines[8], lines[10:]
    positions = [positionlines.index(str) for str in positionlines if str.isdigit()]
    stacks = stackloader(stacklines, positions)
    stacks = CrateMover9001(stacks, commandlines)
    topstackprinter(stacks)

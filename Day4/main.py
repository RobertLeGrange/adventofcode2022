file = open('Day4\input.txt').read()
lines = file.strip().split('\n')

partialcrossover, totalcrossover = 0, 0
for pair in lines:
    elf1, elf2 = pair.split(',')
    elf1start, elf1end = [int(i) for i in elf1.split('-')]
    elf2start, elf2end = [int(i) for i in elf2.split('-')]
    if elf1start >= elf2start and elf1end <= elf2end:
        totalcrossover += 1
    elif elf2start >= elf1start and elf2end <= elf1end:
        totalcrossover += 1
    if elf1end >= elf2start and elf1start <= elf2end:
        partialcrossover += 1
    elif elf2end >= elf1start and elf2start <= elf1end:
        partialcrossover += 1

print("There are {} assignment pairs which fully contain the other.".format(totalcrossover))
print("There are {} assignment pairs which partially contain the other.".format(partialcrossover))

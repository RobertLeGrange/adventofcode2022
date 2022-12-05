data = open("Day1\input.txt").read()
lines = data.strip().split("\n\n")

elves = [line.split("\n") for line in lines]
elfcalories = sorted([sum(map(int, elf)) for elf in elves])

print("The elf with the most calories is carrying {} calories.".format(max(elfcalories)))
print("The three elves with the most calories are carrying {} calories.".format(sum(elfcalories[-3:])))

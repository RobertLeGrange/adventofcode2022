rock, paper, scissors = 1, 2, 3
lose, draw, win = 0, 3, 6

part1score, part2score = 0, 0

data = open("Day2\input.txt").read()
lines = data.strip().split("\n")
games = [line.split(' ') for line in lines]
for opp, you in games:

    if you == "X":
        part1score += rock
        if opp == "A":
            part1score += draw
        elif opp == "B":
            part1score += lose
        elif opp == "C":
            part1score += win

    elif you == "Y":
        part1score += paper
        if opp == "A":
            part1score += win
        elif opp == "B":
            part1score += draw
        elif opp == "C":
            part1score += lose

    elif you == "Z":
        part1score += scissors
        if opp == "A":
            part1score += lose
        elif opp == "B":
            part1score += win
        elif opp == "C":
            part1score += draw
print("The score for Part One would be {}.".format(part1score))

for opp, outcome in games:

    if outcome == "X":
        part2score += lose
        if opp == "A": #Rock
            part2score += scissors
        elif opp == "B": #Paper
            part2score += rock
        elif opp == "C": #Scissors
            part2score += paper

    elif outcome == "Y":
        part2score += draw
        if opp == "A": #Rock
            part2score += rock
        elif opp == "B": #Paper
            part2score += paper
        elif opp == "C": #Scissors
            part2score += scissors

    elif outcome == "Z":
        part2score += win
        if opp == "A": #Rock
            part2score += paper
        elif opp == "B": #Paper
            part2score += scissors
        elif opp == "C": #Scissors
            part2score += rock
print("The score for Part Two would be {}.".format(part2score))

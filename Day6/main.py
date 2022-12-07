
def part1(data, numletters):
    letters, i = data[:numletters], numletters
    for letter in data[numletters:]:
        if len(set(letters)) < numletters:
            letters = letters[1:] + letter
        else:
            print(letter, i)
            break
        i += 1

def part2(data, numletters):
    letters, i = data[:numletters], numletters
    for letter in data[numletters:]:
        if len(set(letters)) < numletters:
            letters = letters[1:] + letter
        else:
            print(letter, i)
            break
        i += 1

if __name__ == "__main__":
    data = open('Day6\input.txt').read().strip()
    part1(data, 4)
    part2(data, 14)

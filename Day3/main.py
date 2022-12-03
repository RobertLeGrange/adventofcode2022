from string import ascii_lowercase, ascii_uppercase

def readandstrip(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    strippedlines = [line.strip('\n') for line in lines]
    return strippedlines

def splitintwo(line):
    length = len(line)
    if length % 2 == 0:
        splitline = [line[:length//2], line[length//2:]]
        return splitline
    else:
        print("Odd number of characters on line " + line)

def find_duplicates(line):
    duplicates = [letter for letter in line[0] if letter in line[1]]
    return set(duplicates)


if __name__ == "__main__":
    lines = readandstrip('Day3\input.txt')
    for line in lines:
        splitline = splitintwo(line)
        duplicates = find_duplicates(splitline)

alphabet = ascii_lowercase + ascii_uppercase
priorities = {key:value for (value, key) in enumerate(alphabet, 1)}
print(priorities)

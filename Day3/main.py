from string import ascii_lowercase, ascii_uppercase

def readandstrip(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    strippedlines = [line.strip('\n') for line in lines]
    return strippedlines

def splitintwo(line):
    length = len(line)
    splitline = [line[:length//2], line[length//2:]]
    return splitline

def find_duplicates(line):
    duplicates = [letter for letter in line[0] if letter in line[1]]
    return set(duplicates)

def splitintogroups(lines):
    groups = []
    for i in range(0, len(lines), 3):
        groups.append(lines[i:(i+3)])
    return groups

def find_badge(group):
    duplicates = [letter for letter in group[0] if letter in group[1] and letter in group[2]]
    return duplicates[0]

if __name__ == "__main__":
    lines = readandstrip('Day3\input.txt')
    prioritysum = 0
    badgesum = 0
    priorities = {key:value for (value, key) in enumerate(ascii_lowercase + ascii_uppercase, 1)}
    for line in lines:
        splitline = splitintwo(line)
        duplicates = find_duplicates(splitline)
        for duplicate in duplicates:
            prioritysum += priorities[duplicate]
    groups = splitintogroups(lines)
    for group in groups:
        badge = find_badge(group)
        badgesum += priorities[badge]
    print(badgesum)



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
    


if __name__ == "__main__":
    lines = readandstrip('Day3\input.txt')
    for line in lines:
        splitline = splitintwo(line)
        print(splitline)

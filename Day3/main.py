

def readandstrip(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    strippedlines = [line.strip('\n') for line in lines]
    return strippedlines

if __name__ == "__main__":
    lines = readandstrip('Day3\input.txt')
    print(lines)

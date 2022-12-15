with open("Day9\input.txt") as data:
    lines = data.read().strip().split("\n")

def diff(set1, set2):
    diff = tuple((a - b if a > b else b - a) for a, b in zip(set1, set2))
    return diff

def moverope(headpos, tailpos):
    if max(diff(headpos, tailpos)) > 1:
        move = tuple(1 if a > b else (-1 if a < b else 0) for a, b in zip(headpos, tailpos))
        position = tuple(map(sum, zip(tailpos, move)))
    else:
        move = (0,0)
        position = tuple(map(sum, zip(tailpos, move)))
    return position

moves = {"L":(-1, 0), "R":(1, 0), "U":(0, 1), "D":(0, -1)}

head, tail = [(0,0)], [(0,0)]
for line in lines:
    dir, amt = line.split()
    for i in range(0, int(amt)):
        move = moves[dir]
        newpos = tuple(map(sum, zip(move, head[-1])))
        head.append(newpos)

for headpos in head:
    tailpos = tail[-1]
    position = moverope(headpos, tailpos)
    tail.append(position)

print(len(set(tail)))

rope = [[(0,0)] for i in range(10)]

for headpos in head[1:]:
    for ind, piece in enumerate(rope):
        if ind == 0:
            piece.append(headpos)
        else: 
            piecepos = piece[-1]
            prevpiecepos = rope[ind-1][-1]
            position = moverope(prevpiecepos, piecepos)
            piece.append(position)

print(len(set(rope[-1])))

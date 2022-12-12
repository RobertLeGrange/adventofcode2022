with open("Day8\input.txt") as file:
    rows = file.read().strip().split("\n")
    cols = [''.join(s) for s in zip(*rows)]

def vischeck(checktrees, tree):
    visible = True
    for checktree in checktrees:
        checktree = int(checktree)
        if tree <= checktree:
            visible = False

    return visible

visibletrees = 0
for treeposy, row in enumerate(rows[1:-1]):
    treeposy += 1
    for treeposx, tree in enumerate(row[1:-1]):
        treeposx += 1
        visibleleft = vischeck(rows[treeposy][:treeposx], int(tree))
        visibleright = vischeck(rows[treeposy][treeposx+1:], int(tree))
        visibletop = vischeck(cols[treeposx][:treeposy], int(tree))
        visiblebottom = vischeck(cols[treeposx][treeposy+1:], int(tree))
        if visibleleft or visibleright or visibletop or visiblebottom:
            visibletrees = visibletrees + 1

visibletrees = visibletrees + len(rows[0])*2 + len(rows)*2 - 4
print(visibletrees)

def viewscore(checktrees, tree):
    score = 0
    for checktree in checktrees:
        checktree = int(checktree)
        score += 1
        if tree <= checktree:
            break
    return score

scoretotal = 0
for treeposy, row in enumerate(rows):
    for treeposx, tree in enumerate(row):
        scoreleft = viewscore(rows[treeposy][:treeposx][::-1], int(tree))
        scoreright = viewscore(rows[treeposy][treeposx+1:], int(tree))
        scoretop = viewscore(cols[treeposx][:treeposy][::-1], int(tree))
        scorebottom = viewscore(cols[treeposx][treeposy+1:], int(tree))
        if scoretotal < (scoreleft * scoreright * scoretop * scorebottom):
            scoretotal = scoreleft * scoreright * scoretop * scorebottom

print(scoretotal)
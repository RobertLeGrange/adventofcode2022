with open("Day8\input.txt") as file:
    rows = file.read().strip().split("\n")

def rowcheck(row, tree, treeposx):
    visible = False
    for checkposx, checktree in enumerate(row):
        if checkposx == treeposx:
            pass
        else:
            if tree > checktree:
                visible = True
                return visible

def colcheck(rows, tree, treeposx, treeposy):
    visible = False
    for checkposy, row in enumerate(rows):
        for checkposy, checktree in enumerate(row[treeposx]):
            if checkposy == treeposy:
                pass
            else:
                if tree > checktree:
                    visible = True
                    return visible

    
    

for treeposx, row in enumerate(rows[1:-1]):
    for treeposy, tree in enumerate(row[1:-1]):
        visiblex = rowcheck(rows[treeposy+1], tree, treeposx+1)
        visibley = colcheck(rows, tree, treeposx+1, treeposy+1)

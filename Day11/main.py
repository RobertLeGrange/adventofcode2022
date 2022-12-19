from math import floor, prod

with open("Day11\input.txt") as data:
    lines = data.read().strip()

monkeysdata = lines.split("\n\n")

class Monkey:
    def __init__(self):
        self.count = 0

    def additems(self, line):
        self.items = list(map(int, line.strip("Starting items: ").split(",")))

    def addid(self, id):
        self.id = id

    def addoperation(self, line):
        _, self.operation = line.split(" = ")

    def addtest(self, line):
        self.test = int(line.strip("  Test: divisible by "))
        
    def addtrue(self, line):
        self.true = int(line.strip("    If true: throw to monkey "))

    def addfalse(self, line):
        self.false = int(line.strip("    If false: throw to monkey "))

    def countitems(self):
        self.count += len(self.items)

monkeys = []
for monkeydata in monkeysdata:
    lines = monkeydata.split("\n")
    id = int(lines[0][7])
    monkeys.append(Monkey())
    monkeys[id].addid(id)
    monkeys[id].additems(lines[1])
    monkeys[id].addoperation(lines[2])
    monkeys[id].addtest(lines[3])
    monkeys[id].addtrue(lines[4])
    monkeys[id].addfalse(lines[5])

rounds = 10000 
modulo = prod([monkey.test for monkey in monkeys])

for round in range(rounds):
    for monkey in monkeys:
        for item in monkey.items:
            old = item
            new = eval(monkey.operation) % modulo
            if new % monkey.test == 0:
                monkeys[monkey.true].items.append(new)
            else:
                monkeys[monkey.false].items.append(new)
        monkey.countitems()
        monkey.items.clear()

monkeycounts = [monkey.count for monkey in monkeys]
monkeycounts.sort()
monkeybusiness = prod(monkeycounts[-2:])

print("The level of monkey business after {} rounds is {}".format(rounds, monkeybusiness))

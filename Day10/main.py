with open("Day10\input.txt") as file:
    lines = file.read().strip().split("\n")

signals = [1]

def nextinstr(lines, curinstr):
    instr = lines[curinstr]
    if instr.startswith("addx"):
        _, num = instr.split()
        return int(num)
    else:
        return None

signalstr = []

curinstr, instr = 0, 0
registers = [1]
for cycle in range(2,241):
    if instr:
        register = instr + registers[-1]
        instr = None
    else:
        instr = nextinstr(lines, curinstr)
        curinstr += 1
        register = registers[-1]
    registers.append(register)
    if (cycle - 20) % 40 == 0: signalstr.append(cycle * register)

print("The answer to Part 1 is", sum(signalstr))
    
prtsc = ""
for cycle, register in enumerate(registers, 1):
    if register - 1 <= (cycle-1) % 40 <= register + 1:
        prtsc += "#"
    else:
        prtsc += "."
    if cycle % 40 == 0: prtsc += "\n"

print("The printed screen is:")
print(prtsc)

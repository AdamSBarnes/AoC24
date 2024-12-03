with open("./data/_old/2022/05.txt", "r") as f:
    lines = f.read()

stacks = [l.replace("["," ").replace("]"," ")[1:] for l in lines.split("\n")][0:8]
instructions = [(x[1],x[3],x[5]) for x in [m.split(" ") for m in lines.split("\n")][10:]]

l = [[] for _ in range(1 + max([len(c.replace(" ","")) for c in stacks]))]

for stack in stacks:
    for idx, c in enumerate(stack):
        if c != ' ':
            pos = int(idx / 4) + 1
            l[pos] = [c,] + l[pos]


for moves, froms, tos in instructions:
    for mv in range(int(moves)):
        box = l[int(froms)][-1]
        l[int(froms)] = l[int(froms)][0:-1]
        l[int(tos)].append(box)


"".join([x[-1] for x in l[1:]])


#p2
for idx, val in enumerate(instructions):
    moves, froms, tos = val
    box = l[int(froms)][-int(moves):]
    l[int(froms)] = l[int(froms)][0:-int(moves)]
    l[int(tos)] += box

"".join([x[-1] for x in l[1:]])

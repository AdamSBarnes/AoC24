with open("./data/_old/2022/01.txt", "r") as f:
    lines = f.read()

data = lines.split("\n")

out = []

runtotal = 0
for d in data:
    if d == '':
        out.append(runtotal)
        runtotal = 0
        continue
    runtotal += int(d)

max(out)

sum(sorted(out)[-3:])
with open("./data/_old/2022/03.txt", "r") as f:
    lines = f.read()

data = lines.split("\n")
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = f"_{letters.lower()}{letters}"

# p1
tot = 0
for d in data:
    p1, p2 = d[0:int(len(d) / 2)], d[int(len(d) / 2):]

    in_both = list(set([p for p in p1 if p in p2]))
    score = [letters.find(p) for p in in_both]
    tot += sum(score)


#p2
i = 0
p = []
while True:
    try:
        g1, g2, g3 = data[i:i + 3]
    except ValueError:
        break
    common = [l for l in g1 if l in g2 and l in g3][0]
    p.append(letters.find(common))
    i += 3

sum(p)

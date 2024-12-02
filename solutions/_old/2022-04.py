with open("./data/_old/2022/04.txt", "r") as f:
    lines = f.read()

data = [l.split(",") for l in lines.split("\n")]


def spl(l):
    l1, l2 = l
    a1, a2 = l1.split("-")
    b1, b2 = l2.split("-")
    return [(int(a1), int(a2)), (int(b1), int(b2))]


clean = [spl(d) for d in data]

out = []
for c in clean:
    min1, max1 = c[0]
    min2, max2 = c[1]

    if min1 >= min2 and max1 <= max2:
        out.append(c)
        continue

    if min2 >= min1 and max2 <= max1:
        out.append(c)

len(out)

## p2
def is_overlap(min1, max1, min2, max2):
    r1 = [i for i in range(min1, max1 + 1)]
    r2 = [i for i in range(min2, max2 + 1)]
    for r in r1:
        if r in r2:
            return 1
    for rr in r2:
        if rr in r1:
            return 1
    return 0

### 
def is_overlap(min1, max1, min2, max2):
    return not (max1 < min2 or max2 < min1)

cnt = 0
for c in clean:
    min1, max1 = c[0]
    min2, max2 = c[1]
    cnt += is_overlap(min1, max1, min2, max2)


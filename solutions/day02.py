with open("./data/02.txt", "r") as f:
    data = f.read()

clean = [[int(i) for i in d.split(" ")] for d in data.split("\n")]

def cl(ll):
    gaps = []
    for idx,l in enumerate(ll):
        try:
            gaps.append(l - ll[idx + 1])
        except Exception:
            continue
    if max([abs(g) for g in gaps]) > 3:
        return 0

    if 0 in gaps:
        return 0

    signs = [c > 0 for c in gaps]

    if all(signs) or all([not(s) for s in signs]):
        return 1

    return 0

sum([cl(c) for c in clean])

#p2
def check_removals(c):
    for i in range(len(c)):
        nc = c.copy()
        nc.pop(i)
        print(nc)
        if cl(nc) == 1:
            return 1
    return 0


runtot = 0
for c in clean:
    print(c)
    if cl(c) == 1:
        runtot += 1
        continue
    runtot += check_removals(c)






sample = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

with open("./data/05.txt", "r") as f:
    lines = f.read()

a = [s.split("|") for s in lines.split("\n") if "|" in s]
a = [[int(x) for x in xx] for xx in a]

b = [s.split(",") for s in lines.split("\n") if "," in s]
b = [[int(x) for x in xx] for xx in b]


def check_bk(bk):
    for idx, pg in enumerate(bk):
        for od in a:
            if pg in od:
                if od[0] == pg:
                    other = od[1]
                    try:
                        other_idx = bk.index(other)
                        if idx > other_idx:
                            return False
                    except ValueError:
                        continue
                elif od[0] == pg:
                    other = od[0]
                    try:
                        other_idx = bk.index(other)
                        if idx < other_idx:
                            return False
                    except ValueError:
                        continue
    return True

rt = 0
for bk in b:
    if check_bk(bk):
        middle = bk[int((len(bk) / 2))]
        print(middle)
        rt += middle

#p2
bad_bk = [bk for bk in b if not check_bk(bk)]

def switch_bk(bk):
    for idx, pg in enumerate(bk):
        for od in a:
            if pg in od:
                if od[0] == pg:
                    other = od[1]
                    try:
                        other_idx = bk.index(other)
                        if idx > other_idx:
                            bk[idx] = other
                            bk[other_idx] = pg
                            return bk
                    except ValueError:
                        continue
                elif od[0] == pg:
                    other = od[0]
                    try:
                        other_idx = bk.index(other)
                        if idx < other_idx:
                            bk[idx] = other
                            bk[other_idx] = pg
                            return bk
                    except ValueError:
                        continue
    return bk


ob = []
for bb in bad_bk:
    while not check_bk(bb):
        bb = switch_bk(bb)
    ob.append(bb)

rt = 0
for bk in ob:
    if check_bk(bk):
        middle = bk[int((len(bk) / 2))]
        print(middle)
        rt += middle



from itertools import chain

sample = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

with open("./data/04.txt", "r") as f:
    lines = f.read()

data = [l for l in lines.split("\n")]


# vals = []


def traverse(x, y):
    def _run(x, y, _h, _v):
        run = data[x][y]
        _x = x
        _y = y

        while len(run) < 4:
            _x = _x + _h
            _y = _y + _v

            if _x < 0 or _y < 0:
                return None

            try:
                val = data[_x][_y]
            except IndexError:
                return None

            run = f"{run}{val}"
        return run

    h = [0, -1, 1]
    v = [0, -1, 1]

    collected = []
    for _h in h:
        for _v in v:
            if _h == _v == 0:
                continue
            ran = _run(x, y, _h, _v)
            if ran:
                collected.append(ran)

    return collected


out = []

for h in range(len(data[0])):
    for v in range(len(data)):
        if data[h][v] == "X":
            out.append(traverse(h, v))

out = list(chain(*out))

len([x for x in out if x == "XMAS"])


# p2
from collections import Counter

with open("./data/04.txt", "r") as f:
    lines = f.read()

data = [l for l in lines.split("\n")]

buf = "".join(["." for _ in range(len(data[0]) + 2)])
wide = ["." + l + "." for l in data]
data = [buf,] + wide + [buf,]

out = []


for h in range(len(data[1])):
    for v in range(len(data)):
        surrounds = []
        if data[h][v] == "A":
            for _h in [1, -1]:
                for _v in [1, -1]:
                    _x, _y = h + _h, v + _v
                    val = data[_x][_y]
                    surrounds.append(val)

        if surrounds:
            counter = Counter(surrounds)
            if counter['S'] == 2 and counter['M'] == 2:
                out.append([h,v, surrounds])

len([o for o in out if not o[2][0] == o[2][3]])

#(1,1), (1,-1), (-1,1), (-1,-1)
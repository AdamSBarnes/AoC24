def rps(t1, t2):
    results = {
        'A': {'X': 3, 'Y': 6, 'Z': 0},
        'B': {'X': 0, 'Y': 3, 'Z': 6},
        'C': {'X': 6, 'Y': 0, 'Z': 3}
    }

    move = {'X': 1, 'Y': 2, 'Z': 3}

    return results.get(t1).get(t2) + move.get(t2)


with open("./data/_old/2022/02.txt", "r") as f:
    lines = f.read()

data = [a.split() for a in lines.split("\n")]

sum([rps(*d) for d in data])



def rps2(t1, r):
    results = {
        'A': {'X': 3, 'Y': 6, 'Z': 0},
        'B': {'X': 0, 'Y': 3, 'Z': 6},
        'C': {'X': 6, 'Y': 0, 'Z': 3}
    }
    inv_move = {'X': 0, 'Y': 3, 'Z': 6}

    t2 = [k for k,v in results.get(t1).items() if v == inv_move.get(r)][0]

    return rps(t1,t2)

sum([rps2(*d) for d in data])

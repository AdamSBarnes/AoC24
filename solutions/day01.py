with open("./data/01/p1.txt", "r") as f:
    data = f.read()

clean = [(int(d.split(" ")[0]),int(d.split(" ")[-1]))  for d in data.split("\n")]

arr0, arr1 = [c[0] for c in clean], [c[1] for c in clean]

arr0.sort()
arr1.sort()

total = 0
for idx, val in enumerate(arr0):
    diff = abs(val - arr1[idx])
    total += diff

# p2
tot_two = 0
for idx, val in enumerate(arr0):
    matches = len([a for a in arr1 if a == val])
    tot_two += val * matches


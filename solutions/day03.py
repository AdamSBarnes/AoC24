
with open("./data/03.txt", "r") as f:
    data = f.read()

clean = [l for l in data.split("mul(")]

valid = []
runtot = 0
for m in clean:
    if ")" not in m:
        continue
    sm = m[0:m.find(")")]

    try:
        n1, n2 = sm.split(",")
    except ValueError:
        continue
    if n1.isnumeric() and n2.isnumeric():
        valid.append((n1,n2))
        runtot += int(n1) * int(n2)


#p2
clean = [f"mul({l}" for l in data.split("mul(")]

runtot = 0
enabled = True
for idx, m in enumerate(clean):

    if ")" not in m:
        n1, n2 = "0", "0"
    else :
        sm = m[4:m.find(")")]

        try:
            n1, n2 = sm.split(",")
        except ValueError:
            n1, n2 = "0", "0"

    if n1.isnumeric() and n2.isnumeric() and enabled:
        runtot += int(n1) * int(n2)

    dont = m.rfind("don't()")
    do = m.rfind("do()")

    if dont > do and dont > 0:
        enabled = False

    if do > dont and do > 0:
        enabled = True
inputs = open("inputsday1.txt", "r")

xs = []
for z in inputs.readlines():
    xs.append([z])

ys = []

for x in xs:
    y = []
    for c1 in x:
        for c2 in c1:
            if c2.isdigit():
                y.append(int(c2))

    ys.append(y)


finals = []
for m in ys:
    finals.append(int(str(m[0]) + str(m[-1])))

counter = 0
for f in finals:
    counter += f
print(counter)

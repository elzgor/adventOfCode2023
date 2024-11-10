import re

inputs = open("inputsday2.txt", "r")

xs = []
for z in inputs.readlines():
    xs.append(z.split(":"))
ys = 0
powers = 0
for x in xs:
    caniadd = True
    x[0] = int(re.sub("[Game ]","",x[0]))
    x[1] = x[1].split(";")
    minimums = [0,0,0] # red green blue
    for combo in x[1]:
        combo1 = combo.split(",")

        for specific in combo1:
            val = sum(int(a) for a in re.findall(r'\d+', specific))
            if (("red" in specific) and (val > minimums[0])):
                minimums[0] = val
            if (("green" in specific) and (val > minimums[1])):
                minimums[1] = val
            if (("blue" in specific) and (val > minimums[2])):
                minimums[2] = val

    power = minimums[0] * minimums[1] * minimums[2]
    powers += power

print(powers)

import re

inputs = open("inputsday2.txt", "r")

xs = []
for z in inputs.readlines():
    xs.append(z.split(":"))
ys = 0

for x in xs:
    caniadd = True
    x[0] = int(re.sub("[Game ]","",x[0]))
    x[1] = x[1].split(";")

    for combo in x[1]:
        combo1 = combo.split(",")
        
        while caniadd == True:
            for specific in combo1:
                val = sum(int(a) for a in re.findall(r'\d+', specific))
                
                if (("red" in specific) and (val > 12)) or (("green" in specific) and (val > 13)) or (("blue" in specific) and (val > 14)):
                    caniadd = False
                    
            break
        
    if caniadd == True:
        ys += x[0]
        print(ys)

print(ys)
# 2176
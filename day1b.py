def First(word):
    for i in range(0, (len(word)) ,1):
        if (word[i] == 'o' and word[i+1] == 'n' and word[i+2] == 'e') or word[i] == '1':
            return(int(str(1) + str(Second(word[::-1]))))
        if (word[i] == 't' and word[i+1] == 'w' and word[i+2] == 'o') or word[i] == '2':
            return(int(str(2) + str(Second(word[::-1]))))
        if (word[i] == 't' and word[i+1] == 'h' and word[i+2] == 'r' and word[i+3] == 'e' and word[i+4] == 'e') or word[i] == '3':
            return(int(str(3) + str(Second(word[::-1]))))
        if (word[i] == 'f' and word[i+1] == 'o' and word[i+2] == 'u' and word[i+3] == 'r') or word[i] == '4':
            return(int(str(4) + str(Second(word[::-1]))))
        if (word[i] == 'f' and word[i+1] == 'i' and word[i+2] == 'v' and word[i+3] == 'e') or word[i] == '5':
            return(int(str(5) + str(Second(word[::-1]))))
        if (word[i] == 's' and word[i+1] == 'i' and word[i+2] == 'x') or word[i] == '6':
            return(int(str(6) + str(Second(word[::-1]))))
        if (word[i] == 's' and word[i+1] == 'e' and word[i+2] == 'v' and word[i+3] == 'e' and word[i+4] == 'n') or word[i] == '7':
            return(int(str(7) + str(Second(word[::-1]))))
        if (word[i] == 'e' and word[i+1] == 'i' and word[i+2] == 'g' and word[i+3] == 'h' and word[i+4] == 't') or word[i] == '8':
            return(int(str(8) + str(Second(word[::-1]))))
        if (word[i] == 'n' and word[i+1] == 'i' and word[i+2] == 'n' and word[i+3] == 'e') or word[i] == '9':
            return(int(str(9) + str(Second(word[::-1]))))
        
def Second(word):
    for i in range(0, (len(word)) ,1):
        if (word[i] == 'e' and word[i+1] == 'n' and word[i+2] == 'o') or word[i] == '1':
            return(1)
        if (word[i] == 'o' and word[i+1] == 'w' and word[i+2] == 't') or word[i] == '2':
            return(2)
        if (word[i] == 'e' and word[i+1] == 'e' and word[i+2] == 'r' and word[i+3] == 'h' and word[i+4] == 't') or word[i] == '3':
            return(3)
        if (word[i] == 'r' and word[i+1] == 'u' and word[i+2] == 'o' and word[i+3] == 'f') or word[i] == '4':
            return(4)
        if (word[i] == 'e' and word[i+1] == 'v' and word[i+2] == 'i' and word[i+3] == 'f') or word[i] == '5':
            return(5)
        if (word[i] == 'x' and word[i+1] == 'i' and word[i+2] == 's') or word[i] == '6':
            return(6)
        if (word[i] == 'n' and word[i+1] == 'e' and word[i+2] == 'v' and word[i+3] == 'e' and word[i+4] == 's') or word[i] == '7':
            return(7)
        if (word[i] == 't' and word[i+1] == 'h' and word[i+2] == 'g' and word[i+3] == 'i' and word[i+4] == 'e') or word[i] == '8':
            return(8)
        if (word[i] == 'e' and word[i+1] == 'n' and word[i+2] == 'i' and word[i+3] == 'n') or word[i] == '9':
            return(9)         

inputs = open("inputsday1.txt", "r")

xs = []
for z in inputs.readlines():
    xs.append(z)

counter = 1
toBeAdded = []

for x in xs:
    toBeAdded.append(First(x))
    
print(sum(toBeAdded))

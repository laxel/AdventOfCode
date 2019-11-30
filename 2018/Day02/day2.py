# Part 1
lines = open("input.txt").read().splitlines()

num2 = 0
num3 = 0
for line in lines:
    d = dict()
    for char in line:
        if not char in d.keys():
            d[char] = 1
        else:
            d[char] += 1

    if 2 in d.values():
        num2 += 1
    if 3 in d.values():
        num3 += 1

print("Part 1:")
print(str(num2) + " * " +str(num3) + " = " + str(num2*num3))

# Part 2
l = list()
for line in lines:
    l.append(line)

for currI in range(0, len(l)):
    for nextI in range(currI+1, len(l)):
        diff = 0
        word1 = l[currI]
        word2 = l[nextI]
        for i in range(0, len(word1)):
            if(word1[i] != word2[i]):
                diff += 1
            #if diff > 1:
             #   break
        if diff < 1:
            print(str(currI) + " " + str(nextI))
#        print(diff)








#        for char in l[currIndex]:
#            print(char + " " + l[n])
#            if not char in l[n]:
#                diff += 1
#                print(char + " <--")
#        #if diff < 2:
#        print(str(currIndex) + " " + str(n))
#        print(diff)
#        #print(diff)
        
                
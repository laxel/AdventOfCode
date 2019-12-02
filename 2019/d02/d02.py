f = open("input.txt")
l = [int(x) for x in f.read().split(",")]

def foo(l, noun, verb):
	l[1] = noun
	l[2] = verb
	i = 0
	while l[i] != 99:
		l[l[i+3]] = l[l[i+1]]+l[l[i+2]] if l[i] == 1 else l[l[i+1]]*l[l[i+2]]
		i += 4
	return l[0]

# --- Part 1 ---
print("Part 1:",foo(l.copy(),12,1))

# --- Part 2 ---
for n in range(0,100):
	for v in range(0,100):
		if foo(l.copy(),n,v) == 19690720:
			print("Part 2:",100*n+v)
			break

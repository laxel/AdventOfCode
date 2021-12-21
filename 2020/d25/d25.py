RFIDS = [17773298, 15530095] #Input
v = 1
i = 0
fnd = [0,0] #[4347326, 14611728]
while fnd[0] == 0 or fnd[1] == 0:
    v *= 7
    v %= 20201227
    i += 1
    if v == RFIDS[0]: fnd[0] = i
    if v == RFIDS[1]: fnd[1] = i

print(fnd)
v = 1
for _ in range(fnd[0]):
    v *= RFIDS[1]
    v %= 20201227

print(v)

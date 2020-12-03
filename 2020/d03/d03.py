f = open("input.txt")

map = []
# Build map
for l in f:
    map.append([c for c in l if c in ['.','#']])

# Function that traverses through the map and return num trees hit
def foo(d_right, d_down):
    result = 0
    x, y = [0,0]
    width = len(map[0])
    height = len(map)
    while y < height:
        if map[y][x] == '#':
            result += 1
        x += d_right if x + d_right < width else  d_right - width
        y += d_down
    return result

print("/P1/ Number of trees " + str(foo(3,1)))

P2_result = foo(1,1) * foo(3,1) * foo(5,1) * foo(7,1) * foo(1,2)
print("/P2/ Number of trees " + str(P2_result))

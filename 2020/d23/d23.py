# Linked list class
class Node:
    def __init__(self, v, n):
        self.v = v
        self.n = n
    def __repr__(self):
        return str(self.v)

def crab_cups(l, iterations):
    curr = l[0]
    num = len(l)
    for _ in range(iterations):
        # Get pointers & values to next 3 nodes
        n1 = curr.n
        n3 = n1.n.n
        n4 = n3.n
        rmvd = [n1.v, curr.n.n.v, n3.v]
        # Update pointers for current
        curr.n = n4
        # Find destination
        n = curr.v
        dest = None
        while True:
            n -= 1
            if n == 0:
                n = num
            if n not in rmvd:
                dest = d[n]
                break
        # Assign updated pointers
        destn1 = dest.n
        dest.n = n1
        n3.n = destn1
        # Update current node
        curr = curr.n

def node_print(start,d,r):
    c = d[start]
    for _ in range(r):
        print(str(c.v) + " ",end='')
        c = c.n
    print()

inp = "215694783"
# === Part 1 ===
d = dict()
node_l = [Node(int(c),None) for c in inp]
for i in range(len(node_l)):
    d[node_l[i].v] = node_l[i]
    node_l[i].n = node_l[(i+1) % len(node_l)]

crab_cups(node_l,100)

c = d[1]
res = ''
for _ in range(8):
    c = c.n
    res += str(c.v)
print("/P1/ Order starting from one: " + res)

# === Part 2 ===
print("Takes a couple of seconds (aprx. 20 on my machine)")
d = dict()
node_l = [Node(int(c),None) for c in inp]
for i in range(10,1000001):
    node_l.append(Node(i,None))

for i in range(len(node_l)):
    d[node_l[i].v] = node_l[i]
    node_l[i].n = node_l[(i+1) % len(node_l)]

crab_cups(node_l,10000000)

c = d[1]
fs = c.n.v
sn = c.n.n.v
print("/P2/ Values after 1: "+str(fs)+" * "+str(sn)+" = "+str(fs*sn))
f = open("input.txt")

d = dict()
# Parse data & store data in dict
for l in f:
    f_bag, snd_half = l.split(" contain ")
    c_split = snd_half.split(", ")
    c_split[len(c_split)-1] = c_split[len(c_split)-1][:-2] # Remove .\n
    f_bag = f_bag[:-1] # Remove ending 's'
    c_split = [x[:-1] if x[-1:] == 's' else x  for x in c_split] # Remove ending 's'

    if c_split[0] == "no other bag":
        d[f_bag] = None
    else:
        d[f_bag] = [ [x[0:1], x[2:]] for x in c_split ]
    

# Recursive dict search function
def p1_search(current_tag, search_tag):
    # Match hit
    if current_tag == search_tag:
        return True
    
    # Recursivly serach down
    l = d[current_tag]
    if l == None:
        return False
    return any( [p1_search(x[1], search_tag) for x in l] )
   

# Check if each bag type can containe 'shiny gold'
t = "shiny gold bag"
p1_result = 0
for k in d:
    if k == t:
        continue
    if p1_search(k, t):
        p1_result += 1

print("/P1/ Number of bags that can contain one shiny: " + str(p1_result))

# Recursive dict search function
def p2_search(tag):
    # Recursivly serach down
    l = d[tag]
    if l == None:
        return 0
    return  sum( [int(x[0]) + int(x[0]) * p2_search(x[1]) for x in l] )

p2_results = p2_search(t)
print("/P2/ Shiny bag # of containing bags: " + str(p2_results))
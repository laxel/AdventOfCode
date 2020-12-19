import itertools

# === Parsing ===
f = open("input.txt")
ls = [l[:-1] if l[-1] == "\n" else l for l in f if l != "\n"]

d = dict()
mgs = []
for l in ls:
    fs = l.split(": ")
    if len(fs) == 1:
        mgs.append(l)
    else:
        k = int(fs[0])
        ss = fs[1].split(" | ")
        if len(ss) == 1:
            if ss[0][0] == '"':
                d[k] = ss[0][1]
            else:
                d[k] = [list(map(lambda x: int(x), ss[0].split(" ")))]
        else:
            d[k] = [list(map(lambda x: int(x), ss[0].split(" "))), \
                    list(map(lambda x: int(x), ss[1].split(" ")))]

# === Functions
# Creates a traversel list to be used when testing a msg
# m_d: max depth the list will be, -1 = no limit
def get_traverse_list(m_d):
    return _check_key(0, m_d, 0)

def _check_key(k, m_d, c_d):
    c_d += 1
    if m_d != -1 and c_d > m_d:
        return 'c' # Will never match

    vs = d[k]
    if type(vs) is str:
        return vs
    elif len(vs) == 1:
        a = vs[0]
        answ_a = list(map(lambda x: _check_key(x, m_d, c_d),  a))
        return [answ_a]
    else:
        a = vs[0]
        b = vs[1]
        answ_a = list(map(lambda x: _check_key(x, m_d, c_d),  a))
        answ_b = list(map(lambda x: _check_key(x, m_d, c_d),  b))
        return [answ_a, answ_b]

# Traverse throught the travers list and check if msg is correct
def traverse(t,answ):
    b, i = _traverse(t,answ,0)
    return b and i == len(answ)

def _traverse(t, answ, i):
    # "c"
    if type(t) is str: 
        
        if 0 <= i < len(answ):
            return [answ[i] == t, i+1]
        else:
            return [False, i+1]
    # [a]
    elif len(t) == 1: 
        for st in t[0]:
            b, i = _traverse(st, answ, i)
            if not b:
                return [False,i]
        return [True,i]
    # [[a] | [b]]
    else:
        j = i
        did_break = False
        for st in t[0]:
            b, j = _traverse(st, answ, j)
            if not b:
                did_break = True
                break
        if not did_break:
            return [True, j]
        for st in t[1]:
            b, i = _traverse(st, answ, i)
            if not b:
                return [False,i]
        return [True,i]
    return [True, i]

def create_all_poss(t):
    r

# === Part 1 ===
trav = get_traverse_list(-1)

num_hit = 0
for m in mgs:
    if traverse(trav, m):
        num_hit += 1
print("/P1/ Messages that match: " + str(num_hit))

# === Part 2 ===
d[8] = [[42],[42,8]]
d[11] = [[42,31],[42,11,31]]

# Max depth needs to be adjusted depending on the input,
trav = get_traverse_list(25) # <=========

num_hit = 0
for m in mgs:
    if traverse(trav, m):
        num_hit += 1
print("/P2/ Messages that match: " + str(num_hit))

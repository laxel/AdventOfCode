import re

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

# === Create regex expression ===
# k: key to check
# m_d: max depth (-1 -> no depth limit)
def check_key(k, m_d):
    return _check_key(k,m_d,0)

def _check_key(k,m_d,c_d):
    c_d += 1
    if m_d != -1 and c_d > m_d:
        return 'c' # Will never match

    vs = d[k]
    if type(vs) is str:
        return vs
    elif len(vs) == 1:
        return "(" + "".join(list(map(lambda x: "(" + _check_key(x, m_d, c_d) + ")",  vs[0]))) + ")"
    else:
        a_s = "".join(list(map(lambda x: "(" + _check_key(x, m_d, c_d) + ")",  vs[0])))
        b_s = "".join(list(map(lambda x: "(" + _check_key(x, m_d, c_d) + ")",  vs[1])))
        return "(" + a_s + "|" + b_s + ")"

re_exp = "^" + check_key(0,-1) + "$"
p1_match = 0
for m in mgs:
    if re.match(re_exp, m):
        p1_match += 1
print("/P1/ Messages that match: " + str(p1_match))

# === Part 2 ===
d[8] = [[42],[42,8]]
d[11] = [[42,31],[42,11,31]]

# Depth of 15 was enought for me, might vary slightly for different inputs
re_exp = "^" + check_key(0,15) + "$"
p2_match = 0
for m in mgs:
    if re.match(re_exp, m):
        p2_match += 1
print("/P2/ Messages that match: " + str(p2_match))

import re

f = open("input.txt")

def to_36_bit(num):
    v = bin(num)[2:]
    return [c for c in (36 - len(v)) * '0' + v]

def from_36_bit(val):
    s = 0
    for k in range(36):
        s += 2**k * int(val[35-k])
    return s


def p1_mask_func(mask, num):
    l_num = to_36_bit(num)
    l_mask = [c for c in mask]
    l_res = []
    for i in range(len(l_num)):
        n = l_num[i]
        m = l_mask[i]
        if m == 'X':
            l_res.append(n)
        else:
            l_res.append(m)
    return l_res

def p2_mask_func(mask, addr):
    l_mask = [c for c in mask]
    l_addr = to_36_bit(addr)
    addrs = []
    x_num = len([x for x in l_mask if x == 'X'])
    x_vals = [(x_num - len(bin(x)[2:])) * '0' + bin(x)[2:] for x in range(2**x_num)]
    for vals in x_vals:
        l_res = []
        v_i = 0
        for i in range(len(l_mask)):
            m = l_mask[i]
            a = l_addr[i]
            if m == '0':
                l_res.append(a)
            elif m == '1':
                l_res.append('1')
            else:
                l_res.append(vals[v_i])
                v_i += 1
        addrs.append(from_36_bit(l_res))
    return addrs

    

p1_d = dict()
p2_d = dict()
mask = []
for l in f:
    # --- part 1 ---
    m_obj = re.match("(mem|mask)(\[(\d+)\])? = (\w+)", l)
    if m_obj.group(1) == 'mask':
        mask = m_obj.group(4)
    else:
        a = m_obj.group(3)
        v = int(m_obj.group(4))
        p1_d[a] = from_36_bit(p1_mask_func(mask, v))
        # --- part 2 ---
        addrs = p2_mask_func(mask, int(a))
        for addr in addrs:
            p2_d[addr] = v

p1_res = 0
for k in p1_d:
    p1_res += p1_d[k]

print("/P1/ Sum of all values: " + str(p1_res))

p2_res = 0
for k in p2_d:
    p2_res += p2_d[k]

print("/P2/ Sum of all values: " + str(p2_res))

def eval(exp):
    c = 0
    n_op = 0
    i = 0
    while i < len(exp):
        e = exp[i]
        if e == "(":
            j = 0
            b_count = 1 
            while b_count != 0:
                j += 1
                e = exp[i+j]
                if e == "(":
                    b_count += 1
                elif e == ")":
                    b_count -= 1
            val = eval(exp[i+1:i+j])
            c = c + val if n_op == 0 else c * val
            i += j

        elif e == "+":
            n_op = 0
        elif e == "*":
            n_op = 1
        else:
            c = c + int(e) if n_op == 0 else c * int(e) 
       
        i += 1
    return c

def insert_para_add(exp):
    i = 0
    while i < len(exp):
        if exp[i] == "+":
            l = exp[i-1]
            r = exp[i+1]
            if l == ")":
                b_count = 1
                j = -1
                while b_count != 0:
                    j -= 1
                    if exp[i+j] == ")":
                        b_count += 1
                    elif exp[i+j] == "(":
                        b_count -= 1
                exp.insert(i+j,"(")
            else:
                exp.insert(i-1,"(")
            
            if r == "(":
                b_count = 1
                j = 2
                while b_count != 0:
                    j += 1
                    if exp[i+j] == "(":
                        b_count += 1
                    elif exp[i+j] == ")":
                        b_count -= 1
                exp.insert(i+j,")")
            else:
                exp.insert(i+3,")")
            
            i += 2
        i += 1
    return exp

f = open("input.txt")

p1_res = 0
p2_res = 0
for l in f:
    exp = [c for c in l if c not in [" ", "\n"]]
    p1_res += eval(exp)
    p2_res += eval(insert_para_add(exp))

print("/P1/ Sum of all expresions: " +str(p1_res))
print("/P2/ Sum of all expresions: " +str(p2_res))
            
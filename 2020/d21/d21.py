import re

f = open("input.txt")

may_c = dict()
all_ing = set()
all_als = set()
org_ing_l = []

for l in f:
    m = re.match("^((\\w+ ?)+)\\(contains ((\\w+,? ?)+)\\)$",l)
    als = m.group(3).split(", ")
    ings = m.group(1)[:-1].split(" ")
    [all_ing.add(x) for x in ings]
    [all_als.add(x) for x in als]
    org_ing_l.append(ings)
    for al in als:
        if al not in may_c:
            may_c[al] = []
        
        s = set()
        [s.add(x) for x in ings]
        may_c[al] .append(s)


def remove_ing_occurenses(d, ing):
    for k in d:
        l = d[k]
        for s in l:
            if ing in s:
                s.remove(ing)


asgnd_als = dict()
asgnd_ings = set()

has_changed = True
while has_changed:
    has_changed = False
    for al in may_c:
        if al in asgnd_als:
            continue
        l = may_c[al]
        res = l[0]
        for i in range(1,len(l)):
            res = res.intersection(l[i])
        if len(res) == 1:
            ing = res.pop()
            remove_ing_occurenses(may_c,ing)
            asgnd_ings.add(ing)
            asgnd_als[al] = ing
            has_changed = True

no_al = all_ing.difference(asgnd_ings)

p1_res = 0
for l in org_ing_l:
    for ing in l:
        if ing in no_al:
            p1_res += 1
print("/P1/ Num occurenses of 'safe' ingrediences: " + str(p1_res))

keys = list(asgnd_als.keys())
keys.sort()

p2_res = ""
for k in keys:
    ing = asgnd_als[k]
    p2_res += ing + ","
print("/P2/ Ingr. sorted by alphabetical alle. order:")
print(p2_res[:-1])
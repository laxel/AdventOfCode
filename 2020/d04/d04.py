import re

f = open("input.txt")

# Store input nicely in a list
passports = []
currentString = ""
for l in f:
    if l == "\n":
        passports.append(currentString)
        currentString = ""
    else:
        currentString += l[:-1] if currentString == "" else " " + l[:-1]
passports.append(currentString)

#  
numValid = 0
numPresent = 0
for p in passports:
    present = [False] * 7
    valid = [False] * 7

    fields = [x.split(":") for x in p.split(" ")]
    for t in fields:
        key, val = t
        if key == "byr":
            present[0] = True
            valid[0] = 1920 <= int(val) <= 2002
        elif key == "iyr":
            present[1] = True
            valid[1] = 2010 <= int(val) <= 2020
        elif key == "eyr":
            present[2] = True
            valid[2] = 2020 <= int(val) <= 2030
        elif key == "hgt":
            present[3] = True
            if re.match("^\d+cm",val):
                valid[3] = 150 <= int(val.split("cm")[0]) <= 193
            elif re.match("^\d+in",val):
                valid[3] = 59 <= int(val.split("in")[0]) <= 76
        elif key == "hcl":
            present[4] = True
            valid[4] = bool(re.match("^#[0-9a-f]{6}",val))
        elif key == "ecl":
            present[5] = True
            valid[5] = val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        elif key == "pid":
            present[6] = True
            valid[6] = bool(re.match("^\d{9}",val))

    if all(present):
        numPresent += 1
    if all(valid):
        numValid += 1
            

print("/P1/ Number of present fields: " + str(numPresent))
print("/P2/ Number of valid passport: " + str(numValid))

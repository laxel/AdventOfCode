f = open("input.txt")

p1_valid = 0
p2_valid = 0
for l in f:
    # Split line on whitespace
    w_list = l.split()
    # Get limits
    limits = w_list[0].split("-")
    lower = int(limits[0])
    upper = int(limits[1])
    # Get letter
    letter = w_list[1].split(":")[0]
    # Get password
    password = w_list[2]

    # --- Part 1 ---
    num_mentions = len([c for c in password if c == letter])

    if num_mentions >= lower and num_mentions <= upper:
        p1_valid += 1

    # --- Part 2 ---
    l_check = password[lower - 1] == letter
    u_check = password[upper - 1] == letter
    if (l_check or u_check) and not (l_check and u_check): 
        p2_valid += 1

print("/P1/ Number of valid passwords: " + str(p1_valid))
print("/P2/ Number of valid passwords: " + str(p2_valid))








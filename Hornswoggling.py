

#
# Hornswoggling swordsman
#
# One hundred people stand in a circle in order, numbered 1 to 100. No. 1 has a sword. He kills 
# the next person (i.e. No. 2) and gives the sword to the next living person (i.e. No. 3). All
# people do the same until only 1 participant survives. Which number survives to the end?
#
p = [i for i in range(1, 101)]
# mod is 0 or 1 and signifies if we kill starting with the second or first element respectively
mod = len(p) % 2
while (len(p) > 1):
    print("list length:", len(p))
    print("modulus, kill even (mod 0) or odd (mod 1) elements:", mod)
    print("elements:", p)
    print("-----")
    p2 = [r for (i, r) in enumerate(p) if i % 2 == mod]
    # new mod is going to depend on if we started killing the first or second element, and 
    # if the length of the array was even or odd.
    mod = (len(p) + mod) % 2 
    p = p2


print("last sordsperson standing:")
print(p[0])

# Answer is 37

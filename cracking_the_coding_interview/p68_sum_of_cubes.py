#
# pg 68 - find all a,b,c,d in [1,1000] such that a^3 + b^3 = c^3 + d^3
#
import math


# naive brute force O(n^4)
def naive(n=1000):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n, +1):
                for d in range(1, n + 1):
                    if a**3 + b**3 == c**3 + d**3:
                        print(a, b, c, d)


# Avoid duplicated work:
#  1. pre-compute and cache a**3, b**3,
#  2. directly compute d from a,b,c
#  3. only check values of c for which a**3 + b**3 - c**3 > 0
# O(n^3)
def better(n=1000):
    e = 1/3
    for a in range(1, n + 1):
        a3 = a**3
        for b in range(1, n + 1):
            b3 = b**3
            ab = a3 + b3
            for c in range(1, n + 1):
                d3 = ab - c**3
                if (d3 < 1):
                    break
                d = math.ceil(math.pow(d3, e))
                if d > 0 and d <= n and ab == c**3 + d**3:
                    print(a, b, c, d)


# Same as better() but also use symmetry to only check values such
# that a <= b, using the fact that if (a,b,c,d) is a solution, then
# (b,a,c,d) is also a solution.  Likewise any soltion of the from
# (a,b,c,d) -> (a,b,d,c) is also a slotion.  by breaking from our
# loops whenever b > a and c > d, less work is duplicated.
# O(n^3)
def better_symmetry(n=1000):
    e = 1/3
    for a in range(1, n + 1):
        a3 = a**3
        for b in range(1, n + 1):
            if (b > a):
                # use symmetry of solutions (a,b,c,d) -> (b,a,c,d)
                break
            b3 = b**3
            ab = a3 + b3
            for c in range(1, n + 1):
                c3 = c**3
                d3 = ab - c3
                if (d3 < 1):
                    # no real integer solutions for d if d^3 < 1
                    break
                d = math.ceil(math.pow(d3, e))
                if (c > d):
                    # use symmetry, (a,b,c,d) -> (a,b,d,c)
                    break
                if d > 0 and d <= n and ab == c3 + d**3:
                    print(a, b, c, d)
                    if (b != a):
                        print(b, a, c, d)
                    if (d != c):
                        print(a, b, d, c)
                        if (b != a):
                            print(b, a, d, c)


# Cracking the Coding Interview book points out that we can just
# compute all the a^3 + b^3 combinations and note the pairs that add
# up to the same sum. We now have a list of all possible pairs. Then
# we iterate over all the values and print out the permutations of the
# pairs.  O(n^2)
def book(n=1000):
    sums = {}
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            s = a**3 + b**3
            if s in sums:
                sums[s].append((a, b))
            else:
                sums[s] = [(a, b)]
    for s, pairs in sums.items():
        for (a, b) in pairs:
            for (c, d) in pairs:
                print(a, b, c, d)


# Use suggested book lookup method but also use symmetry. Still O(n^2)
def book_sym(n=1000):
    sums = {}
    for a in range(1, n + 1):
        a3 = a**3
        for b in range(1, n + 1):
            if (b > a):
                break
            s = a3 + b**3
            if s in sums:
                sums[s].append((a, b))
            else:
                sums[s] = [(a, b)]
    for s, pairs in sums.items():
        for (a, b) in pairs:
            for (c, d) in pairs:
                print(a, b, c, d)
                if (a != b):
                    print(b, a, c, d)
                if (c != d):
                    print(a, b, d, c)
                    if (a != b):
                        print(b, a, d, c)


n = 1000
#naive(n)
#better(n)
#better_symmetry(n)
#book(n)
book_sym(n)

# results for n=         50     100     1000
#   naive()            9.095s  91.33s    -
#   better()           0.185s  1.119s    -
#   better_symmetry()  0.108s  0.436s   386s
#   book()             0.064s  0.110s   7.3s
#   book_sym()                          5.9s
#
# Checking the output requires sorting the output to make the order of
# the tuples the same for the naive and better algorithms.
#
# sort < better_sym100.out > better_sym100.sorted.out


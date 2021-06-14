#Find the Symmetric Difference:
#Create a function that takes two or more arrays and returns an array of their symmetric difference.
# The returned array must contain only unique values (no duplicates).
#Link:
# https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/find-the-symmetric-difference

a = [3, 3, 3, 2, 5]
b = [2, 1, 5, 7]
c = [3, 4, 6, 6]
d = [1, 2, 3]
e = [5, 3, 9, 8]
f = [1]

def sym(list1, list2, *listlist):
    set1 = set(list1)
    set2 = set(list2)
    for list in listlist:
        set2 = set2^set(list)
    return set1^set2

print(sym(a, b, c, d, e, f))

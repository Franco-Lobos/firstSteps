#Implement Selection Sort
#Write a function selectionSort which takes an array of integers as input and returns
# an array of these integers in sorted order from least to greatest.
#link:
#https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/implement-selection-sort

def selectionSort(inputlist, *rev):
    integerlist = list(inputlist)
    for i in range(len(integerlist)):
        minor = min(integerlist[i:])
        integerlist.remove(minor)
        integerlist.insert(i, minor)
        if checking(integerlist) is True:
            if 'reverse' in rev:
                integerlist.reverse()
            return integerlist

def checking(test):
    for i in test:
        if test.index(i) == 0:
            continue
        if i < test[test.index(i)-1]:
            return False
    return True

print(selectionSort([63, 2, 1, 4, 9], 'reverse'))
print(selectionSort([63, 2, 1, 4, 9]))
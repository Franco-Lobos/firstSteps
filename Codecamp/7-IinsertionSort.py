#Implement Insertion Sort
#Write a function insertionSort which takes an array of integers as input and returns
# an array of these integers in sorted order from least to greatest.
#link:
#https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/implement-insertion-sort

def insertionSort(inputlist, *rev):
    integerlist = list(inputlist)
    outputlist = []
    for i in integerlist:
        if integerlist.index(i) == 0:
            outputlist.insert(0,i)
        else:
            location = insertMet(i, outputlist)
            outputlist.insert(location,i)
    if 'reverse' in rev:
        outputlist.reverse()
    return outputlist

def insertMet(i, outputlist):
    for y in outputlist:
        if y >= i:
            return outputlist.index(y)
        else:
            continue
    return len(outputlist)

print(insertionSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92], 'reverse'))
print(insertionSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))

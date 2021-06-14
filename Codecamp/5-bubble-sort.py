#Implement Bubble Sort
#Write a function bubbleSort which takes an array of integers as input and returns an array
# of these integers in sorted order from least to greatest.
#(it should not use the built-in .sort() method)
#link:
#https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/implement-bubble-sort

def bubbleSort(inputlist, *rev):
    integerlist = list(inputlist)
    actions = 0
    for i in range(len(integerlist)):    
        if i+1 == len(integerlist):
            continue
        else:
            comparative = integerlist[i+1]
        comparativeindex = i+1
        if comparative < integerlist[i]:
            temp = integerlist[i]
            integerlist.remove(integerlist[i])
            integerlist.insert(comparativeindex,temp)
            actions +=1
    if actions == 0:
        if 'reverse' in rev:
            integerlist.reverse()
        return integerlist
    else:
        if 'reverse' in rev:
            return bubbleSort(integerlist, 'reverse')
        else:
            return bubbleSort(integerlist)

print(bubbleSort([1, 4, 2, 8, 345, 55, 1, 234, 92], 'reverse'))
print(bubbleSort([1, 4, 2, 8, 345, 55, 1, 234, 92]))
            

 

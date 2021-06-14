#Merge Sort
#Write a function mergeSort which takes an array of integers as input and returns an array of these
# integers in sorted order from least to greatest. 
#link:
#https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/implement-merge-sort

def mergeSort(inputlist, *rev):
    splits = list(divide(inputlist))
    while len(splits) < len(inputlist):
        for i in splits:
            if len(i) == 1:
                continue
            splits.remove(i)
            for y in divide(i):
                splits.append(y)
    final = finalsort(splits)[0]
    if 'reverse' in rev:
        final.reverse()
    return final

def finalsort(splits):
    finallist = []
    for i in range(len(splits)):
        if (i+1)%2 == 0:
            finallist.append((merge(splits[i-1], splits[i])))
        else:
            if i+1 == len(splits):
                finallist.append(splits[i])
    if len(finallist) > 1:
        return finalsort(finallist)
    elif len(finallist) == 1:
        return finallist

def divide(inputlist):
    if len(inputlist) == 1:
        return inputlist
    middle = int(len(inputlist)/2)
    half1 = list(inputlist[:middle])
    half2 = list(inputlist[middle:])
    return half1, half2


def merge(list1 , list2, *returnedlist):
    list3 = []
    for i in returnedlist:
        for y in i:
            list3.append(y)
    if list1[0] < list2[0]:
        list3.append(list1.pop(0))
    else:
        list3.append(list2.pop(0))
    if len(list1) == 0 or len(list2) == 0:
        list3 += list1 +list2
        return list3
    else:
        return merge(list1, list2, list3)




print(mergeSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))
print(mergeSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92], 'reverse'))




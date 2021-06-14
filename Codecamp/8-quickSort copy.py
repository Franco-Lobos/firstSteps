#Implement Quick Sort
#Write a function quickSort which takes an array of integers as input and returns an array of these integers
# in sorted order from least to greatest. While the choice of the pivot value is important,
# any pivot will do for our purposes here. For simplicity, the first or last element could be used.
#link:
#https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/implement-quick-sort

class SortingClass():
    def __init__(self, inputlist):
        self.mainlist = list(inputlist)
        self.recursive(self.mainlist)

    def recursive(self, datalist):
        self.outputlist = []
        if type(datalist[0]) is list:
            for lists in datalist:
                self.pivoting(lists)
        else:
            self.pivoting(datalist)
        if self.checking() is False:
            self.recursive(self.outputlist)

    def pivoting(self, parciallist):
        if len(parciallist) == 1:
            self.outputlist.append(parciallist)
        else:
            lower = []
            higer = []
            pivot = parciallist[0]
            parciallist.remove(pivot)
            for i in parciallist:
                if i > pivot:
                    higer.append(i)
                if i <= pivot:
                    lower.append(i)
            lower.append(pivot)
            self.outputlist.append(lower)
            if len(higer) > 0:
                self.outputlist.append(higer)

    def checking(self):
        checkinglist = []
        for i in self.outputlist:
            checkinglist += i
        for i in checkinglist:
            if checkinglist.index(i) == 0:
                continue
            if i < checkinglist[checkinglist.index(i)-1]:
                return False
        self.outputlist = checkinglist
        return True

def quickSort(inputlist, *rev):
    sorted = SortingClass(inputlist)
    if 'reverse' in rev:
        sorted.outputlist.reverse()
    return sorted.outputlist

print(quickSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]))
print(quickSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92], 'reverse'))




            
#Pairwise
#Given an array arr, find element pairs whose sum equal the
#second argument arg and return the sum of their indices.
#link:
#https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/pairwise

class PairingClass():
    def __init__(self, inputlist, match):
        self.inputlist = inputlist
        self.match = match
        self.counter = 0
        self.searchtry()

    def searchtry(self):
        counter = 0
        for i in self.inputlist:
            pairwise = self.match - i
            indexi = self.inputlist.index(i)
            self.inputlist[self.inputlist.index(i)] = 0.1
            self.findmatch(indexi, pairwise)

    def findmatch(self, indexi, pairwise):
        for remain in self.inputlist[indexi:]:
            if pairwise == remain:
                self.counter+= self.inputlist.index(pairwise)
                self.counter+= indexi
                self.inputlist[self.inputlist.index(pairwise)] = 0.1
                return True
            

def pairWise(inputlist, match):
    compared = PairingClass(inputlist, match)
    return compared.counter

print(pairWise([1, 4, 2, 3, 0, 5], 7))


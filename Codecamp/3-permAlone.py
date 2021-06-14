#No Repeats Please
#Return the number of total permutations of the provided
#string that don't have repeated consecutive letters.
#Assume that all characters in the provided string are each unique.
#link:
#https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/no-repeats-please

from math import ceil 

class CalculateChances():
    def __init__(self, string):
        self.finallist = []
        self.temporallist = self.settemporallist(string)
        self.unit = len(string)
        self.possibilities = self.setpossibilities()
        self.operation()
        
    def exceptions(self):
        if self.unit == 2:
            if self.temporallist[0] != self.temporallist[1]:
                self.permalon = 2
            else:
                self.permalon = 0
        elif self.unit == 1:
            self.permalon = 1

    def settemporallist(self, string):
        templist = []
        for i in string:
            templist.append(i)
        return templist

    def setpossibilities(self):
        poss = 1
        for i in range(self.unit):
            poss = poss * (i+1)
        return poss

    def setcombinations(self, counter): #counter = self.unit
        for i in range(counter):
            position = counter -1 
            removed = self.temporallist.pop(0)
            self.temporallist.insert(position,removed)
            if counter > 3:
                counter -= 1
                self.setcombinations(counter)
                counter += 1
            elif counter == 3:
                self.sort()
             
    def sort(self):
        for i in range(2):
            removed = self.temporallist.pop(0)
            self.temporallist.insert(1,removed)
            posibilitylist = list(self.temporallist)
            self.finallist.append(posibilitylist)
        
    def counterpairs(self):
        counter = 0
        match = False
        diferent = False
        for iterlist in self.finallist:
            if self.searchmatch(iterlist) is True:
                counter +=1
        return counter

    def searchmatch(self, iterlist):
        diferent = True
        for i in range(len(iterlist)):
            if i == 0:
                continue
            if iterlist[i] != iterlist[i-1]:
                diferent = True
            elif iterlist[i] == iterlist[i-1]:
                diferent = False
                return diferent
        return diferent

    def checking(self):
        temporaldict = {}
        diversity = ceil(self.unit/2)
        comparative = 0
        for i in self.temporallist:
            if i not in temporaldict:
                temporaldict[i] = 1 
            else:
                temporaldict[i] += 1
        for key in temporaldict.keys():
            if temporaldict[key] > comparative:
                comparative = temporaldict[key]
        if comparative > diversity:
            return 0
        elif len(temporaldict.keys()) == len(self.temporallist):
            return self.possibilities
        return 1

    def operation(self):
        if self.checking() == self.possibilities or self.checking() == 0:
            self.permalon = self.checking()
            print('Fast cheking')
        else:
            if self.unit > 2 :
                self.setcombinations(self.unit)
                self.permalon = self.counterpairs()
            else:
                self.exceptions()
                print('Fast cheking')

def permAlone(inputvalue):
    chances = CalculateChances(inputvalue)
    return(chances.permalon)

print(permAlone('aaabb'))
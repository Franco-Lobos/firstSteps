#Inventory Update
#Compare and update the inventory stored in a 2D array against a second 2D array of a fresh delivery.
# Update the current existing inventory item quantities (in arr1).
# If an item cannot be found, add the new item and quantity into the inventory array.
# The returned inventory array should be in alphabetical order by item.
#Link:
#https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/inventory-update


def updateInventory(curinv, newinv):
    datadict = {}
    for list in curinv:
        datadict[list[1]] = list[0]
    for list in newinv:
        if list[1] in datadict.keys():
            cache = datadict.get(list[1])
            datadict[list[1]] = cache + list[0]
        else:
            datadict[list[1]] = list[0]
    array=[]
    for key in sorted(datadict):
        pair = [datadict.get(key), key]
        array.append(pair)
    return array

print(updateInventory([[0, "Bowling Ball"], [0, "Dirty Sock"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]) )
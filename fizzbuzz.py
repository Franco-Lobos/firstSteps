
def multiple3(number):    
    multiple = False
    while len(str(number)) > 1:
        cache = 0
        for figure in (str(number)):
            cache = cache + int(figure)
        number = cache
    if number == 3 or number == 6 or number ==9:
        multiple = True
    return multiple

def multiple5(a):
    multiple = False
    conditional = str(a)[-1:]
    if int(conditional) == 5 or int(conditional) == 0:
        multiple = True
    else:
        multiple = False
    return multiple

def fizzbuzz(numb):
    for i in range(int(numb)):
        i = i+1
        mtp3 = multiple3(i)
        mtp5 = multiple5(i)

        if mtp3 is True and mtp5 is False: print(f'{i}: fizz')    
        elif mtp3 is False and mtp5 is True: print(f'{i}: buzz')
        elif mtp3 is True and mtp5 is True: print(f'{i}: fizzbuzz')
        else: print(i)


fizzbuzz(input('Choice a number as the range of iterations\n'))
input('')

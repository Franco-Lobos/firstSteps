
text = open('prueba.txt')
alphabet = 'qwertyuiopasdfghjklñzxcvbnmáéíóúüQWERTYUIOPASDFGHJKLñZXCVBNMÁÉÍÓÚÜ'

def conversor(string):
    cache = '(\''
    for character in string:
        if character == ' ':
            character = '\', \''
            cache = cache + character
        elif character not in alphabet:
            pass 
        else:
            cache = cache + character.lower()
    cache = cache + '\')'        
    return cache

def counter():
    array = eval(conversor(text.read()))
    text.close()
    counterDict = {}
    for i in array:
        if i not in counterDict:
            counterDict[i] = 1
        elif i in counterDict:
            counterDict[i] = counterDict.get(i) + 1
    
    for i in counterDict:
        print(f'{i}:{counterDict.get(i)}')
    print('Total de palabras:', sum(counterDict.values()))

counter()




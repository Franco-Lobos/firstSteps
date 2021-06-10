def fizzbuzz2(inputnumber):
    for i in range(int(inputnumber)):
        if i%3 == 0:
            print(f'{i}--Fizz')
        elif i%5 ==0:
            print(f'{i}--Buzz')
        elif i%3 == 0 and i%5 == 0:
            print(f'{i}--FizzBuzz')
        else:
            print(i)

fizzbuzz2(input('Choice a number as the range of iterations\n'))
input('')
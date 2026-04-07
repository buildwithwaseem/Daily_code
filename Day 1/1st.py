'''QUES1 - Print all the even numbers from 1 to 100.'''

#way1
for numbers in range(1,101):
    if numbers % 2 ==0:
        print(numbers)

#way2
#we start with 2 and jump by 2
for numbers in range(2,101,2):
    print(numbers)



'''QUES2  - FizzBuzz'''
#way1
for i in range(1,101):
    if i%3 ==0 and i%5 ==0:
        print("FizzBuzz")
    elif i %3 ==0:
        print("Fizz")
    elif i%5 ==0:
        print("Buzz")
    else:
        print(i)

#way2 -- the best way
for i in range(1,101):
    output= ""
    if i %3 ==0 :  output +="Fizz"
    if i %5 ==0 : output += "Buzz"
    
    print(output or i)


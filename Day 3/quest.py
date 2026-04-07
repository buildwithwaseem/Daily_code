'''Ques1 - Find max in a list without max()'''
numbers = [3,41,12,9,74,15]
max_val = numbers[0]

for num in numbers:
    if num > max_val:
        max_val = num

print(f'maximum number in this list is: {max_val}')



'''Ques2 -  Check if a number is prime '''


n =  int(input('Enter the number: '))
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2,n):
        if n % i ==0:
            is_prime = False
            break

if is_prime:
    print(f'{n} is a prime number.')

else:
    print(f'{n} is not a prime number.')





'''Ques3 - Print star pyramid pattern'''

height = 5
for i in range(1, height+1):
    spaces = " " * (height-i)
    stars = "*" * (2 * i-1)
    print(spaces + stars)

'''Ques1 - Print star pyramid pattern'''
height =3
for i in range(1, height+1):
    space = ' ' * (height-i)
    star = '*' * (2 * i-1)
    print(space + star)

'''Ques2 - Sum of digits of a number'''
n = 143
total_sum = 0
while n >0:
    digit = n % 10
    total_sum += digit
    n = n//10

print(f'sum: {total_sum}')

'''Ques3 - Check if a string is a palindrome'''
word = input('Enter the word: ')
word = word.lower()
is_palindrome = True
length = len(word)
for i in range(length // 2):
    if word[i] != word[length -1 -i]:
        is_palindrome = False
        break

if is_palindrome:
    print(f'{word} is palindrome')
else:
    print(f'{word} is not a palindrome')
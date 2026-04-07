"""'''Ques1 - Reverse a string with a loop (no slicing)'''
original = input("Enter your word: ")
reversed_str = ""

for char in original:
    reversed_str = char + reversed_str

print("Your reversed word is :", reversed_str)



'''Ques2 - Count vowels in a string'''
text = input("Enter your sentences/words: ")
vowel_count = 0
vowels = "aeiouAEIOU"

for char in text:
    if char in vowels:
        vowel_count += 1

print(f'Number of vowels: {vowel_count}')


'''Ques3 - Print multiplication table of n'''

n = int(input("Enter the number: "))
for i in range(1,11):
    result = n * i

    print(f'{n} * {i} = {result}')"""


''' AGAIN P R A C T I C E '''
#1 Ques1 - Reverse a string with a loop (no slicing)

original = input("Enter you word: ")
reversed_str = ""

for char in original:
    reversed_str = char + reversed_str

print(f'your reversed string is : {reversed_str}')


#2 Ques2 - Count vowels in a string

text = "i am the best at this time of ai era"
vowel_count = 0
vowel = "aeiouAEIOU"

for char in text:
    if char in vowel:
        vowel_count +=1

print(f"number of vowels: {vowel_count}")


#3 Ques3 - Print multiplication table of n

n = 5
for i in range(1,11):
    result = n * i
    print(f'{n}*{i} = {result}')
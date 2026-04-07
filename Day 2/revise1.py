'''Ques1 - Reverse a string with a loop (no slicing)'''
original = int(input("Enter the word: "))
reversed_str = ""
for char in original:
    reversed_str = char + reversed_str

print(f'the reersed word is: {reversed_str}')


'''Ques2 - Count vowels in a string'''
text = input("Enter the sentence/word: ")
vowel_count = 0
vowel = 'aeiouAEIOU'
for char in text:
    if char in vowel:
        vowel_count += 1

print(f'vowel count in the sentence is : {vowel_count}')


'''Ques3 - Print multiplication table of n'''

n = int(input("Enter the number : "))
for i in range(1,11):
    result = n * i
    print(f'{n}*{i} = {result}')

    
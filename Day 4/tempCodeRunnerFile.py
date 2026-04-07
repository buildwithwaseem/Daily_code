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
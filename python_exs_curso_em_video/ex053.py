sentence = str(input('Write a sentence that is a palindrome: ')).strip().upper()
words = sentence.split()
join = ''.join(words)
reverse = ''

for letter in range(len(join) - 1, -1, -1):
    reverse = reverse + join[letter]

if reverse == join:
    print('This is a palindrome =)')
else:
    print('That is not a palindrome =(')

pyg = 'ay'

original = eval(input('Enter a word:'))

if len(original) > 0 and original.isalpha():
    original.lower()
    word = original
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print(new_word)
else:
    print("empty")

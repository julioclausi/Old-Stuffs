letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

word = 'AbCdEfGh'

value = 3
new_word = ""

for letter in word:
    position = letters.index(letter)
    if (position+value) >= (len(letters)):
        new_letter = letters[position+value-len(letters)]
    else:
        new_letter = letters[position+value]
    new_word += new_letter

print (new_word)
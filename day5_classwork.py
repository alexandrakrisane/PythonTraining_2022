# 07.02.2022

import string


print("\n___________Exercise 1 ________________\n")
name = input("Input your name: ").lower()
extra_text = ' , a thorough mess is it not '
reversed_name = name[::-1]
print(reversed_name.title() + extra_text + name[0].upper() + "?")



print("\n___________Exercise 2 ________________\n")

text = input("Input you word or phrase: ")
text_masked = ''
text_unmasked = ''
for c in text:
    if c == " ":
        text_masked += " "
    else:
        text_masked += "*"
print(text_masked)

guess_letter = input("Input your guess (one symbol): ")
for c in text:
    if c == guess_letter:
        text_unmasked += c
    elif c == " ":
        text_unmasked += " "
    else:
        text_unmasked += "*"
print(text_unmasked)



print("\n___________Exercise 3 ________________\n")
user_input = input("Input you word or phrase: ")
print("\n" + user_input)
word_not = 'not'
word_bad = 'bad'
replacement = "good"

position_not = user_input.find(word_not)
position_bad = user_input.find(word_bad)
start = position_not
end = position_bad + len(word_bad)

if 0 < position_not < position_bad:
    user_output = user_input.replace(user_input[start:end], replacement)
    print(user_output.replace("  "," "))

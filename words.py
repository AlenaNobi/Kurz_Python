import json

with open('words.txt', encoding='utf-8') as file:
    words = file.read().split()

words_list = []
for word in words:
    first_letter = word[0]
    if first_letter not in words_list:
        words_list.append(first_letter)
words_list = sorted(words_list)

words_dict = {}
for letter in words_list:
    words_dict[letter] = []

for word in words:
    first_letter = word[0]
    words_dict[first_letter].append(word)

for key, value in words_dict.items():
    words_dict[key] = sorted(value)

with open('output.json', 'w', encoding='utf-8') as file:
    json.dump(words_dict, file, indent=4)

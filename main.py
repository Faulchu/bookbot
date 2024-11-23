def word_count(string):
    word_list = string.split()
    word_count = len(word_list) 
    return word_count

def characters(string):
    string = string.lower()
    characters = {}
    for letter in string:
        if letter in characters:
            characters[letter] = characters[letter] + 1
        else:
            if letter.isalpha():
                characters[letter] = 1
                
    return characters

def sort_on(dict):
    return dict["num"]

def split_sort_dict(dict):
    list_of_characters = []
    for key in dict:
        temp_dict = {"char": key, "num": dict[key]}
        list_of_characters.append(temp_dict)
    list_of_characters.sort(reverse=True, key=sort_on)

    return list_of_characters



with open("books/frankenstein.txt") as f:
    file_contents = f.read()
print(file_contents + "\n")

word_amount = word_count(file_contents)

print(f"This book has {word_amount} words!\n")

letters = characters(file_contents)
letters = split_sort_dict(letters)

for item in letters:
    print(f"The '{item["char"]}' character was found {item["num"]} times")

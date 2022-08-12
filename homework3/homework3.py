"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""
from collections import Counter
characters = "sjfhskjgsfnsrghsodfh"
phrase = "john"
character_list = []
phrase_list = []

def generate_phrase(characters, phrase):
    for a in characters:
        character_list.append(a)
    for b in phrase:
        phrase_list.append(b)
    for l in phrase_list:
        #print(l)
        if l in character_list:
            character_list.remove(l)
            #print(True)
        elif l not in character_list:
            #print(False)
            return False
    return True
    # common_character = (list(set(character_list).intersection(phrase)))
    # print(len(common_character) == len(phrase_list))
    # print(all(char in character_list for char in phrase_list))
    # list3 = set(character_list) & set(phrase_list)
    # list4 = sorted(list3, key=lambda k: character_list.index(k))
    # print(list4)


x = generate_phrase(characters, phrase)
print(x)
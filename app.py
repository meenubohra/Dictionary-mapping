# imports
import json
from difflib import get_close_matches

# load JSON data into python
data = json.load(open('data.json'))

# function to return translation of input words


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]  # in case user enters words like USA or NATO
    elif len(get_close_matches(w, data.keys())) > 0:
        rep = input("Did you mean %s instead? If yes the enter Y and if no the N: " % get_close_matches(
            w, data.keys())[0])
        # %s string formatter ,get_close_matched returns string formatter
        if rep == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif rep == "N":
            return 'The word doesnt exist,please check again.'
        else:
            return 'Did not understand the entry.'
    else:
        return 'The word doestnt exist in the dictionary.'


# input processing
word = input('Enter the word: ')
results = translate(word)

# result output either a list or string so use type to differenciate
if type(results) == list:
    for res in results:
        print(res)
else:
    print(results)

# we can use try except block as well
# try:
#     print(translate(word))
# except:
#     print('The word do not exist in the dictionary')

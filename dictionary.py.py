import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data :
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        choice=input("Did you mean {} instead ?".format(get_close_matches(w,data.keys())[0]))
        if choice=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif choice=="n":
            return "No similar word found"
        else:
            return "No similar word"
while True:
    word=input("Enter a word :")
    output=translate(word)
    if type(output)==list:
        for item in output:
            print(item)
    else:
        print(output)
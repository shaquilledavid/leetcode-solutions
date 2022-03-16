import os
import glob


path = 'C:/Users/shaqu/Documents/the_hub/lib/chores/pages'

count = 0

def countWords(f, word):
    allWords = [str(x.strip()) for x in f]
    occurences = 0
    for w in allWords:
        if w == word:
            occurences += 1

    print(allWords)   
    return occurences

def replace(oldWord, newWord):
    pass

for filename in glob.glob(os.path.join(path, '*.dart')):
    with open(os.path.join(os.getcwd(), filename), 'r') as f: #open in write mode
        countWords(f, "chores")

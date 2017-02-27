from collections import defaultdict
file = open('words.txt')

"""
word_ladder is a recursive function that implements depth first search. It itterates
through the list of words until it has found a word that is one letter different
from the current word and is equal to or greater in simlarity to the current word.

After getting a functional version returning a path 87 words long We used the 
following word ladder generator to give a benchmark:
http://ceptimus.co.uk/wordladder.php

this site returns an 8 step solution. all 8 words are in words.txt. we concluded
our solution was not reaching the best possible path. After refactoring heuristics
we were able to get it down to 32. Further attempts were made, but we were unable
to break it down more using DFS. 

BFS may perhaps be the better solution. I just think this way is cool.

input:
    list: list of words of same length
    start: starting word
    end: ending word
    step: alright so this one was an attempt to improve heuristics though I am
          unsure how to implement it. given more time I could porbably figure
          it out.

output:
    path: the list of words from start to end.

"""

def word_ladder(list, start, end, step = 0):
    list.remove(start)
    path = []
    path.append(start)
    for word in list:
        if sum(n == m for n, m in zip(word, start)) == len(word) - 1 and sum(n == m for n, m in zip(word, end)) >= sum(n == m for n, m in zip(start, end)):
            if word == end:
                path.append(word)
                return path
            temp = word_ladder(list, word, end, step + 1)
            if temp == 0:
                continue
            return path + temp
    return 0

words_dict = defaultdict(list)

# creates a dictionary with word lengths as the key, and a list of words corresponding
# to that length.
for word in file:
    word = word.strip()
    key = len(word)
    words_dict[key].append(word)

startWord = 'f'
endWord = ''
tempWord = ''

print('\n\n\n\n\n\nWelcome to word ladder! please ensure that the starting and ending words are the same length\n')
while len(startWord) != len(endWord) :
    
    startWord = raw_input('Enter the starting word: ')
    endWord = raw_input('Enter the ending word: ')
    
    if len(startWord) != len(endWord) :
        print('ERROR: re-enter the words\n')

i = 0
for word in word_ladder(words_dict[len(startWord)], startWord, endWord):
    i = i + 1
    print word
print 'steps:', i
from collections import defaultdict

file = open('words.txt')

words = {}
anagrams = {}

firstWord = file.readline()
firstWord = firstWord.strip()
sort = sorted(firstWord)
firstWordSorted = ''.join(sort);
# defaultdict contains the append method which we will need
# THIS IS A BREADTH-FIRST SEARCH as we are not checking each word against every other word in the dictionary to find a solution
from collections import defaultdict
# open word file
file = open('words.txt')
# declare a defaultdict object that takes a list as an argument
words = defaultdict(list)
# for loop to read through every line in the file
for word in file:
    # strip the word of any line breaks or whitespace
    # sort the word and use .join() to combine the sorted list of chars into a string
    # necessary because a defaultdict can't take a list as a key
    word = word.strip()
    sort = sorted(word)
    sort = ''.join(sort)
    # add the current word to a dictionary with its sorted self as a key and append it to that entry
    words[sort].append(word)
# loop through the dictionary and print any entries in which the length is greater than 1
for entry in words:
    if len(words[entry]) > 1:
        print(words[entry])
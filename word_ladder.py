from collections import defaultdict
file = open('words.txt')

def word_ladder(list, start, end, step = 0):
    list.remove(start)
    path = []
    path.append(start)
    for word in list:
        if sum(n == m for n, m in zip(word, start)) == len(word) - 1 and sum(n == m for n, m in zip(word, end)) >= sum(n == m for n, m in zip(start, end)):
            #print word
            if word == end:
                path.append(word)
                return path
            temp = word_ladder(list, word, end, step + 1)
            if temp == 0:
                continue
            return path + temp
    return 0

words_dict = defaultdict(list)

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
# print word_ladder(words_dict[len(startWord)], startWord, endWord)
for word in word_ladder(words_dict[len(startWord)], startWord, endWord):
    i = i + 1
    print word
print 'steps:', i
from collections import defaultdict
file = open('words.txt')
words = defaultdict(list)
grid = [[0 for x in range(4)] for y in range(4)] 
for word in file:
    word = word.strip()
    words[word] = list(word)

"""
check implements depth first search. it checks the given character from grid
against a list of words and once it finds a match it investigates further by
looping through the remaining characters and checks the immediately surrounding 
characters in the grid to see if they correspond to the current character and
breaks if they don't, moving on to the next word.


input:
    words: a dictionary where key = a word and value = char list of that word.
    grid: a 2D list of characters
    r: the starting row
    c: the starting column

output:
    explored_words: a dictionary, where key = a word and value = the corresponding
                    coordinates of each letter.

"""

def check(words, grid, r, c):
    explored_words = defaultdict(list)
    visited = []
    for word in words:
        row = r
        col = c
        if grid[row][col] != word[0]:
            continue
        visited.append((row,col))
        for char in word[1:]:
            x = -1
            y = -1
            newPos = False
            # The cool bit. there are a maximum of 8 positons surrounding any given
            # position. the following loop checks every single one. However, python
            # is weird and allows for negative indexes. so we have to check against
            # that. We also check to see if the positions has been visited, and if
            # the character at that position is equal to the current char in the word.
            
            for i in range(8):
                if i > 0 and i < 3:
                    x = x + 1
                if i >= 3 and i < 5:
                    y = y + 1
                if i >= 5 and i < 7:
                    x = x - 1
                if i == 7:
                    y = y - 1
                newPos = False
                try:
                    if row + x >= 0 and col + y >= 0 and (row + x, col + y) not in visited and grid[row + x][col + y] == char:
                        row = row + x
                        col = col + y
                        visited.append((row,col))
                        newPos = True
                        break
                except IndexError:
                    continue
            # if it completes without finding the next letter in the word, the path
            # is whiped and we move on to the next word.
            if not newPos:
                visited = []
                break
        if visited:
            explored_words[word] = visited
            visited = []
    return explored_words
            
        
grid[0][0] = 'u'
grid[0][1] = 'n'
grid[0][2] = 't'
grid[0][3] = 'h'
grid[1][0] = 'g'
grid[1][1] = 'a'
grid[1][2] = 'e'
grid[1][3] = 's'
grid[2][0] = 's'
grid[2][1] = 'r'
grid[2][2] = 't'
grid[2][3] = 'r'
grid[3][0] = 'h'
grid[3][1] = 'm'
grid[3][2] = 'i'
grid[3][3] = 'a'

words_in_grid = defaultdict(list)

for row in range(4):
    for col in range(4):
        words_in_grid.update(check(words,grid,row,col))

for i in words_in_grid:
    print i, words_in_grid[i]
print 'words:', len(words_in_grid)
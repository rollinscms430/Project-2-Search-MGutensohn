# Grade

## Anagrams

Looks good.

## Word Ladders

Works fine, although it doesn't find the shortest path. Remeber that a breadth-first search would be guaranteed to find the solution
path that contains the smallest number of actions from the root.

Also, you have a very complicated conditional that, I think, is checking
if a candidate word and the current word are only one letter apart. It would be appropriate to use a comment to explain what that
statement is doing. -1.


## Boggle

Okay. It looks like your implementation is taking the entire list of words, then searching to see which words can be found in
the Boggle grid, as opposed to starting searching the grid and finding the words that it contains. It's hard to tell, because again, your
implementation contains no comments explaining how it works or why you used the design you did.

It also looks like there's a bug in your search: I'm not sure that it actually generates all of the eight neighbors correctly.

-10

## Total

89 / 100

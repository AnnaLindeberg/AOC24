# Advent of code 2024
First time advent-of-coding with a full-time job and grown-up responsibilities. Let's see if I make it to december 10th!

## Day 1: Historian Hysteria
Look its December first! Parse two vertical lists, sort them and then do some arithmetics.

## Day 2: Red-Nosed Reports
There is certainly a way of not rechecking each line for each element in the line i.e. do a linear time version, but I didn't bother.

## Day 3: Mull It Over
Well this feels like a good place to use regex-things, but I just parsed it from left to right in a brute-force kind of way. I did cheat a little though by making sure that the number that occurred in the input file did not have too many digits (probably never more than 3 each?), that none of them where negative (no occurrences of the patterns 'mul(-' or ',-digit' ) etc. Probably got the code for the second part to work a lot faster than I thought –- I first didn't catch that the small given example had actually changed between part one and two...

## Day 4: Ceres Search
Implemented a Grid-class with a sort of semi-elaborate `getitem`-implementation for sliced indexing things like `grid[(0,0):(6,6):'SE']`. Because I didn't want to bother determining the direction from the coordinate pairs I let the `step`-part of the slice be a string that decided the offset (eg 'SE' corresponds to South East or $(1,-1)$, one increase in $x$-direction and one in $y$-direction). In no way robust but a little bit of fun and it made the wordsearch in part one quite nice. Also suitable enough for part 2, so that was nice.

## Day 5: Print Queue
This was a nice little graph problem! Looking at the input file, I concluded that it was fine to verify if a list was sorted by checking each pair in the given list –– possibly there's a way around it if you're clever about it but well, that wasn't necessary. For the second part I thought about writing some custom key-function to pass to pythons sort-function, but then I just guessed that each unsorted list would have a unique sorting, and could thus restrict the graph-like orders to only the numbers in the list to-be-sorted

## Day 6: Guard Gallivant
I spent the first part of this figuring out how to work with `slice` objects in custom `getitem`-methods. Completely over-engineered for this certainly, yet still half-assed. But good practice. The second one I solved (almost) brute force, namely by placing an obstruction at each of the positions visited in the first guard-walk (so.. not all spots of the map, but quite many). On the slow side but this time I'm not inclined to cook up something better.

## Day 7: Bridge Repair
I did this with a queue, sort of just exhaustive search? I didn't even need to abort certain `lines of search' when they became infeasable to make the calculations run quickly enough (I would've guessed this was necessary, since all operations make something larger).

## Day 8: Resonant Collinearity
Aaaa okay I just didn't feel like another grid-puzzle and hacked together part 1. Part 2 shouldn't be too difficult but my first meager attempt did't work so we'll see if I ever finish it.

## Day 9: Disk Fragmenter
I _like_ this one! For part 1, I essentially compute the checksum on-the-fly by having a left pointer determining if we're at an index that is initially empty or not and a right pointer that keeps track of what we would move to some empty slot more to the left. Run until the two pointers meet, in essence.

For part 2, I'm in the unfortunate place where it works on the small input but not on the large one. But I think my solution is clever! It should work! :(

## Day 10: Hoof It
Haha okay this was just a DFS in the map that I hacked together, but I didn't read the task that thoroughly so I solved part 2 when I tried to solve part 1. That means I just needed like one line of code more for part 2. Very quick!

## Day 11: Plutonian Pebbles
Standard part2: do the same as in part1 but only larger. I have, after all, taught dynamic programming this term so this was not so difficult to crack. Fortunately, the recursion depth was not a problem for python here, because I have no clue how one would make it interative...
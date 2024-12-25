# Advent of code 2024
First time advent-of-coding with a full-time job and grown-up responsibilities. Let's see if I make it to december 10th!

## Day 1: Historian Hysteria
Look its December first! Parse two vertical lists, sort them and then do some arithmetics.

## Day 2: Red-Nosed Reports
There is certainly a way of not rechecking each line for each element in the line i.e. do a linear time version, but I didn't bother.

## Day 3: Mull It Over
Well this feels like a good place to use regex-things, but I just parsed it from left to right in a brute-force kind of way. I did cheat a little though by making sure that the number that occurred in the input file did not have too many digits (probably never more than 3 each?), that none of them where negative (no occurrences of the patterns `mul(-` or `,-digit` ) etc. Probably got the code for the second part to work a lot faster than I thought –- I first didn't catch that the small given example had actually changed between part one and two...

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

## Day 12: Garden Groups
So, the first one I solved with some sort of BFS that counts perimeter and area at each position (one contigious flower bed at a time). Not so difficult to figure out, but I'm a bit stumped when it comes to part 2. I have tried to update the BFS to have som "memory" of what fence-pieces already have been encountered, but now when I think about it again I've realized that I can still reach the same fence side from different directions and therefore overcount the sides slightly. I would now guess that one needs to keep track of pieces of fence overall, and then "glue them together" in a last step. That's an interesting thought but not something I had time to code today...

OK – weekend! I though about it and solved part 2 too! Essentially, I keep track of pieces of fence with a small offset (0.1) to the left or right of the tile where I found it. These fence pieces are then puzzled together when contigious intervals are found, counting actual sides and not pieces of fence. It works but the code is quite repetative and hacky... 

## Day 13: Claw Contraption
Oh.. These are linear diophantine equations. Or I guess equation systems of linear diophantine equations. I can sort of do it by hand but not so eager to manage it with a computer. This will have to wait, if ever...

OK attempt one was fancy math. But even if I generate a particular solution (solving only for, say, the x-part of the coordinate) it's a headache to generate all solutions in the correct interval so I gave up and did the stupid thing: nested for-loops. Oh well. Worked for part 1, but not even worth trying for part 2.
Attempt three was less fancy math, just inverting 2x2-matrices and calculating the real solutions to the equation system consisting of $x_a\cdot a+x_b\cdot b = p_x$  and $y_a\cdot a+y_b\cdot b = p_y$ (solving for $a$ and $b$) -– but that does not seem to find solutions at all?! I give up...

## Day 14: Restroom Redoubt
Spent way way way to much time debugging like 6 rows of code I *knew* was correct, since the grid looked nothing like it should after 100 seconds. Turns out I had dropped every single negation sign while reading the input. For part 2: hahaha that's the least well-defined question I've seen in AOC. I need to learn some basics of a GUI to make it work.

Update: I really didn't need a GUI. Based on a hint from my mum I just checked for situations when no two robots occupied the same position and printed that to the terminal. Look, a little christmas tree!

## Day 15: Warehouse Woes
This was a fun one! I could copy-paste a little from the word search on day 4, but most of the rest I sort of hacked together bit by bit. There's no elegant stuff going on, and I more or less had to write a completely different solution for part 2. 

## Day 17: Chronospatial Computer
Hm I solved day 1 by tediously rewriting the 8 givenn rules as code, then for part 2 I sort of manually decoded the operations and wrote down as a small while-loop that updates values of A, B, C without actually using the program as input. But I can't crack how to limit the search space from all integers in the range $[8^{15}, 8^{16}-1]$ (this is what makes the output consist of 16 digits) which, of course, is way to large. By various insanely questionable attempts I think I landed in that the binary representation of the correct answer must start with `101011010010000001000` and end with `101010011110000001111`, with six digits between –– but that doesn't quite work. It makes the first six digits and the last seven correct but no six digits chucked inbetween these sequneces seem to work, and I can't test every integer between 
`101011010010000001000000000101010011110000001111` to `101011010010000001000111111101010011110000001111` (in binary, then) because that's the range $[190354025692175, 190354157812751]$, way to large (and possibly not even correct?). Why did my approach of deciding for chunks of three bits at a time only work for parts of the list but not the whole thing? Beats me!!!! 

## Day 19: Linen Layout
This was so obviously fitting for dynamic programming that I, in essence, solved the second part already in the first. Just had to change some Boolean values in the DP-array to integer counts and remove some `continue`-behaviour. Few lines of codes for a date this late in December -- but I guess there's always an ''easy one'' now and again.


## Day 16: Reindeer Maze
Went back and gave this an attempt in the way I've said last year: build a networkX-graph from the input rather than writing a custom Dijkstra (or similar). Seemed suitable for this one – there was some fiddling in which coordinates should be vertices and which not, and which edges should have what weights but I managed it for the first part. Unfortunately I think I need to rebuild the whole graph for the second part so that will have to wait for some other time...

Update part2: I didn't have to re-build the graph! Since I omitted some map-positions for nodes (in intersections, essentially) to get correct edge weights the vertices of the graph didn't exactly correspond to the positions that were to be counted. However, I could find out if these positions should be counted depending on wether they are adjacent to at least two actual vertices that lie along a shortest path. Nice enough, I'd say.

## Day 20: Race Condition
A big question mark on why I haven't used networkX earlier years – it makes it possible to solve things like this! I parsed the track as a graph and then checked "almost adjacent" pieces of tracks and wether a cheat would be advantageous. For the second part I had to slightly rethink this and instead loop over the positions it would be good to cheat-jump to, and then check if it's possible to travel that far. Positions that are too far away from start or end (in comparison to shortest start-end path) are not considered. This is just barely enough restriction of the problem to make it run in a couple of seconds, so I guess there is a faster solution but I'm not going to attempt finding it.

## Day 18: RAM Run
This was, too, quite easy with networkx (any pattern here?!): initiate a grid-graph and then stepwisely remove vertices as specified in the input. For part one, terminate after a specified number of deletions and return the shortest path. For part two, continue until no start-end path can be found. I guess it is completely brute-force to (try to) recalculate the shortest path after each deletion – possibly there's more dynamic shortest path algorithms (actually there's many hits for papers on that topic with a quick google search) that would've been the fast solution here, but who cares when it works like this too.

## Day 21: Keypad Conundrum

## Day 23: LAN Party

## Day 24: Crossed Wires

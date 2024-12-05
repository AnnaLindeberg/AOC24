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

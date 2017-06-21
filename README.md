# x-inference
Inference engine experimentation

The central idea here is to process inference rules symbolically. Given the form of a rule ```if A then B```,
we do not immediately
care what A and B represents, only that each A in a list of rules have some number of then conditions. Also, given a number
of rules with A on the LHS, like:
```
A=>B
A=>C
A=>F
```
we can rewrite these rules as ```if A then B|C|F```. Maybe that's useful in the long run, as FPGAs do bitwise
logical operations for free.

I'm assuming the symbols do relate to real things, but we only care about these on the input and output from the engine
itself. This implies we could have a symbol map (database?) that is only consulted when a human wants to know results. 
I think the bulk of the processing time is rules processing, so symbol to readable name mapping hopefully is
low performance impact relative to rules processing. We'll see.

Let's start with forward chaining (why not?), straight symbol manipulation, cycling through three
sequential steps: match rules, select rules, and execute rules.

I'm thinking this can get away with only using a single bit position for the LHS and a single bit position for the RHS
(RHS: to start, at least.) So in A=>B, A and B both are represented by a single bit position. The tiny example
```
A=>B
A=>C
A=>F
```
could be represented by two bytes
```
10000000 => 01000000
10000000 => 00100000
10000000 => 00000100
```
or even
```
10000000 => 01100100
```
if the bits are representing ABCDEFGH from left to right. I understand rule execution order is important, so
maybe the second form is not so useful. Unless I could impose an ordering on processing? Experimentation is needed. Whole
heap o' tradeoffs already.


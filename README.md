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


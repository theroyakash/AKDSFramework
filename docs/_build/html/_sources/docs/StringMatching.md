# String Matching algorithm
Fast access linear time string matching algorithm from Knuth, Morris and Pratt. Mathematical complexity: $O(m + n)$, where n is the length of the sequence and m is the length of query string.

The algorithm avoids the computation of transition function delta altogether (better than using a finite automata).

## Usage
We have one KMP algorithm and one naive string matching algorithm.
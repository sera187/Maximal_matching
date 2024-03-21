In this thesis, we study deterministic algorithms for maximal matching in a dynamically 
changing graph. The purpose is the implementation and experimentation of the algorithm 
described in the paper by Neiman and Solomon entitled ‘’Simple Deterministic Algorithms 
for Fully Dynamic Maximal Matching’’. This dynamic setting allows both insertions and 
deletions of edges while the vertex set is fixed and determined from the beginning. A 
standard assumption is that in each step, a single edge is added to the graph or removed 
from it, such a step is called an edge updated or shortly an update. A simple greedy 
algorithm computes a maximal matching in 𝑂(𝑚) time, so recomputing a maximal
matching would cost 𝑂(𝑚) per update. Neiman and Solomon’s algorithm manages 
maintains explicitly a maximal matching in 𝑂(√𝑚 + 𝑛) worst-case update time.

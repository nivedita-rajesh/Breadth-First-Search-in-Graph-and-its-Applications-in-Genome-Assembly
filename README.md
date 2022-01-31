# Breadth First Search in Graph and its Applications in Genome Assembly
## ABOUT

Applying BFS on a de_Bruijn graph.

## IMPLEMENTATION
The contents of the fasta file (dataset) is read and processed by removing the unwanted lines. Only the alternate lines in the file can be used for making the graph, so every line starting with > is omitted. The next step is to convert reads to k-mers. This function accepts reads and the value of k so that the dictionary returned has every k-mer in it as keys and values are the number of occurrences of the k-mer in the read. The obtained k-mers are used to prepare edges next. A set called 'edges' is made containing all the edges made after checking the overlapping k-mers. Edges is a set of two-element tuples with the two k-1-mers that make up the k-mer. Now, the edges are used to plot de Bruijn graph using a Python module called toyplot. Also, the acquired edges are converted to a dictionary so that it can be used to make the graph data structure and traverse conforming to breadth-first traversal.An empty list for keeping track of visited nodes and a queue to keep track of BFS traversal elements are initialised. The graph is iterated from a given node, and as the name suggests, all the elements in a level is traversed first before moving to the next level of the graph. The elements are appended to a list which is finally printed.

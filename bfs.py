read = "CGCAAAAGCCAAGATAACGGGCCAATCCATATTGATATCCAACATGTATACAATTGGGACGAACCATTCTTTTTATCCTTTCTAAACTTTCTTCAAACAA"

k = input("Enter the value of k : ")
k = int(k)
graph = {}

for x in range(len(read)-k+1):
    kmer = read[x:x+k]
    #print(kmer+" ")
    if not kmer in graph.keys():
        graph[kmer] = []
    for keys in graph.keys():
        suffix = keys[-(k-1):]
        prefix = kmer[:(k-1)]
        if suffix == prefix:
            if not kmer in graph[keys]:
                graph[keys].append(kmer)

visited = []  # List for visited nodes.
queue = []  # Initialize a queue

def bfs(visited, graph, node, k):  # function for BFS
    visited.append(node)
    queue.append(node)
    contig = ""

    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        #print(m, end=" ") #prints node acc to BFS

        for neighbour in graph[m]:
            if len(graph[m]) > 1 and contig != "":
                print(contig + " is contig") #prints contig
                contig = ""

            else:
                if(len(contig) < k):
                    contig += neighbour
                else:
                    contig += neighbour[-1]
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("Following is the Breadth-First Search")
bfs(visited, graph, 'CAA', 3)

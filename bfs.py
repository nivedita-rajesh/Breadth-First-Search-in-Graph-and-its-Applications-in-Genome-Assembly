file = open('data1/short_1_dummy.fasta', 'r')
reads = []
lines = file.readlines()
for i in range(0, len(lines)):
    if(i % 2 != 0):
        reads.append(lines[i])

file.close()

k = input("Enter the value of k : ")
k = int(k)
graph = {}

for read in reads:
    read = read.rstrip(read[-1])
    for x in range(len(read)-k+1):
        kmer = read[x:x+k]
        if not kmer in graph.keys():
            graph[kmer] = []
        for keys in graph.keys():
            suffix = keys[-(k-1):]
            prefix = kmer[:(k-1)]
            if suffix == prefix:
                if not kmer in graph[keys]:
                    graph[keys].append(kmer)
#print(graph)


visited = []  # List for visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node, k):  # function for BFS
    visited.append(node)
    queue.append(node)
    contig = ""

    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        #print(m, end=" ")

        for neighbour in graph[m]:
            if len(graph[m]) > 1 and contig != "":
                print(contig + " is contig")
                contig = ""

            else:
                if(len(contig) < k):
                    contig += neighbour
                else:
                    contig += neighbour[-1]
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("The contigs are: ")
bfs(visited, graph, list(graph.keys())[0], k)
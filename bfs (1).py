read = "CGCAAAAGCCAAGATAACGGGCCAATCCATATTGATATCCAACATGTATACAATTGGGACGAACCATTCTTTTTATCCTTTCTAAACTTTCTTCAAACAA"

k = input("Enter the value of k : ")
k = int(k)
kmerset = {}
# print(len(string)-k+1)
for x in range(len(read)-k+1):
    kmer = read[x:x+k]
    #print(kmer+" ")
    if not kmer in kmerset.keys():
        kmerset[kmer] = []
    for keys in kmerset.keys():
        suffix = keys[-(k-1):]
        prefix = kmer[:(k-1)]
        if suffix == prefix:
            if not kmer in kmerset[keys]:
                kmerset[keys].append(kmer)

print(kmerset)
graph = kmerset
# graph = {
#     'CAA': ['AAG'],
#     'AAG': ['AGT'],
#     'AGT': ['GTC', 'GTT'],
#     'GTC': ['TCC'],
#     'TCC': ['AAT'],
#     'GTT': ['TTA'],
#     'TTA': ['AAT'],
#     'AAT': []

# }

visited = []  # List for visited nodes.
queue = []  # Initialize a queue
contigs = []


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


print("Following is the Breadth-First Search")
bfs(visited, graph, 'CAA', 3)

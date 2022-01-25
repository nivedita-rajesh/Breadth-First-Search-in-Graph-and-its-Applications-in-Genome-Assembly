# -*- coding: utf-8 -*-
"""BFS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QS3aRr-EkaEsGNNmB4K4qN9EN-Z06xya
"""

file=open('data1\short_1.fasta','r')
reads=[]
lines=file.readlines()
for i in range(0,len(lines)):
  if(i%2!=0):
    reads.append(lines[i])
  else:
    pass

file.close()

k = input("Enter the value of k : ")
k = int(k)
graph = {}

for read in reads:
  read=read.rstrip(read[-1])
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
print(graph)
#print(len(graph))
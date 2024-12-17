import sys

file = open(sys.argv[1])
dna_str = file.read()

A = dna_str.count("A")
C = dna_str.count("C")
G = dna_str.count("G")
T = dna_str.count("T")
print(A, C, G, T)
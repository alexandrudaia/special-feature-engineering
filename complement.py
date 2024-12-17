import sys

file = open(sys.argv[1])
string = file.read()
string=string.split('\n')[0]
string_complement=[]
 
complements={'A':'T','T':'A','G':'C','C':'G'}
n=len(string)-1
while n>=0:
     string_complement.append(complements[string[n]])
     n=n-1
print(''.join(string_complement))
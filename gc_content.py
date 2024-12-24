import sys
file=open('rosalind_gc.txt')
string=file.read()
def gc_content(string):
    n_g=string.count('G')
    n_c=string.count('C')
    n_gc=n_g+n_c
    return n_gc/len(string)*100

ids=[]
dnas=[]
for i in range(len(string.split('>'))):
    ids.append(string.split('>')[i].split('\n')[0])
    dnas.append(",".join(string.split('>')[i].split('\n')[1:len(string.split('>')[1].split('\n'))-1]))
dnas=[dna.replace(',','')for dna in dnas]
ids=ids[1:]
dnas=dnas[1:]
for dna in dnas :
    gcs_contents.append(gc_content(dna))
idx_max=gcs_contents.index(max(gcs_contents))
print(ids[idx_max])
print(max(gcs_contents))
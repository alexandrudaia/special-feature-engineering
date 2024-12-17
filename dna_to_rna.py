import sys
file=open(sys.argv[1])
string=file.read()
rna=''
for s in range(len(string)) :
    if string[s]=='T':
        rna=rna+'U'
    else:
        rna=rna+string[s]
print(rna)
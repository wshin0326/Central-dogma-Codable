dna = input("Enter your DNA :")
rna = ""

for i in dna:
    if i not in 'ATGC':
        print("Invalid")
        break
    if i == 'A':
        rna += 'U'
    elif i == 'C':
        rna += 'G'
    elif i == 'T':
        rna += 'A'
    else:
        rna += 'C'

print('Converted RNA:' + rna)

def translate(dna):

    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
        }
    primary =""
    if len(dna)%3 == 0:
        for n in range(0, len(dna), 3):
            codon = dna[n:n + 3]
            primary+= table[codon]
        return primary
print(translate(dna))
second = translate(dna)
for i in range(len(second)):
    if second[i] == '_':
        second = second[:i]
        break
print (second)

def countscore(second):
    table1 = {
        'R':['positive polar',1],
        'H':['positive polar',1],
        'K':['positive polar',1],
        'D':['negative polarn',1],
        'E':['negative polarn',1],
        'S':['Polar uncharged',1],
        'T':['Polar uncharged',1],
        'N':['Polar uncharged',1],
        'Q':['Polar uncharged',1],
        'C':['Special',0],
        'G':['Special',0],
        'P':['Special',0],
        'A':['Special',0],
        'V':['nonpolar',-1],
        'I':['nonpolar',-1],
        'L':['nonpolar',-1],
        'M':['nonpolar',-1],
        'F':['nonpolar',-1],
        'Y':['nonpolar',-1],
        'W':['nonpolar',-1],
        }
    Secondary=""
    score= 5
    much = 7
    if len(second) >= 36:
        for i in range(len(second)-6):
            if table1[second[i]]==table1[second[i+6]]:
                score +=1
                much += 1
    if 'A' in second or 'L' in second:
        score += 2
        much += 1
    if len(second) <= 72:
        score += 1
        much += 1
    else: 
        score -= 1
        much += 1
    for i in range(len(second)-1):
        if table1[second[i]][1]*table1[second[i+1]][1] == -1:
            score -= 1
            much += 1
        if table1[second[i]][1]*table1[second[i+1]][1] == 1 and table1[second[i]][0]!=table1[second[i+1]][0]:
            score -= 1
            much += 1
    if 'I' in second or 'V' in second:
        score -= 1
        much += 1
    if 'P' in second or 'G' in second:
        score -= 2
        much += 1
    return score,much

finalscore,finalmuch = countscore(second)

final = (finalscore/finalmuch) * 100
final2 = str(round(final,2))
if final <= -10:
    print("This amino acid sequence will likely to be Beta Sheet with " + str(float(final2)*-1) +" percent.")
elif final >= 10:
    print("This amino acid sequence will likely to be Alpha Helix with " + final2 + " percent.")
else:
    print("This amino acid sequence will likely to be Tertiery Structure containing a loop or terminated amino acid sequence with " + str(100-float(final2)) + " percent.")
    

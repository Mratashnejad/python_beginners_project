
import sys
import stdio




def isGene(dna):
    if len(dna % 3 == 0) : return False
    if not dna.startwich('ATG') : return False
    for i in range(len(dna) -  3):
        if dna[i:i+3] == 'TGA' or dna[i:i+3] == 'TAA' or dna[i:i+3] == 'TGA' : return False

    if dna.endwich('TGA') or dna.endwich('TAA') or dna.endwich('TGA'): return True

    return False



def main():
    start = sys.argv[1]
    stop  = sys.argv[2]
    genome = stdio.fetch()
    begging = -1
    for i in range(len(genome) -2):
        condon = genome[i:i+3]
        if condon == start : begging = i
        if condon == stop and begging != -1:
            gene = genome[begging:+3 :1]
            if len(gene) % 3 == 0 :
                print(gene)
                beg = -1

if __name__ == '__main__':
    main()



#############
#           python code.py ATG TAG < gene.txt
#############
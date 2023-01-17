import stdio 



def translate(dna):
    dna = dna.upper()
    rna = dna.replace("T" ,"U")
    return rna


if __name__ == '__main__':
    dna = input("please inter your DNA string :")
    rna = translate(dna)
    print(rna)
    


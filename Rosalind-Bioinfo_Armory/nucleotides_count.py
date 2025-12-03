
def nucleotides_count (seq):
    if len(seq) > 1000:
        throw("sequence length exceeded 1k")
    else:
        seq.upper()
        A = str(seq.count("A"))
        T = str(seq.count("T"))
        C = str(seq.count("C"))
        G = str(seq.count("G"))
        result = A+" "+C+" "+T+" "+G
        return result



sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
print(nucleotides_count(sequence))


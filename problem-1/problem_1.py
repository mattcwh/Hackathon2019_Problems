#Problem
#A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

#An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

#Given: A DNA string s of length at most 1000 nt.

#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

#Sample Dataset
#AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

#Sample Output
#20 12 17 21

def BaseCounter(seq):
    a = 0
    t = 0
    c = 0
    g = 0
    err = []
    for pos, base in enumerate(seq):
        if base.upper() == "A":
            a += 1
        elif base.upper() == "T":
            t += 1
        elif base.upper() == "C":
            c += 1
        elif base.upper() == "G":
            g += 1
        else:
            err.append(pos + 1)

    print("A:%d T:%d C:%d G:%d Error positions:%s" % (a, t, c, g, err))

seq_1 = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGApGTGTCTGATAGCAGCppw"
BaseCounter(seq_1)

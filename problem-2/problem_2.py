#Problem
#In a weighted alphabet, every symbol is assigned a positive real number called
#a weight. A string formed from a weighted alphabet is called a weighted string,
#and its weight is equal to the sum of the weights of its symbols.

#The standard weight assigned to each member of the 20-symbol amino acid alphabet
#is the monoisotopic mass of the corresponding amino acid.

#Given: A protein string P of length at most 1000 aa.

#Return: The total weight of P. Consult the monoisotopic mass table.

#Sample Dataset
#SKADYEK

#Sample Output
#821.392

aa_mass = {}
with open(doc, 'r') as readin:
    read = csv.reader(readin, delimiter="   ")
    for row in read:
        aa_mass[row[0]] = row[1]


aa_mass = dict([["A", 71.03711], ["C", 103.00919], ["D", 115.02694], ["E", 129.04259], ["F", 147.06841], ["G", 57.02146], ["H", 137.05891], ["I", 113.08406], ["K", 128.09496], ["L", 113.08406], ["M", 131.04049], ["N", 114.04293], ["P", 97.05276], ["Q", 128.05858], ["R", 156.10111], ["S", 87.03203], ["T", 101.04768], ["V", 99.06841], ["W", 186.07931], ["Y", 163.06333]])

def ProtWeigher(proseq):
    total_weight = 0
    for aa in proseq:
        total_weight += aa_mass[aa.upper()]
    return total_weight

proseq_1 = "SKADYEK"
weight_1 = ProtWeigher(proseq_1)
print(weight_1)

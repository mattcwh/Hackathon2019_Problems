#Problem
#Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s (as a result, t must be no longer than s).

#Find all locations of t as a substring of s.

#Given: Two DNA strings s and t (each of length at most 1 kbp).

#Return: All locations of t as a substring of s.

#Sample Dataset
#GATATATGCATATACTT
#ATAT
#Sample Output
#2 4 10

s = "GATATATGCATATACTT"
t = "ATAT"

import re

pattern = "(?=(" + min(t, s) + "))" #lookahead for overlapping matches

for motif in re.finditer(pattern, max(t, s)):
    print(motif.start() + 1)

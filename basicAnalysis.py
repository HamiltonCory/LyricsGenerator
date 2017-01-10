import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist
import os
from numpy.core.defchararray import isalpha


corpus_location='C:\\Users\\Jeff\\git\\LyricsYo\\runDataset'
print(corpus_location)
testCorpus = PlaintextCorpusReader(corpus_location, '.*')
words = testCorpus.words()
fdist = FreqDist(words)
vocab = fdist.keys()
a = [w for w in words if isalpha]
print (a)

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0

for w in a:
    if 'chevy' in w:
        n1 = n1 + 1
    if 'girl' in w:
        n2 = n2 + 1
    if 'truck' in w:
        n3 = n3 + 1
    if 'beer' in w:
        n4 = n4 + 1
    if 'love' in w:
        n5 = n5 + 1

print(n1)
print(n2)
print(n3)
print(n4)
print(n5)

n1 = n1/len(a)
n2 = n2/len(a)
n3 = n3/len(a)
n4 = n4/len(a)
n5 = n5/len(a)
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)

#Chevy
#Girl
#Downtown
#Pickup
#Truck
#Beer
#Love

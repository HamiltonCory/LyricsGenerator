import nltk
from nltk.corpus import PlaintextCorpusReader
import os

corpus_location='C:\\Users\\Jeff\\git\\LyricsYo\\testDataset'
print(corpus_location)
testCorpus = PlaintextCorpusReader(corpus_location, '.*')
print(testCorpus.words())
print(len(testCorpus))

import nltk
from nltk import bigrams
from nltk import ngrams
from nltk.corpus import PlaintextCorpusReader

corpus_location='C:\\Users\\Jeff\\git\\LyricsYo\\runDataset'
testCorpus = PlaintextCorpusReader(corpus_location, '.*')
n = 2
sixgrams = ngrams(testCorpus.raw().lower().split(), n)
for gram in sixgrams:
  print (gram)

import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist
import os
import collections
from numpy.core.defchararray import isalpha
from nltk.tokenize import WhitespaceTokenizer
from nltk import word_tokenize


corpus_location='C:\\Users\\Jeff\\git\\LyricsYo\\runDataset'
print(corpus_location)
testCorpus = PlaintextCorpusReader(corpus_location, '.*')
words = word_tokenize(testCorpus.raw())
# words = WhitespaceTokenizer().tokenize(testCorpus.raw())
# words = testCorpus.words()
counts = collections.Counter(words)
# print (counts)
fdist = FreqDist(words)
vocab = fdist.keys()
a = [w for w in words if isalpha]
# print (a)
print ("Number of words:", len(a))
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

word = [w for w in fdist.keys() if isalpha]
fdist2 = FreqDist([len(w) for w in a])
# fdist2.plot(cumulative = True)

# cfd = nltk.ConditionalFreqDist((len(word)) for w in testCorpus.raw())
# cfd.plot(cumulative = True)

longest_len = max([len(w) for w in a]) + 1
l = [0] * longest_len
print (longest_len)

#Prints words over length 10
for w in a:
    num = l[len(w)]
    num = num + 1
    l[len(w)] = num
    if len(w) > 12:
        print(w)

# print(nltk.pos_tag(words))
partsOfSpeech = nltk.pos_tag(words)
print (partsOfSpeech[1])
posDict = {}
for tag in partsOfSpeech:
    pos = tag[1]
    word = tag[0]
    if pos in posDict:
        wordCountDict = posDict[pos]
        if word in wordCountDict:
            # print ("Got here, count is: " + str(wordCountDict[word]) + " incrementing...");
            wordCountDict[word] = wordCountDict[word] + 1
        else:
            wordCountDict[word] = 1;
    else:
        posDict[pos] = {}
        posDict[pos][word] = 1;

print(posDict)
def getMostFrequentWordInPOS(pos):
    maxWord = "";
    if pos in posDict:
        maxOccur = 0;
        for word in posDict[pos]:
            if(posDict[pos][word] > maxOccur):
                maxOccur = posDict[pos][word]
                maxWord = word
        posDict[pos][maxWord] = 0
    return maxWord
# print(len(posDict.keys())) 40 parts of speech


corpus_location2='C:\\Users\\Jeff\\git\\LyricsYo\\songLyric'
print(corpus_location)
lyricCorpus = PlaintextCorpusReader(corpus_location2, '.*')
words2 = WhitespaceTokenizer().tokenize(lyricCorpus.raw())
partsOfSpeech = nltk.pos_tag(words2)
newLyrics = ""
for w in partsOfSpeech:
    nextWord = getMostFrequentWordInPOS(w[1])
    if nextWord == "t":
        print(w)
    newLyrics = newLyrics + " " + nextWord
print (newLyrics)

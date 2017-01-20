import nltk
from random import randint
from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist
import os
import pickle
import collections
from numpy.core.defchararray import isalpha
from nltk.tokenize import WhitespaceTokenizer
from nltk import word_tokenize
from nltk import ngrams


corpus_location='C:\\Users\\Jeff\\git\\LyricsYo\\runDataset'
print(corpus_location)
testCorpus = PlaintextCorpusReader(corpus_location, '.*')
# words = word_tokenize(testCorpus.raw())
# words = WhitespaceTokenizer().tokenize(testCorpus.raw())
words = WhitespaceTokenizer().tokenize(testCorpus.raw().lower())
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

# print(n1)
# print(n2)
# print(n3)
# print(n4)
# print(n5)

n1 = n1/len(a)
n2 = n2/len(a)
n3 = n3/len(a)
n4 = n4/len(a)
n5 = n5/len(a)

# print(n1)
# print(n2)
# print(n3)
# print(n4)
# print(n5)

word = [w for w in fdist.keys() if isalpha]
fdist2 = FreqDist([len(w) for w in a])
# fdist2.plot(cumulative = True)

# cfd = nltk.ConditionalFreqDist((len(word)) for w in testCorpus.raw())
# cfd.plot(cumulative = True)

longest_len = max([len(w) for w in a]) + 1
l = [0] * longest_len
print (longest_len)

# #Prints words over length 10
# for w in a:
#     num = l[len(w)]
#     num = num + 1
#     l[len(w)] = num
#     if len(w) > 12:
#         print(w)

# print(nltk.pos_tag(words))
partsOfSpeech = nltk.pos_tag(words)
#print (partsOfSpeech[1])
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
#Lottery system
def getRandomWord(pos):
    # print ("Starting lottery")
    # print ("POS", pos)
    numTotal = 0
    # This catches any unseen parts of speech
    localPOSList = posDict.get(pos, "TEMP")
    if (localPOSList is 'TEMP'):
        return "TEMP"
    # print ("Got here")
    # print (localPOSList)
    for tuple in localPOSList:
        # print (localPOSList[tuple])
        numTotal = numTotal + localPOSList[tuple]

    # print ("Total size of lottery is", numTotal)
    pick = randint(0, numTotal)
    # print ("Pick is:", pick)
    for tuple in localPOSList:
        pick = pick - localPOSList[tuple]
        if pick <= 0:
            # print (pick)
            # print ("Tuple", tuple)
            return tuple

def split_and_keep(s, sep):
   if not s: return [''] # consistent with string.split()

   # Find replacement character that is not used in string
   # i.e. just use the highest available character plus one
   # Note: This fails if ord(max(s)) = 0x10FFFF (ValueError)
   p=chr(ord(max(s))+1)

   return s.replace(sep, sep+p).split(p)

#TODO Cache?
def ngramSearch(input, size):
    grams = ngrams(testCorpus.raw().lower().split(), size)
    for gram in grams:
        if (input[0] is gram[0]):
            print ("Found")
            print (gram)
            return gram
    #   None found
    return "None"

corpus_location2='C:\\Users\\Jeff\\git\\LyricsYo\\songLyric'
print(corpus_location)
lyricCorpus = PlaintextCorpusReader(corpus_location2, '.*')
words2 = WhitespaceTokenizer().tokenize(lyricCorpus.raw())
partsOfSpeechForSong = nltk.pos_tag(words2)
newLyrics = ""
wordsString = lyricCorpus.raw()
words = wordsString.split('\r\n')
if "\n" in words:
    print ("There's a newline in variable the string")
#Prints characters
print (words)
print ("printing array")
print (words[0])
# for s in words:
#    print(split_and_keep(s, '\r\n'))
# for c in words:
#     print (c)
for line in words:
    partOfSpeech = nltk.pos_tag(line.split())
    print (partOfSpeech)
    for w in partOfSpeech:
        print (w[0])
        ngram = ngramSearch(w[0], len(partOfSpeech))
        if ngram != "None":
            nextWord = ngram
        nextWord = getRandomWord(w[1])
        # print (nextWord)
        if nextWord == "t":
            print(w)
        newLyrics = newLyrics + " " + nextWord
    newLyrics = newLyrics + "\r\n"
print (newLyrics)
# for w in partsOfSpeechForSong:
#     nextWord = getRandomWord(w[1])
#     # print (nextWord)
#     # print (w[0])
#     if nextWord == "t":
#         print(w)
#     newLyrics = newLyrics + " " + nextWord
# print (newLyrics)

pickle.dump(posDict, open( "posDictPickle.p", "wb" ) )
#To load posDict = pickle.load( open( "posDictPickle.p", "rb" ) )

import random

# Generate tokens
# Tuple
def getMostFrequentWordInPOS(input):
    print ("Starting lottery")
    numTotal = 0
    for tuple in input:
        numTotal = tuple[0].size

    pick = random.seed(numTotal)
    for tuple in input:
        pick = pick - tuple[0].size
        if pick <= 0
            return pick

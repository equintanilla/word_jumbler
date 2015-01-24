
wordDictionary = set()
def calculatePerms(word):
    perms = []
    wordsFound = set()
    INDECES_UNUSED = 'ixUnused'
    VALUE = 'val'
    # initialize perms
    currentInitDict = {}
    perms.insert(0, currentInitDict)
    currentInitDict[INDECES_UNUSED] = range(0, len(word))
    currentInitDict[VALUE] = ''

    while (len(perms) > 0):
        currentOldPerm = perms.pop()
        for j in currentOldPerm[INDECES_UNUSED]:
            currentPerm = currentOldPerm[VALUE] + word[j]
            if isWord(currentPerm):
                wordsFound.add(currentPerm)
            #only enqueue if word still has not used all of letters
            if len(currentPerm) < len(word):
                newPerm = {}
                newPerm[VALUE] = currentPerm
                newPerm[INDECES_UNUSED] = list(currentOldPerm[INDECES_UNUSED])
                newPerm[INDECES_UNUSED].remove(j)
                perms.insert(0, newPerm)

    print 'Words found:'
    for wordFound in wordsFound:
        print wordFound
    print


def loadWordDictionary():
    f = open('en_US.dic')
    for line in f:
        line = line.strip()
        lineSplit = line.split('/')
        word = lineSplit[0]
        wordDictionary.add(word)


def isWord(word):
    return word in wordDictionary
loadWordDictionary()

def init():

    while True:
        print 'Word Jumble Solver, type your word and then press Enter'
        input = raw_input()
        calculatePerms(input.strip())



init()
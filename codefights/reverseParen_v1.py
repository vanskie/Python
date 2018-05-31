def reverseParentheses(s):
    sList = [x for x in s]
    copyList = sList[:]
    parenSlices = []
    parenSlicePos = -1
    reverseSlices = []
    
    #Find where the parentheses are
    for char in range(len(sList)):
        if sList[char] == '(':
            parenSlicePos += 1
            parenSlices.insert(parenSlicePos, [char+1])
        if sList[char] == ')':
            parenSlices[parenSlicePos].insert(1, char)
            parenSlicePos -= 1
    
    #reverse all words in parentheses and put them in a list: reversedWords[]
    reversedWords = []
    for sliced in range(len(parenSlices)-1, -1, -1):
        reversedChars = ''
        for reverseWord in range(parenSlices[sliced][1], parenSlices[sliced][0]-2, -1):
            reversedChars += sList[reverseWord]
        reversedWords.append(reversedChars)
        
    if len(reversedWords) > 1:
    
        #main sentance is set to a variable
        #the words left in the reverse list are reversed again
        mainSentence = reversedWords.pop(-1)
        """
        for word in range(len(reversedWords)):
            doubleReverse = ''
            discardWord = reversedWords.pop(word)
            for letter in range(len(discardWord)-1, -1, -1):
                doubleReverse += discardWord[letter]
            
            reversedWords.insert(word, doubleReverse)
        """
        #from the slice coordinates starting from 1 because 0 is the main sentance insert the words from reversedWords into main sentance
        #go through main sentance in reverse ... dude trust me
        combinedNewList = []
        reversePositionCounter = 0
        for slice in range(len(parenSlices)-1, 1, -1):
            for letter in range(len(mainSentence)-1, 1, -1):
                reversePositionCounter += 1
                combinedNewList.append(mainSentence[letter-1])
                if reversePositionCounter == parenSlices[slice][0]:
                    combinedNewList.append(reversedWords[reversePositionCounter])
                    reversePositionCounter += 1
                    letter -= 1
                    if reversePositionCounter == parenSlices[slice][1]:
                        break
                #if mainSentence[letter] == '(':
                 #   break
                
    return combinedNewList
    
    #This works
    #Now make it work in a loop for all parenSlices
    """
    testReverseWord = ''
    for lSlice in range(parenSlices[1][1]-1, parenSlices[1][0]-1, -1):
        testReverseWord += sList[lSlice]
    """
    #puts all the reversed words in one sList
    #make all reversable parts destinguishable
    """
    for lSlice in parenSlices:
        for sliceRange in range(lSlice[0], lSlice[1]):
            reverseSlices.insert(0, sList[sliceRange])
    """ 
    """
    for reverseSlice in range(parenSlices[1][0], parenSlices[1][1]):
        copyList[parenSlices[1][1] + reverseSlice] = sList[reverseSlice]
    """

    #return sList[parenSlices[1][0]:parenSlices[1][1]]
    #return reversedWords

string = '(hello (darkness) my old friend)'
string2 = '(hello (darkness) (my) old friend)'
print(reverseParentheses(string))
print(reverseParentheses(string2))
        

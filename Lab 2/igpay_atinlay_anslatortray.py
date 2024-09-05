import random
def translator(word):
    wordlist = list(word)
    if wordlist[0] in ["a", "e", "i", "o", "u"]:
        suffix = random.choice(["way", "nay", "hay", "yay"])
        word = (word + suffix)
        '''I was on the pig latin page on Wikipedia, and
        it said only the suffix was changed on words
        that start with vowels. The original word is not
        clipped at its beginning.'''
    elif (wordlist[0] + wordlist[1]) in ["bl", "br", "ch", "ck", "cl", 
                                            "cr", "dr", "fl", "fr", "gh", 
                                            "gl", "gr", "ng", "ph", "pl", 
                                            "pr", "qu", "sc", "sh", "sk", 
                                            "sl", "sm", "sn", "sp", "st", 
                                            "sw", "th", "tr", "tw", "wh", 
                                            "wr."]:
        word = (word[2:] + wordlist[0] + wordlist[1] + "ay")
        #removes the first 2 letters from the word, adds them to the end and concatenates "ay"
    else:
        word = (word[1:] + wordlist[0] + "ay")
        #removes only the first letter
    return word
    
wordofchoice = input("Choose a word you want to translate:")
print(translator(wordofchoice))
#Sources Used: https://www.geeksforgeeks.org/python-program-convert-string-list/
#https://www.w3schools.com/python/python_ref_list.asp
#https://www.w3schools.com/python/python_ref_string.asp
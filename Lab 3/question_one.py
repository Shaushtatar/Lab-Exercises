#Resources used
#https://www.w3schools.com/python/python_ref_list.asp -- for line 15, 17
import random
class StringListModifier:
    def __init__(self, wordlist):
        self.wordlist = wordlist
    def withoutVowels(self):
        newwordlist = []
        for i in self.wordlist:
            if i[0] not in ["a","e","i","o","u"]:
                newwordlist.append(i)
        return newwordlist #List without vowel-starting words
    def randthree(self):
        wordlist_copy = self.wordlist
        r1 = random.choice(wordlist_copy)
        wordlist_copy.remove(r1) #Avoids duplicates in list
        r2 = random.choice(wordlist_copy)
        wordlist_copy.remove(r2)
        r3 = random.choice(wordlist_copy)
        return [r1,r2,r3]
    def blank_checker(self):
        nospacelist = []
        for i in self.wordlist:
            spaceless = i.replace(" ","")
            #https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/
            nospacelist.append(spaceless)
        return nospacelist
    def addshuffledlist(self):
        #shuffle learned from https://www.w3schools.com/python/module_random.asp
        shuffledlist = self.wordlist
        random.shuffle(shuffledlist)
        self.wordlist.append(shuffledlist)
        print(self.wordlist)
    def printupper(self):
        for i in self.wordlist:
            print(i.upper())
    def abcsort(self):
        sorted = self.wordlist
        sorted.sort()
        return sorted
    def printandchoose(self):
        print(self.wordlist)
        unwanted = input("Name a word on the list if you would like it to be removed from the list:")
        if unwanted in self.wordlist:
            self.wordlist.remove(unwanted)
        print("The new word list is:\n" + str(self.wordlist))
    def add(self): #adds an item of choice to list
        addedword = input("Input what item would you like to add:")
        self.wordlist.append(addedword)
        print(self.wordlist)

test_list = ["apple",
             "banana",
             "fried chicken",
             "yogurt",
             "radish",
             "coca cola",
             "hamburger",
             "ice pop",
             "lemonade",
             "onion",
             "danish",
             "sandwich bread",
             "gatorade",
             "cherry pie"
             ]

slm = StringListModifier(test_list)
print(slm.withoutVowels())
print(slm.randthree())
print(slm.blank_checker())
slm.printupper()
print(slm.abcsort())
slm.printandchoose()
slm.add()
slm.addshuffledlist()
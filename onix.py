#Imports:
from random import randint
import json

#Constants:
MAXLENGTH = 32
MINLENGTH = 8

#Translations:
toDigits = {'l': 1, 'z':2, 'e':3, 'q':4, 's':5, 'g':6, 'g':9, 'o':0}
toSign = {'i':'!', 'a':'@', 'h':'#', 's':'$', 'r':'&'}

class Onix:
    #Functions:
    def __init__(self, length="8", plaintext="", options="123", banned=""):
        plaintext = plaintext.lower()
        banned = banned.lower()
        
        self.transFuncs = [self.getCapital, self.getDigit, self.getSign, self.getSmall]
        self.banned = banned.split(" ")

        if len(plaintext) == 0:
            if int(length) < 8:
                return "ERROR: Length is lower than 8."
            elif int(length) > 32:
                return "ERROR: Length is higher than 32."
            else:
                self.length = int(length)
                self.plaintext = self.fromDic(self.length)
        else:
            self.length = len(plaintext)
            self.plaintext = plaintext

        if options == "":
            self.options = "123"
        else:
            self.options = options

        return None


    def jsonOut(self):
        jsonDictionary = {'plaintext':self.plaintext, 'length':self.length, 'cyphertext':self.toPass(self.plaintext, self.options)}
        return json.dumps(jsonDictionary)


    def onix(self):
        return self.jsonOut()


    def fromDic(self, length):
        if (length > MAXLENGTH) or (length < MINLENGTH):
            return "error"
        else:        
            words = open("dictionary.txt", "rb").read().split(' ')

            while True:
                word = words[randint(0, (len(words)-1))]
                if len(word) == length:
                    return word


    #Translation Functions:
    def getCapital(self, letter):
        if letter.upper() in self.banned:
            return letter
        else:
            return letter.upper()


    def getDigit(self, letter):
        try:
            if str(toDigits[letter]) in self.banned:
                return letter
            else:
                return str(toDigits[letter])
        except KeyError:
            return letter


    def getSign(self, letter):
        try:
            if toSign[letter] in self.banned:
                return letter
            else:
                return toSign[letter]
        except KeyError:
            return letter

    def getSmall(self, letter):
        return letter
    

    def toPass(self, plaintext, options):
        self.cyphertext = ""
        self.localFuncs = []

        if "1" in options:
            self.localFuncs.append(self.transFuncs[0])
        if "2" in options:
            self.localFuncs.append(self.transFuncs[1])
        if "3" in options:
            self.localFuncs.append(self.transFuncs[2])

        self.localFuncs.append(self.transFuncs[3])

        for letter in plaintext:
            self.cyphertext += self.localFuncs[randint(0, (len(self.localFuncs)-1))](letter)

        return self.cyphertext
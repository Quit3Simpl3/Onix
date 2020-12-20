from random import randint
import json

# Constants:
MAXLENGTH = 32
MINLENGTH = 8

# Translations:
to_digits = {'l': 1, 'z': 2, 'e': 3, 'q': 4, 's': 5, 'g': 9, 'o': 0}
to_sign = {'i':'!', 'a':'@', 'h':'#', 's':'$', 'r':'&'}

class Onix:
    def __init__(self, length=8, plaintext="", options="123", banned=""):
        try:
            open("dictionary.txt", "r")
        except FileNotFoundError:
            raise FileNotFoundError("The required dictionary.txt file was not found.")

        self.localFuncs = []
        self.cyphertext = ""
        plaintext = plaintext.lower()
        banned = banned.lower()
        
        self.transFuncs = [self.get_capital, self.get_digit, self.get_sign, self.get_small]
        self.banned = banned.split(" ")

        if len(plaintext) == 0:
            if int(length) < 8:
                raise Exception("ERROR: Length is lower than 8.")
            elif int(length) > 32:
                raise Exception("ERROR: Length is higher than 32.")
            else:
                self.length = int(length)
                self.plaintext = self.from_dict(self.length)
        else:
            self.length = len(plaintext)
            self.plaintext = plaintext

        if options == "":
            self.options = "123"
        else:
            self.options = options

    def json_out(self):
        return json.dumps({
            'plaintext':self.plaintext,
            'length':self.length,
            'cyphertext':self.to_password(self.plaintext, self.options)
        })

    def onix(self):
        return self.json_out()

    def from_dict(self, length):
        if (length > MAXLENGTH) or (length < MINLENGTH):
            raise Exception("The length isn't valid.")

        else:
            words = open("dictionary.txt", "rb").read().split(' ')
            while True:
                word = words[randint(0, (len(words)-1))]
                if len(word) == length:
                    return word

    #Translation Functions:
    def get_capital(self, letter):
        if letter.upper() in self.banned:
            return letter
        else:
            return letter.upper()

    def get_digit(self, letter):
        try:
            if str(to_digits[letter]) in self.banned:
                return letter
            else:
                return str(to_digits[letter])

        except KeyError:
            return letter

    def get_sign(self, letter):
        try:
            if to_sign[letter] in self.banned:
                return letter
            else:
                return to_sign[letter]
        except KeyError:
            return letter

    def get_small(self, letter):
        return letter
    

    def to_password(self, plaintext, options):
        for i in range(1, 4): # Check if options include 1, 2, or 3
            if str(i) in options:
                self.localFuncs.append(self.transFuncs[i-1])

        self.localFuncs.append(self.transFuncs[3])

        for letter in plaintext:
            self.cyphertext += self.localFuncs[randint(0, (len(self.localFuncs)-1))](letter)

        return self.cyphertext

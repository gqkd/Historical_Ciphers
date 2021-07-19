
# %%
#caesar cipher
class his_cip:
    def __init__(self):
        self.alf = "abcdefghijklmnopqrstuvwxyz"
        self.alf2 = self.alf*2
        self.len_ = len(self.alf)
        
    def caesar_enc(self,plaintext,key):
        ciphertext = ""
        alpha = self.alf*2
        #replace dots and getting all in lower case
        plaintext = plaintext.lower()
        #control if plain is a string and key is a number
        if isinstance(plaintext,str) and isinstance(key,int) and plaintext.isalpha():
            key = key % self.len_
            for letter in plaintext:
                # #if there is a space
                # if ord(letter)==32:
                #     ciphertext += letter
                # else:
                ciphertext += self.alf2[self.alf2.index(letter)+key]
        else:
            print("ERRORE -> solo lettere (A-Z)")
            return 
        return ciphertext

    def caesar_dec(self,ciphertext,key):
        plaintext = ""
        if isinstance(ciphertext,str) and isinstance(key,int):
            key = key % self.len_
            for letter in ciphertext:
                # #if there is a space
                # if ord(letter)==32:
                #     plaintext += letter
                # else:
                plaintext += self.alf2[self.alf2.index(letter)-key]
        return plaintext

    #encryption with numbers first try
    # def caesar_enc2(self,plaintext,key):
    #     ciphertext = ""
    #     vet=[0,1,2,3,4,5,6,7,8,9]
    #     if isinstance(plaintext,str) and isinstance(key,int):
    #         key = key%26
    #         plaintext = plaintext.replace(".","").lower()
    #         for letter in plaintext:
    #             #if there is a space
    #             if ord(letter)==32:
    #                 ciphertext += letter
    #             elif ord(letter)>=48 and ord(letter)<=57:
    #                 c=(((ord(letter)%48)+key))+48
    #                 ciphertext += chr(c)
    #             else:
    #                 #97 is the unicode position for "a"
    #                 c=(((ord(letter)%97)+key))+97
    #                 ciphertext += chr(c)
    #     return ciphertext           
    
    # def caesar_dec2(self,ciphertext,key):
    #     plaintext = ""
    #     vet=[0,1,2,3,4,5,6,7,8,9]
    #     if isinstance(ciphertext,str) and isinstance(key,int):
    #         key = key%26
    #         for letter in ciphertext:
    #             if ord(letter)==32:
    #                 plaintext += letter
    #             elif ord(letter)>=48 and ord(letter)<=57:
    #                 c=(((ord(letter)%48)-key))+48
    #                 plaintext += chr(c)
    #             else:
    #                 #97 is the unicode position for "a"
    #                 c=(((ord(letter)%97)-key))+97
    #                 plaintext += chr(c)
    #     return plaintext
        
    def vigenere_enc(self,PlainText,key):
            lenPlainText = len(PlainText)
            lenKey = len(key)
            x = int(lenPlainText/lenKey)
            keyMatched = (key*(x+1))[0:(lenPlainText)]
            cipherText = ""
            for x in range(len(keyMatched)):
                letterPlain = PlainText[x]
                letterKey = keyMatched[x]
                cipherLetter = self.caesar_enc(letterPlain,ord(letterKey)%self.len_)
                cipherText += cipherLetter
            return cipherText

    def vigenere_dec(self,cipherText,key):
        lenCipherText = len(cipherText)
        lenKey = len(key)
        x = int(lenCipherText/lenKey)
        keymatched = (key*(x+1))[0:(lenCipherText)]
        PlainText = ""
        for x in range(len(keymatched)):
            letterCipher = cipherText[x]
            letterKey = keymatched[x]
            plainLetter = self.caesar_dec(letterCipher,ord(letterKey)%self.len_)
            PlainText += plainLetter
        return PlainText

#%%
a=his_cip()
plain="porcodio"
key="lemon"
cipher = a.vigenere_enc(plain,key)
print(cipher)
plaint = a.vigenere_dec(cipher,key)
print(plaint)
# %%

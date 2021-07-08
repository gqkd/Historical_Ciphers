
# %%
#caesar cipher
class his_cip:
    def __init__(self):
        pass
    def caesar_enc(self,plaintext,key):
        ciphertext = ""
        vet=[0,1,2,3,4,5,6,7,8,9]
        if isinstance(plaintext,str) and isinstance(key,int):
            key = key%26
            plaintext = plaintext.replace(".","").lower()
            for letter in plaintext:
                if ord(letter)==32:
                    ciphertext += letter
                elif ord(letter)>=48 and ord(letter)<=57:
                    c=(((ord(letter)%48)+key))+48
                    ciphertext += chr(c)
                else:
                    #97 is the unicode position for "a"
                    c=(((ord(letter)%97)+key))+97
                    ciphertext += chr(c)
        return ciphertext           
    
    def caesar_dec(self,ciphertext,key):
        plaintext = ""
        vet=[0,1,2,3,4,5,6,7,8,9]
        if isinstance(ciphertext,str) and isinstance(key,int):
            key = key%26
            for letter in ciphertext:
                if ord(letter)==32:
                    plaintext += letter
                elif ord(letter)>=48 and ord(letter)<=57:
                    c=(((ord(letter)%48)-key))+48
                    plaintext += chr(c)
                else:
                    #97 is the unicode position for "a"
                    c=(((ord(letter)%97)-key))+97
                    plaintext += chr(c)
        return plaintext

a=his_cip()
plain="12abc def"
key=1
cipher = a.caesar_enc(plain,key)
a.caesar_dec(cipher,key)

# %%

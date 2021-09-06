#%%
import json
from string import ascii_lowercase
#%%
#creation of the list of the alphabet
alphabet = list(ascii_lowercase)
#configuration of rotors, the key is the notch position
rotor_I_conf = {"q":"jgdqoxuscamifrvtpnewkblzyh"}


#settings of enigma
steckerbrett = {" ":" ","b":"a","e":"z"}
#doubling the dict, b->a a->b
for value in range(len(list(steckerbrett.values()))):
    steckerbrett[list(steckerbrett.values())[value]]=list(steckerbrett.keys())[value]

#grund and ring stellung
grundstellung = ["a","a","a"]

def rotate(rotors):
    slow = rotors[0]
    middle = rotors[1]
    fast = rotors[2]
    rotors_alph = [alphabet[slow],alphabet[middle],alphabet[fast]]
    rotors = [slow, middle, fast]
    print(rotors)
    print(rotors_alph)

    #if the 1st rotor is in notch rotate the 2nd
    if fast % 16 == 0 and fast != 0:
        fast += 1
        middle += 1
        rotors = print_rotors(fast, middle, slow)
        return rotors
 
    #if the 2nd rotor is in notch rotate the 2nd & the 3rd
    elif middle % 16 == 0 and middle != 0:
        fast += 1
        slow += 1
        middle += 1
        rotors = print_rotors(fast, middle, slow)
        return rotors
    else:
        fast +=1    

    #reset rotor
    if fast == 26:
        fast = 0
    if middle == 26:
        middle = 0
    if slow == 26:
        slow = 0   
    rotors = [slow, middle, fast]
    # print(rotors)
    # rotors_alph = [alphabet[slow],alphabet[middle],alphabet[fast]]
    # print(rotors_alph,'\n')
    return rotors

def print_rotors(fast, middle, slow):
    rotors = [slow, middle, fast]
    print(rotors)
    rotors_alph = [alphabet[slow],alphabet[middle],alphabet[fast]]
    print(rotors_alph,'\n')
    return rotors

def en_stage2(grundstellung, ringstellung, letter):
    #grundstellung
    pass

#steckerbrett encryption
def en_stage1(steckerbrett,letter):
    if letter in list(steckerbrett.keys()):
        return steckerbrett[letter]

def shift(plaintext,key,alphabet):
    ciphertext = ""
    alphabet = alphabet*2
    print(alphabet,alphabet.index(plaintext)+key,alphabet[alphabet.index(plaintext)+key])
    key = key % 26
    ciphertext += alphabet[alphabet.index(plaintext)+key]
    return ciphertext

def encrypt(letter, rotors, rotor_conf):
    rotors = rotate(rotors)
    for rotor in rotors:
        cipher_letter = shift(letter,rotor,list(rotor_conf.values())[0])
        print(rotor)
        print(cipher_letter)
# %%
slow = 0
middle = 0
fast = 0
rotors = [slow, middle, fast]

encrypt('a',rotors,rotor_I_conf)
# %%

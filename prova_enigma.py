#%%
import json
from string import ascii_lowercase

#creation of the list of the alphabet
alphabet = list(ascii_lowercase)
alphabet = alphabet*2
#configuration of rotors, the key is the notch position
#from 6th to 8th there are 2 notch positions
rotor_I    = {"q" :"ekmflgdqvzntowyhxuspaibrcj"}
rotor_II   = {"e" :"ajdksiruxblhwtmcqgznpyfvoe"}
rotor_III  = {"v" :"bdfhjlcprtxvznyeiwgakmusqo"}
rotor_IV   = {"j" :"esovpzjayquirhxlnftgkdcmwb"}
rotor_V    = {"z" :"vzbrgityupsdnhlxawmjqofeck"}
#TODO implementation of double notch rotors
# rotor_VI   = {"zm":"jpgvoumfyqbenhzrdkasxlictw"}
# rotor_VII  = {"zm":"nzjhgrcxmyswboufaivlpekqdt"}
# rotor_VIII = {"zm":"fkqhtlxocbjspdzramewniuygv"}

#configuration of reflectors
ukw_A      = {"":"ejmzalyxvbwfcrquontspikhgd"}
ukw_B      = {"":"yruhqsldpxngokmiebfzcwvjat"}
ukw_C      = {"":"fvpjiaoyedrzxwgctkuqsbnmhl"}
ukw_B_thin = {"":"enkqauywjicopblmdxzvfthrgs"}
ukw_C_thin = {"":"rdobjntkvehmlfcwzaxgyipsuq"}

#settings of enigma
steckerbrett = {" ":" ","b":"a","e":"z"}
#doubling the dict, b->a a->b
for value in range(len(list(steckerbrett.values()))):
    steckerbrett[list(steckerbrett.values())[value]]=list(steckerbrett.keys())[value]

#grund and ring stellung
grundstellung = ["a","a","a"]
#TODO aggiustare quando ruota in notch position data dalla configurazione
def rotate(rotors):
    slow = rotors[0]
    middle = rotors[1]
    fast = rotors[2]
    rotors_alph = [alphabet[slow],alphabet[middle],alphabet[fast]]
    rotors = [slow, middle, fast]
    # print(rotors)
    # print(rotors_alph)

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
def steck(steckerbrett,letter):
    if letter in list(steckerbrett.keys()):
        return steckerbrett[letter]

def shift(plain,rotors,rotors_conf,refl_conf):
    #like the wiring diagram of the original machine, there are two passages
    #first passage is from fast rotor to slow, reverse the rotors for simplicity
    rotors_inv = rotors[::-1]
    rotors_conf_inv = rotors_conf[::-1]

    #alphabet of the reflector
    ref_alphabet = list(refl_conf.values())[0]
    #find the index of the first letter, the input
    index_input = alphabet.index(plain)
    print(f"index_input {plain} {index_input}")
    
    #for all rotors, starting from the fast to the slow, there are steps on the normal
    # alphabet and steps on the rotor alphabet:
    # - in this first step we look for the index of the input into the rotor alphabet,
    #   we find the correspondent letter to the index of the input
    # - find the index of the letter we found into the normal alphabet
    # - reassing the index of the input to the index of the last letter found and restart
    #   the cycle
    #
    # step1 (rotor_alphabet) index_input -> letter_rotor
    # step2 (normal_alphabet) letter_rotor -> index_alphabet
    # step3 index_input=index_alphabet

    for i,rotor_shift in enumerate(rotors_inv):
        print(f"rotor_shift {rotor_shift}")
        rot_alphabet = list(rotors_conf_inv[i].values())[0]

        #step1 index_input -> letter_rotor
        letter_rotor = rot_alphabet[(index_input+rotor_shift)%26]

        index_rotor = rot_alphabet.index(letter_rotor)
        print(f"letter_rotor: {letter_rotor} index_rotor: {index_rotor}")
        
        #step2 letter_rotor -> index_alphabet
        index_alphabet = alphabet.index(letter_rotor)

        letter_alphabet = alphabet[index_alphabet]
        print(f"letter_alphabet: {letter_alphabet} index_alphabet: {index_alphabet}\n")

        #step3
        index_input = index_alphabet-rotor_shift
    
    #reflector, a simple substitution
    letter_reflector = ref_alphabet[index_input]
    index_input = alphabet.index(letter_reflector)

    # print(f"letter_reflector: {letter_reflector} index_reflector: {index_input}\n")

    #now the second passage, from slow to fast
    # step1 (normal_alphabet) index_input -> letter_alphabet
    # step2 (rotor_alphabet)  letter_alphabet -> index_rotor
    # step3 index_input = index_rotor

    for i,rotor_shift in enumerate(rotors):
        print(f"rotor_shift {rotor_shift}")
        rot_alphabet = list(rotors_conf[i].values())[0]

        #step1 index_input -> letter_alphabet
        letter_alphabet = alphabet[(index_input+rotor_shift)%26]

        index_alphabet = index_input+rotor_shift
        print(f"letter_alph {letter_alphabet} index_alph {index_alphabet} ")

        # step2 letter_alphabet -> index_rotor
        index_rotor = rot_alphabet.index(letter_alphabet)

        letter_rotor = rot_alphabet[index_rotor]
        print(f"letter_rotor {letter_rotor} index_rotor {index_rotor}\n")

        #step3
        index_input = index_rotor-rotor_shift
        
    #output
    return alphabet[index_input]


def single_encrypt(letter, rotors, rotor_conf, refl_conf):
    #it returns the shift of the rotors from 1 to 26
    rotors = rotate(rotors)
    cipher_letter = shift(letter,rotors,rotor_conf,refl_conf)
    
    rotors_alph = [alphabet[rotors[0]],alphabet[rotors[1]],alphabet[rotors[2]]]
    print(rotors,rotors_alph,cipher_letter)
    return rotors, cipher_letter

def encrypt(stringa, rotors, rotor_conf, refl_conf):
    ciphertext=""
    for letter in stringa:
        letter = steck(steckerbrett,letter)
        rotors, cipher_letter = single_encrypt(letter, rotors, rotor_conf, refl_conf)
        ciphertext += cipher_letter
    return ciphertext
# %%
slow = 0
middle = 0
fast = 0
#from left to right like in the original machine
rotors = [slow, middle, fast]
rotors_conf = [rotor_I, rotor_II, rotor_III]

ciphertext = encrypt("aaaaa",rotors, rotors_conf, ukw_B)
print(ciphertext)



# %%

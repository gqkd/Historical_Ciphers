#%%
import json
from string import ascii_lowercase
#%%
#creation of the list of the alphabet
alphabet = list(ascii_lowercase)
rotor_I_conf = {"q":"jgdqoxuscamifrvtpnewkblzyh"}


#settings of enigma
steckerbrett = {" ":" ","b":"a","e":"z"}
#doubling the dict, b->a a->b
for value in range(len(list(steckerbrett.values()))):
    steckerbrett[list(steckerbrett.values())[value]]=list(steckerbrett.keys())[value]

#let's call the K of rotors alpha, beta, gamma
# this is the initial position of the rotors
alpha = 5 
beta = 17
gamma = 24
rotors = [alpha, beta, gamma]

#grund and ring stellung
grundstellung = ["a","a","a"]

def rotate(rotors):
    gamma = rotors[0]
    beta = rotors[1]
    alpha = rotors[2]
    rotors_alph = [alphabet[gamma],alphabet[beta],alphabet[alpha]]
    print("prima della rotazione:")
    print(rotors)
    print(rotors_alph)
    alpha += 1
    if alpha % 17 == 0 and alpha != 0:
        beta += 1
    elif alpha % 26 == 0 and alpha != 0:
        alpha = 0
    if beta % 17 == 0 and beta != 0:
        gamma += 1
        beta += 1
    elif beta % 26 == 0 and beta != 0:
        beta = 0

    rotors = [gamma, beta, alpha]
    print("dopo la rotazione:")
    print(rotors)
    rotors_alph = [alphabet[gamma],alphabet[beta],alphabet[alpha]]
    print(rotors_alph,'\n')
    return rotors


def rotate_first_rotor(rotors):
    alpha = rotors[0]
    beta = rotors[1]
    gamma = rotors[2]

    # alpha += 1
    # if alpha % 26 == 0:
    #   beta += 1
    #   alpha = 0
    # if beta % 26 == 0 and alpha % 26 != 0 and beta >= 25:
    #   gamma += 1
    #   beta += 1

    #il codice sopra va, però non considera quando gamma arriva a notch
    #il codice sotto non va, è quello che ho scritto io, bisogna implementare
    # la rotazione del secondo e del terzo contemporaneamente
    alpha = 0
    beta = 0
    gamma = 25
    rotors = [alpha, beta, gamma]
    print(alpha, beta, gamma)
    gamma += 1
    print(alpha, beta, gamma)
    if alpha % 26 == 0 and alpha != 0:
        beta += 1
        alpha = 0
    if beta % 26 == 0 and beta != 0:
        gamma += 1
        beta = 0
    if gamma % 26 == 0 and gamma != 0:
        alpha += 1
        gamma = 0
    rotors = [alpha, beta, gamma]
    print(rotors)

def en_stage2(grundstellung, ringstellung, letter):
    #grundstellung
    pass
#steckerbrett encryption
def en_stage1(steckerbrett,letter):
    if letter in list(steckerbrett.keys()):
        return steckerbrett[letter]


# %%
gamma = 0
beta = 15
alpha = 15
rotors = [gamma, beta, alpha]

for i in range(0,10):
    rotors = rotate(rotors)
# %%

import string
import numpy as np

alph = list(string.ascii_uppercase) # make a list of the alphabet in upper case
k = list(np.arange(0, 26)) # list of numbers 1 to 26
message = 'ZNK UCR NUUZY' # message (can be changed of course)

for i in range(len(k) - 1): # loop through all 26 numbers
    new_mes = ''
    i = i + 1
    for j in range(len(message)):
        if message[j] == ' ': # condition for if there is a space in the message
            new_mes = new_mes + ' '
        else:
            let = message[j] 
            pos = alph.index(let) # find the position of the given letter in the alphabet
            new_mes = new_mes + alph[pos - i] # shift the decrpyted message by i places (hence shift cypher)
    print('Key:', i, 'Message:', new_mes) # print the key no. and decrpyted message (all but one will be coherent)
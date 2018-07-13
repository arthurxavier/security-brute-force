import hashlib
import numpy as np
import random


def readDictionary(file_name):
    with open(file_name, 'r') as data:
        dictionary = {}
        for line in data:
            p = line.split()
            dictionary[p[0]] = p[1]
    return dictionary

def compareSha256(listaCodigos, dicionario):
    frase = ""
    for valor in listaCodigos:
        frase += dicionario[valor]
    fraseTeste = hashlib.sha256(frase.encode()).hexdigest()
    print (fraseTeste)
    if (sha256 == fraseTeste):
        return True
    return False

def generateWord():
    word = []
    for i in range(6):
        array = np.random.choice(dado,5, p=probs)
        word.append(''.join(map(str, array)))
    return word
	

def generateWord2():
    word = []
    array = []
    for i in range(6):
        array = []
        array += str(weighted_choice_sub([5.0, 5.0, 0.0, 0.0, 0.0, 0.0]))
        array += str(weighted_choice_sub([5.0, 5.0, 0.0, 0.0, 0.0, 0.0]))
        array += str(weighted_choice_sub([5.0, 5.0, 0.0, 0.0, 0.0, 0.0]))
        array += str(weighted_choice_sub([5.0, 5.0, 0.0, 0.0, 0.0, 0.0]))
        array += str(weighted_choice_sub([5.0, 5.0, 0.0, 0.0, 0.0, 0.0]))
        word.append(''.join(map(str, array)))
    print (word)
    return word

def teste():
    array = choices(dado, probs)
    return array

def teste2():
    myProb = []
    for i in range(5):
        test = np.random.choice(np.arange(1, 7), p=[0.25, 0.75, 0.0, 0.0, 0.0, 0.0])
        myProb.append(test)
    return myProb
	
def weighted_choice_sub(weights):
    rnd = random.random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i+1
	
def convertToWord(listaCodigos):
    frase = ""
    for valor in listaCodigos:
        frase += dicionario[valor]
    return frase

def findPassword():
    while True:
        palavra = generateWord()
        print (palavra)
        if compareSha256(palavra, dicionario):
            return convertToWord(palavra)
        


#Le o arquivo e salva num dicionário
#['21331','11212','13233','31231','22233','23131']
#t13 = 'da3bca6d8d797393ee46cfe6ee441d5d6dd06d98cd93286d2266b3496ebf7aae'
dicionario = readDictionary('diceware.wordlist.asc')
dado = [1,2,3,4,5,6]
probs = [0.1111111111111111, 0.1111111111111111, 0.7777777777777778, 0.0, 0.0, 0.0]
sha256 = '1bbabbbe542dc9c8139c36a9c9bd8bd89a0f10128191b029a5cfb72bdae40ab7'

print(findPassword())
#generateWord2()
#generateWord2();

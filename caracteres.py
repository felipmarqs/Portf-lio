'''
Ese módulo contém funções para srings
'''

from typing import Union

def conta_letras(frase:str) -> int:
    '''Conta a quantidade de letras em uma frase
        param: 
            frase: uma frase qualquer
        return:
            retorna quantas letras tem na frase '''
    cont = 0
    frase = frase.replace(' ', '')
    for i in range(len(frase.strip())):
        cont += 1
    
    return cont
def conta_vogais(palavra:str) -> int:
    '''Conta a quantidade de vogais em uma palavra
        param: 
            uma palavra qualquer
        return:
            retorna a quantidade de vogais dessa palavra
    
    
    '''
    cont = 0
    for i in range(len(palavra)):
        if palavra[i].lower() in ['a','e','i','o','u']:
            cont += 1
    return cont
    ...
def eh_palindromo(palavra:str) -> bool:
    '''Verifica se uma palavra é um palíndromo
        param:
            Uma palavra qualquer
        return:
            Retorna se uma palavra é um palíndromo

    '''
    if palavra[::-1].upper().strip() == palavra.upper().strip():
        return True
    else:
        return False
    ...
def tem_maiusculas(palavra:str, contar:bool = False) -> Union[bool,int]:
    if not contar:
        for letra in palavra:
            if letra.isupper() == True:
                return True

    cont = 0
    if contar:
        for letra in palavra:
            if letra.isupper() == True:
                cont += 1
    return cont

    
def tem_minusculas(palavra:str, contar:bool = False) -> Union[bool,int]:
    if not contar:
        for letra in palavra:
            if letra.islower() == True:
                return True

    cont = 0
    if contar:
        for letra in palavra:
            if letra.islower() == True:
                cont += 1
    return cont
    ...

if __name__ == '__main__':
    print(__doc__)

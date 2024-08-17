# Pesquisa Binária - Mais eficiente do que a busca linear, pois o número de tentativas para achar o item procurado é absurdamente menor.
#  Para a pesquisa binária funcionar, a lista precisa estar ordenada. 
# O 'chute' para achar o item é sempre feito no meio da lista, e caso o item não seja achado no meio, metade da lista é descartada da procura pela redefinição do valor da variável baixo ou alto, e o processo é repetido até achar o item ou será retornado None caso o item não exista na lista.

def pesquisa_binaria(lista, item):
    baixo = 0 # Primeiro índice
    alto = len(lista) - 1 # Último índice
    while baixo <= alto:
        metade = (baixo + alto) // 2
        if item == lista[metade]:
            return metade 
        else:
            if item > lista[metade]:
                baixo = metade + 1
            if item < lista[metade]:
                alto = metade - 1
    return None 


lista = [2, 4, 5, 6, 7, 8]
print(pesquisa_binaria(lista, 4)) 
print(pesquisa_binaria(lista, 9))  

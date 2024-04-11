
lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]

numero_mais_repetido = lista.pop(0)

print(f"O numero mais repetido dessa lista é o {numero_mais_repetido}")

#professor, não entendi ao certo se era pra só dar um sort na lista que foi dada ou se era pra percorre-la, reutilizei a logica que usei uma vez em JS pra percorrer a lista e printar o mais repetido aqui abaixo caso fosse isso:


# lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
# contagem = {}


# for num in lista:
#     if num in contagem:
#         contagem[num] += 1
#     else:
#         contagem[num] = 1

# maiorQuantidade = 0
# numero_mais_repetido = 0
# for num, quantidade in contagem.items():
#     if quantidade > maiorQuantidade:
#         maiorQuantidade = quantidade
#         numero_mais_repetido = num

# print("O número que se repete mais vezes é:", numero_mais_repetido)

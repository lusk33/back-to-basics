from math import log2

_ = """ Calcula o O(n!) (big O)
 Comparando o tempo de execução de uma pesquisa simples e uma pesquisa binária.
"""

tamanho_lista = 128 # resposta 7
#tamanho_lista =  input("Insira o tamanho da lista que deseja: ")


print(f"Pesquisa simples: {tamanho_lista} passos\n")

resultado_pesquisa_binária = log2(tamanho_lista)
print(f"Pesquisa binária: {resultado_pesquisa_binária} passos")
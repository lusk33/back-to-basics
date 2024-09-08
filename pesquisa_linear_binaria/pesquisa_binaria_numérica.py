""" 
Para pesquisasa binárias é importante que os valores estejam ordenados.
O motivo disto é que realizaremos uma varredura com os valores intermediários da lista.
"""

valor_secreto = 9999999

array = range(0, 10000)


def  pesquisa_binaria(array, valor_secreto):
    menor_valor = 0
    maior_valor = len(array)-1  # Identifica o tamanho da lista
    chute = None
    print(f"O valor secreto é {valor_secreto}")
    print(f"O menor valor atualmente é: {menor_valor}")
    print(f"Tamanho da lista {maior_valor}")

    while menor_valor <= maior_valor or chute == valor_secreto :
        valor_intermediário = (menor_valor + maior_valor) // 2  # posição na lista
        chute = array[valor_intermediário]  # real valor na lista
        print(f"Valor intermediário: {valor_intermediário}")
        print(f"O chute é: {chute}")

        if chute == valor_secreto:
            print(f"Encontrei o valor! O número secreto é {chute}")
            return chute

        elif chute < valor_secreto:
            print("O chute foi muito baixo :(")
            menor_valor = valor_intermediário + 1 # Aumento a posição na lista
            print(f"O novo menor valor é: {menor_valor}")

        elif chute > valor_secreto:
            print("O chute foi muito alto :(")
            maior_valor = valor_intermediário - 1
            print(f"O novo maior valor é: {maior_valor}")
    
    return print("Erro: Não o valor secreto não existe na lista")

pesquisa_binaria(array, valor_secreto)

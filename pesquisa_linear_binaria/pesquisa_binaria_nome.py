from typing import Dict, List, Tuple, Union
import logging
import sys

# Configuração básica do logging
logging.basicConfig(
    level=logging.DEBUG,  # Define o nível de log para DEBUG (mostra todos os níveis)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Formato da mensagem
    datefmt='%Y-%m-%d %H:%M:%S',  # Formato da data
    handlers=[
        logging.FileHandler("app.log"),  # Salva logs em um arquivo
        logging.StreamHandler()  # Exibe logs no console
    ]
)

# Criando um logger
logger = logging.getLogger(__name__)


"""

Encontra com pesquisa simples o contato desejado

"""

# Funções
## data_pipeline
def importa_contatos() -> Dict[str,str]:
    contatos = {
        "Alice Brown": "(11) 91234-5678",
        "Benjamin Davis": "(21) 98765-4321",
        "Catherine Evans": "(31) 97654-3210",
        "Daniel Foster": "(41) 96543-2109",
        "Emily Green": "(51) 95432-1098",
        "Frank Harris": "(61) 94321-0987",
        "Grace Johnson": "(71) 93210-9876",
        "Henry King": "(81) 92109-8765"
    }
    return contatos

def extrai_nomes(contatos: Dict[str,str]) -> List[str]:
    """
    Processa um dicionário de contatos e retorna uma lista de nomes e o tamanho da lista.

    Parâmetros:
    contatos (Dict[str, str]): Dicionário contendo nomes como chaves e números de telefone como valores.

    Retorna:
    List[str]: Lista de nomes extraídos do dict.
    
    """
    nomes = list(contatos.keys())

    # Aplicando strip() e lower() para cada elemento da lista
    nomes_processados = [nome.strip().lower() for nome in nomes]

    logger.info(f"Nomes existentes: {nomes_processados}") # Idealmente em cenário prd não loggar isto

    return nomes_processados


def encontra_numero(contatos: Dict[str,str], indice: str) -> Tuple[str,str]:
    # Procura o indice de pesquisa em contatos 
    nome = list(contatos.keys())[indice]
    numero_telefone = contatos[nome]

    return nome, numero_telefone

## Métodos de pesquisa
def pesquisa_linear(lista_nomes: List[str], contato_desejado: str) ->  Union[int, None]:
    """
    Parâmetros: 
    lista_nomes(List[str]): Nomes da lista telefonica
    contato_desejado(str): Contato que está sendo buscado pelo usuário

    Retorna:
    Union[int, None]: int em caso de sucesso | None em caso de erro, 

    """
    
    chute = 0  # posição na lista do primeiro chute
    cont_passos = 0 # contador de passos necessários
    tamanho_lista = len(lista_nomes) - 1

    # Limpando o contato desejado
    contato_desejado = contato_desejado.strip().lower()

    while chute <= tamanho_lista:
        #print(lista_nomes[chute], chute)
        
        cont_passos+= 1

        if lista_nomes[chute] == contato_desejado:
            logger.info(f"Foram necessários {cont_passos} passos.")
            return chute

        elif chute == tamanho_lista:
            logger.info(f"Foram necessários {cont_passos} passos.")
            logger.error("Function Error: Não foi possível encontrar o nome.")
            return None
            
        else: chute += 1


def main():
    contato_desejado = "Graciane Johnson"

    logger.info("Importando contatos...")
    contatos = importa_contatos()

    logger.info("Processando contatos...")
    lista_nomes = extrai_nomes(contatos)

    logger.info("Buscando nome...")
    indice = pesquisa_linear(lista_nomes, contato_desejado)
    
    if indice == None:       
        logger.error("Não foi possível encontrar o nome desejado")
        sys.exit()
        
    logger.info("Telefone encontrado!")
    nome, numero_telefone = encontra_numero(contatos, indice)

    print(f"""
        Nome: {nome},
        Telefone: {numero_telefone}
        """)


if __name__ == "__main__":
    main()






    
#     if contato_desejado == chute:
#         print(f"Nome encontrado! {chute}")
#         break
#     else 





# menor_nome = lista_nomes[0]
# maior_nome = lista_nomes[-1]

# print(f'Menor nome: {menor_nome}')
# print(f'Maior nome: {maior_nome}')

# quebrar em letras
# quebrar em silabas
# pesquisar por combinação de silabas


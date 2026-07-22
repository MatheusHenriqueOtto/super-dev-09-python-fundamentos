from typing import Dict

def exercicio_01():
    pasciente: Dict[str, str|float|int|bool] = {}
    pasciente["nome"] = "Matheus Henrique Otto"
    pasciente["saude"] = "Pessimo"
    pasciente["idade"] = 18
    pasciente["peso"] = 62.5
    pasciente["vivo"] = True

    print(f"Pasciente: {pasciente["nome"]}")


def exercicio_02():
    aluno:Dict[str, str|int] = {}
    aluno["nome"] = "Samuel"
    aluno["idade"] = 16
    aluno["turma"] = "101"
    aluno["curso"] = "Fulstak em python"

    for chaves in aluno.keys():
        print(chaves)


def exercicio_03():
    produto: Dict[str, str|float|int] = {}
    produto["nome"] = "Celuar"
    produto["preco"] = 3209.99
    produto["estoque"] = 20
    produto["categoria"] = "eletrodomestico"

    for key, valor in produto.items():
        print(valor)


def exercicio_04():
    funcionario: Dict[str, str|float] = {}
    funcionario["nome"] = "Lukas"
    funcionario["cargo"] = "vendedor"
    funcionario["salario"] = 3500.00
    funcionario["setor"] = "comercial"

    for key, valor in funcionario.items():
        print(f"{key}: {valor}")


def exercicio_05():
    titulo = input("Digite o titulo do livro: ")
    autor = input("Digite o autor do livro: ")
    ano_publicacao = int(input("Digite o ano de publicação: "))
    quantidade_paginas = int(input("Digite a quantidade de paginas: "))
    livro: Dict[str, str|int] = {
        "titulo": titulo,
        "autor": autor,
        "ano_publicacao": ano_publicacao,
        "quantidade_paginas": quantidade_paginas
    }

    for key, valor in livro.items():
        print(f"{key}: {valor}")


def exercicio_06():
    jogos = [
        {
            "nome_jogo": "Minecraft",
            "genero": "Mundo Aberto",
            "ano_lancamento": 2011,
            "preco": 200.00
        },
        {
            "nome_jogo": "GTA 6",
            "genero": "Mundo Aberto",
            "ano_lancamento": 2026,
            "preco": 450.00
        },
    ]

    for jogo in jogos:
        for chave, valor in jogo.items():
            print(f"{chave}: {valor}")



def exercicio_07():
    produtos = [{
        "id": 1,
        "nome": "Martelo",
        "categoria": "Ferrameta",
        "preco": 15.00,
        "estoque": 20
        },
        {
        "id": 2,
        "nome": "Prego",
        "categoria": "Ferrameta",
        "preco": 0.80,
        "estoque": 250,
        },
        {
        "id": 3,
        "nome": "Notebook",
        "categoria": "eletrodomestico",
        "preco": 4000.20,
        "estoque": 5
        },
        {
        "id": 4,
        "nome": "Geladeira",
        "categoria": "eletrodomestico",
        "preco": 4599.99,
        "estoque": 3
        },
        {
        "id": 5,
        "nome": "Mesa",
        "categoria": "Mobilia",
        "preco": 200.00,
        "estoque": 1
        }
    ]

    nomes = obter_nomes_produtos(produtos)
    produtos_com_estoque_baixo = obter_produtos_com_estoque_baixo(produtos)
    produtos_categoria = obter_produtos_por_categoria(produtos, input("Digite a categoria que deseja filtrar: "))
    produtos_acima_preco = obter_produtos_acima_do_preco(produtos, float(input("Digite o preco minimo para filtrar: ")))
    total_estoque = somar_valor_total_estoque(produtos)


    print(nomes)
    print(produtos_com_estoque_baixo)
    print(produtos_categoria)
    print(produtos_acima_preco)
    print(total_estoque)


def obter_nomes_produtos(produtos):
    nomes = []

    for produto in produtos:
        nomes.append(produto["nome"])

    return nomes
    

def obter_produtos_com_estoque_baixo(produtos):
    produtos_estoque_baixo = []

    for produto in produtos:
        if produto["estoque"] < 10:
            produtos_estoque_baixo.append(produto["nome"])

    return produtos_estoque_baixo


def obter_produtos_por_categoria(produtos, categoria_pesquisada):
    produtos_filtrados = []

    for produto in produtos:
        if produto["categoria"] == categoria_pesquisada:
            produtos_filtrados.append(produto["nome"])

    return produtos_filtrados

    
def obter_produtos_acima_do_preco(produtos, preco_minimo):
    produtos_filtrados = []

    for produto in produtos:
        if produto["preco"] > preco_minimo:
            produtos_filtrados.append(produto["nome"])

    return produtos_filtrados



def somar_valor_total_estoque(produtos):
    total_estoque = 0

    for produto in produtos:
        total_estoque = total_estoque + (produto["estoque"] * produto["preco"])

    return total_estoque


exercicio_07()
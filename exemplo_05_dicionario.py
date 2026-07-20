from typing import Dict, List

def exemplo_basico_dicionario():
    carros = {}

    carros["bmw"] = "M5"
    carros["mercedes"] = "GLA 250"
    carros["fiat"] = "uno"

    carros["mercedes"] = "GLA 200"
    print("Dicionario:", carros)

    print("Chaves:", carros.keys())

    print("Valores:", carros.values())


def obter_cliente_com_score_alto(clientes: Dict[str, Dict[str, float]]):

    clientes_selecionados: List[str] = []
    for nome_cliente, dados_cliente in clientes.items():
        if dados_cliente["score"] > 650:
            clientes_selecionados.append(nome_cliente)
    return clientes_selecionados


def somar_salarios(clientes: Dict[str, Dict[str, float]]) -> float:
    total: float = 0.0
    for dados in clientes.values():
        salario = dados["salario"]
        total = total + salario
    return total


def obter_nome_clientes(clientes: Dict[str, Dict[str, float]]) -> List[str]:
    nomes = []
    for nome_cliente in clientes.keys():
        nomes.append(nome_cliente)
    return nomes


def processar_disponibilidade_emprestimo():
    clientes: Dict[str, Dict[str, float]] = {
        "Amanda": {
            "salario": 2000.0,
            "score": 997,
            "id": 100
        },
        "Pedro": {
            "salario": 20_951.29,
            "score": 130,
            "id": 101
        },
        "Steffany": {
            "salario": 4_593.29,
            "score": 520,
            "id": 102
        },
        "Rogério": {
            "salario": 17_231.39,
            "score": 776,
            "id": 103
        }
    }
    clientes_aprovados_para_emprestimo = obter_cliente_com_score_alto(clientes)
    total_salarios = somar_salarios(clientes)
    nome_clientes = obter_nome_clientes(clientes)

    print("Clientes aprovados para empréstimo:", clientes_aprovados_para_emprestimo)
    print("Total de salários:", total_salarios)
    print("Clientes:", nome_clientes)


processar_disponibilidade_emprestimo()
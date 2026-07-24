class Autor:
    def __init__(self, nome: str, nacionalidade: str, ano_nascimento: str) -> None:
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.ano_nascimento = ano_nascimento

    def apresentar_dados(self):
        print(f"Nome: {self.nome}\nNacionalidade: {self.nacionalidade}\nAno de nascimento: {self.ano_nascimento}")

    def obter_descricao(self):
        print(f"{self.nome} - {self.nacionalidade}")


class Livro:
    def __init__(self, titulo: str, quantidade_paginas: str, ano_publicado: str, autor: Autor) -> None:
        self.titulo = titulo
        self.quantidade_paginas = quantidade_paginas
        self.ano_publicado = ano_publicado
        
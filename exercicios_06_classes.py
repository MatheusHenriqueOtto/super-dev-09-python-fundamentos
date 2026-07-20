
class Tenis:
    def __init__(self, modelo: str, tamanho: float, marca: str, valor: float):
        self.modelo = modelo
        self.tamanho = tamanho
        self.marca = marca
        self.valor = valor


    def apresentar_dados(self):
        print(f"""
--------------------------------------------------------------------------------------
Modelo: {self.modelo}
Tamanho: {self.tamanho}
Marca: {self.valor}
---------------------------------------------------------------------------------------""")
       
def exemplos_tenis():
    jordan = Tenis("jordan", 47.5, "nike", 120.00)


    jordan.apresentar_dados()








class Aluno:
    def __init__(self, nome: str, nota_1: float, nota_2: float):
        self.nome = nome
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.media = self.calcular_media()
        self.situacao = self.definir_situacao()


    def apresentar_aluno(self):
        print(f"Aluno: {self.nome}\nPrimeira nota: {self.nota_1}\nSegunda nota: {self.nota_2}\nMedia: {self.media}\nSituação: {self.situacao}\n\n\n")
   
    def calcular_media(self):
        media = (self.nota_1 + self.nota_2) / 2
       
        return media
   
    def definir_situacao(self):
        situacao = "Aprovado"
        if self.media < 7:
            situacao = "Reprovado"
       
        return situacao
   


def exemplo_aluno():
    matheus = Aluno("Matheus", 9, 8)
    lukas = Aluno("Lukas", 8.5, 10)
    elias = Aluno("Elias", 7.8, 10)


    matheus.apresentar_aluno()
    lukas.apresentar_aluno()
    elias.apresentar_aluno()








class Triangulo:
    def __init__(self, base: float, altura: float, lado_1: float, lado_2: float, lado_3: float):
        self.base = base
        self.altura = altura
        self.lado_1 = lado_1
        self.lado_2 = lado_2
        self.lado_3 = lado_3
        self.area = self.calcular_area()
        self.tipo = self.verificar_tipo()


    def apresentar_dados(self):
        print(f"\nBase: {self.base}\nAltura: {self.altura}\nPrimeiro lado: {self.lado_1}\nSegundo lado: {self.lado_2}\nTerceiro lado: {self.lado_3}\nArea: {self.area}")


    def calcular_area(self):
        area = (self.base * self.altura)/2
        return area
   
    def verificar_tipo(self):
        tipo = ""
        if self.verificar_equilatero() == True:
            tipo = "Equilátero"
        elif self.verificar_isosceles() == True:
            tipo = "Isósceles"
        elif self.verificar_escaleno() == True:
            tipo = "Escaleno"
        else:
            tipo = "indefinido, ou erro ao tentar identificar"


        return tipo
   
    def verificar_equilatero(self):
        if self.lado_1 == self.lado_2 == self.lado_3:
            return True
        else:
            return False


    def verificar_isosceles(self):
        if self.lado_1 == self.lado_2 != self.lado_3:
            return True
        elif self.lado_1 != self.lado_2 == self.lado_3:
            return True
        elif self.lado_1 == self.lado_3 != self.lado_2:
            return True
        else:
            return False


    def verificar_escaleno(self):
        if self.lado_1 != self.lado_2 != self.lado_3:
            return True
        else:
            return False

    
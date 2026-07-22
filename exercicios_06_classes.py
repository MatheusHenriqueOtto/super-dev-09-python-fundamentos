
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
        self.area = self.calcular_area_triangulo()
        self.tipo = self.verificar_tipo()


    def apresentar_dados(self):
        print(f"\nBase: {self.base}\nAltura: {self.altura}\nPrimeiro lado: {self.lado_1}\nSegundo lado: {self.lado_2}\nTerceiro lado: {self.lado_3}\nTipo: {self.tipo}\nArea: {self.area}m²")


    def calcular_area_triangulo(self) -> float:
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
        
    def calcular_area(self):
        area = (self.base * self.altura)/ 2
        return area

def exemplo_triangulo():
    robson = Triangulo(10, 15, 20, 20, 20)
    agatha = Triangulo(21, 10, 20, 20, 15)

    robson.apresentar_dados()
    print("-" * 25)
    agatha.apresentar_dados()



class Quadrado:
    def __init__(self, lado: float):
        self.lado = lado
        self.area = self.calcular_area_quadrado()
        self.perimetro = self.calcular_perimetro()

    def apresentar_quadrado(self):
        print(f"Lado do quadrado: {self.lado}\nArea do quadrado: {self.area}\nPerimetro do quadrado: {self.perimetro}")
    
    def calcular_area_quadrado(self):
        area = self.lado * self.lado
        return area
    
    def calcular_perimetro(self):
        perimetro = self.lado * 4
        return perimetro


def exemplo_quadrado():
    quadrado = Quadrado(15)
    quadradao = Quadrado(30)

    quadrado.apresentar_quadrado()
    quadradao.apresentar_quadrado()



class Retangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
        self.area = self.calcular_area()
        self.perimetro = self.calcular_perimetro()


    def calcular_area(self):
        area = self.base * self.altura
        return area
    
    def calcular_perimetro(self):
        perimetro = self.base + self.base + self.altura + self.altura
        return perimetro
    
    def apresentar_retangulo(self):
        print(f"Base: {self.base}\nAltura: {self.altura}\nArea: {self.area}\nPerimetro: {self.perimetro}\n{"-"*20}")


def exemplo_retangulo():
    retangulo = Retangulo(20, 10)
    retangulao = Retangulo(40, 20)

    retangulo.apresentar_retangulo()
    retangulao.apresentar_retangulo()


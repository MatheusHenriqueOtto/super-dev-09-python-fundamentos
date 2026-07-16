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
        

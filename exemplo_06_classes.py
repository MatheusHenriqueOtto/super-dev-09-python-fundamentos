class Cachorro:
    def __init__(self, apelido: str, raca: str, cor: str, peso: float, idade: int):
        self.apelido = apelido
        self.raca = raca
        self.cor = cor
        self.peso = peso
        self.idade = idade

    def apresentar_dados(self):
        print(f"Cachorro: {self.apelido}")
        print(f"Raça: {self.raca}")
        print(f"Cor: {self.cor}", end="\n\n\n\n")

    def fazer_aniversario(self):
        self.idade = self.idade + 1
        print("FEELLIIZZ ANIVERSÁRIO!!!!!!!", self.apelido, "fez", self.idade, "anos")


tobi = Cachorro("Tobi", "Vira-Lata", "caramelo", 25.60, 6)

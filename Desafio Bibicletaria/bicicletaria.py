class Bicicleta:
    # def __init__: método construtor
    # self ou this representa a instância do objeto, explicita
    # self. : atributos da classe

    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = 18
        self.marcha = 1

    # funções e métodos são declarados da mesma forma, a diferença é a passagem de argumentos
    # mesmo que o método não receba parametros, é necessário informar o 'self'
    def buzinar(self):
        print("Plin Plin!")

    def parar(self):
        print("Parando...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummm...")

    def trocar_marcha(self, nro_marcha):
        print("Trocando marcha")

        def _trocar_marcha():
            if nro_marcha > self.marcha:
                print("Marcha trocada!")
            else:
                print("Não foi possível trocar a marcha")
 
    # exibir a instância de forma mais legível ao usuário:
    # def __str__(self):
    #     return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"
    # ou
    # exibir a instância de forma mais legível ao usuário:

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items() ])}"


# instância de bicicleta:
b1 = Bicicleta("rosa", "caloi", 2023, 1000)
print(b1)

# # Chamada de classe pode ser feita: b1.correr() ou Bicicleta.correr(b1)
# b1.correr()
# b1.buzinar()
# Bicicleta.correr(b1)
# b1.parar()

# # exibir atributos da classe:
# print(b1.cor, b1.modelo, b1.ano, b1.valor)

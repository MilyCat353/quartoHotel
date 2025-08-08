class Quarto:
    def __init__(self, identificador, tipo_quarto, valor_diaria, disponivel=True):
        self.__identificador = identificador
        self.__tipo_quarto = tipo_quarto
        self.__valor_diaria = valor_diaria
        self.__disponivel = disponivel

    def exibir_detalhes(self):
        print("-" * 30)
        print(f"Quarto {self.__identificador}")
        print(f"Tipo: {self.__tipo_quarto}")
        print(f"Valor da diária: R${self.__valor_diaria:.2f}")
        print(f"Status: {'Disponível' if self.__disponivel else 'Ocupado'}")
        print("-" * 30)
        
    def reservar(self):
        if self.__disponivel:
            self.__disponivel = False
            print("Reserva realizada com sucesso.")
        else:
            print("O quarto já está ocupado.")

    def liberar(self):
        if not self.__disponivel:
            self.__disponivel = True
            print("Quarto liberado com sucesso.")
        else:
            print("O quarto já está disponível.")

    def alterar_preco(self, novo_valor):
        self.__valor_diaria = novo_valor
        print(f"Valor da diária alterado para R${self.__valor_diaria:.2f}")

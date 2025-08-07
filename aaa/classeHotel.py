class Quarto:
    def __init__(self, identificador, tipo_quarto, valor_diaria, disponivel=True):
        self.identificador = identificador
        self.tipo_quarto = tipo_quarto
        self.valor_diaria = valor_diaria
        self.disponivel = disponivel

    def exibir_detalhes(self):
        print(f"Quarto {self.identificador}")
        print(f"Tipo: {self.tipo_quarto}")
        print(f"Valor da diária: R${self.valor_diaria:.2f}")
        print(f"Status: {'Disponível' if self.disponivel else 'Ocupado'}")
        
    def reservar(self):
        if self.disponivel:
            self.disponivel = False
            print("Reserva realizada com sucesso.")
        else:
            print("O quarto já está ocupado.")

    def liberar(self):
        if not self.disponivel:
            self.disponivel = True
            print("Quarto liberado com sucesso.")
        else:
            print("O quarto já está disponível.")

    def alterar_preco(self, novo_valor):
        self.valor_diaria = novo_valor
        print(f"Valor da diária alterado para R${self.valor_diaria:.2f}")
        
    @property
    def identificador(self):
        return self.__identificador
    @property
    def tipoQuarto(self):
        return self.__tipoQuarto
    @property
    def ValorDiaria(self):
        return self.__ValorDiaria
    @property
    def quartoDisponivel(self):
        return self.__quartoDisponivel
    @property
    def dadosQuarto(self):
        return self.__dadosQuarto
        
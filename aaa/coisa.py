from quarto import Quarto
exibirDadosQuarto():
    
quartoDisponivel = False

def reservarQuarto():
    if quartoDisponivel ==  True:
        while(True):
            print("1 -  Fazer reserva")
            print("2 -  Voltar")

            Reserva = int(input("Escolha a opção desejadan: "))
            if Reserva == 1:
                print("Você efetuou sua reserva com sucesso!")
                print(dadosQuarto)
                quartoDisponivel = False

            else: 
                print("Agendamento cancelado")

def verificar_acesso():
    if quartoDisponivel = True:
        print("O quarto está disponivel")
        function reservarQuarto()
       
    else:
        print("O quarto ja está reservado")
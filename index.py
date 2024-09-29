import numpy
import random

setor_1 = numpy.array([])
setor_2 = numpy.array([])
setor_3 = numpy.array([])


def sendMessage(message: str) -> str:
    return f"ESTACIONAMENTO: {message}"


def inVaga(placa: str) -> bool:
    return placa in setor_1 or placa in setor_2 or placa in setor_3


def outVaga(placa: str) -> None:
    global setor_1
    global setor_2
    global setor_3
    if placa in setor_1:
        position = numpy.where(setor_1 == placa)
        setor_1 = numpy.delete(setor_1, position)
    elif placa in setor_2:
        position = numpy.where(setor_2 == placa)
        setor_2 = numpy.delete(setor_2, position)
    elif placa in setor_3:
        position = numpy.where(setor_3 == placa)
        setor_3 = numpy.delete(setor_3, position)


def disponiveis() -> str:
    global setor_1
    global setor_2
    global setor_3
    mensage = "Setores disponiveis:\n"
    if len(setor_1) < 5:
        mensage = mensage + f"Setor 1: " + str(abs(len(setor_1)-5))+"\n"
    if len(setor_2) < 5:
        mensage = mensage + f"Setor 2: " + str(abs(len(setor_2)-5))+"\n"
    if len(setor_3) < 5:
        mensage = mensage + f"Setor 3: " + str(abs(len(setor_3)-5))
    return mensage


def chooseSetor(placa: str) -> None:
    global setor_1, setor_2, setor_3
    setores_disponiveis = []

    if len(setor_1) < 5:
        setores_disponiveis.append(1)
    if len(setor_2) < 5:
        setores_disponiveis.append(2)
    if len(setor_3) < 5:
        setores_disponiveis.append(3)

    if len(setores_disponiveis) == 0:
        return

    setorchoosed = random.choice(setores_disponiveis)
    if setorchoosed == 1:
        setor_1 = numpy.append(setor_1, placa)
    elif setorchoosed == 2:
        setor_2 = numpy.append(setor_2, placa)
    elif setorchoosed == 3:
        setor_3 = numpy.append(setor_3, placa)


def isFull() -> bool:
    global setor_1, setor_2, setor_3
    return len(setor_1) >= 5 and len(setor_2) >= 5 and len(setor_3) >= 5


def carsList() -> str:
    global setor_1, setor_2, setor_3
    data = f"Setor 1 - [{len(setor_1)}]: "
    for i in setor_1:
        data = data + i + " "
    data = data + f"\nSetor 2 - [{len(setor_2)}]: "
    for i in setor_2:
        data = data + i + " "
    data = data + f"\nSetor 3 - [{len(setor_3)}]: "
    for i in setor_3:
        data = data + i + " "
    return data


def getSetor(placa: str) -> str:
    global setor_1
    global setor_2
    global setor_3
    if placa in setor_1:
        return "Setor 1"
    if placa in setor_2:
        return "Setor 2"
    if placa in setor_3:
        return "Setor 3"


while True:
    option = int(input(
        "1 - Adicionar Carro\n2 - Remover Carro\n3 - Verificar carro estacionado:\n4 - Lista de carros\n> "))
    if option == 1:
        if isFull():
            print(sendMessage("O estacionamento está cheio"))
        else:
            placa = input("Informe a placa: ")
            if not inVaga(placa):
                chooseSetor(placa)
                print(sendMessage(
                    f"Esse carro foi cadastrado no setor {getSetor(placa)}"))
            else:
                print(sendMessage(
                    f"Esse carro já está cadastrado no setor {getSetor(placa)}"))

    elif option == 2:
        placa = input("Informe a placa que será removida: ")
        if inVaga(placa):
            print(sendMessage(f'Seu carro de placa {placa} foi removido'))
            outVaga(placa)
        else:
            print(sendMessage(f"O carro de placa {
                  placa} não foi encontrado, insira uma placa válida"))

    elif option == 3:
        placa = input("Inoforme a placa do carro: ")
        if inVaga(placa):
            print(sendMessage(
                f"Seu carro está estacionado no setor {getSetor(placa)}"))
        else:
            print(sendMessage("Seu carro não está estacionado"))
    elif option == 4:
        print(carsList())

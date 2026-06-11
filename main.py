from uteis import linha,leia_int,leia_string,cabecalho

def registrar_voto(votos):
    cabecalho("REGISTRAR VOTO")
    quantidade = leia_int("Quantos votos será registrado? ")
    for i in range(quantidade):
        pessoas = leia_string('Nome da pessoa para a votação:').strip().upper()
        if pessoas in votos:
            votos[pessoas] +=1
        else:
            votos[pessoas] = 1
    return votos

def mostrar(votos):
    c = 0
    cabecalho("MOSTRAR CANDIDATOS")
    if not votos:
        print("Não há nada para mostrar!")
        return
    for canditado,valor in votos.items():
        c+=1
        print(f"{c} - {canditado} - {valor}")

def menu(opc):
    c = 0
    for valor in opc:
        c += 1
        print(f'{c} - {valor}')

def main():
    votos = {}
    while True:
        cabecalho("VOTING SIMULATOR")
        menu(['Registrar Voto',
              'Ver Resultado',])
        opc = leia_int('Escolha uma opção ')
        if opc == 1:
            registrar_voto(votos)
        elif opc == 2:
            mostrar(votos)

main()

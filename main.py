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

def pessoa_mais_votada(votos):
    if not votos:
        print('Nenhum voto foi registrado no momento!')
        return
    mais_votado = 0
    porcentagem = 0
    maior_frequencia = None
    for chave,candidato in votos.items():
        if candidato > mais_votado:
            mais_votado = candidato
            maior_frequencia = chave
    return {'candidato_maior_voto':maior_frequencia,
            'QTD_votos':mais_votado
            }

def main():
    votos = {}
    while True:
        cabecalho("VOTING SIMULATOR")
        menu(['Registrar Voto',
              'Ver Resultado',
              'Ver o mais votado'])
        opc = leia_int('Escolha uma opção ')
        if opc == 1:
            registrar_voto(votos)
        elif opc == 2:
            mostrar(votos)
        elif opc == 3:
            res = pessoa_mais_votada(votos)
            print(res)       
main()

from uteis import linha,leia_int,leia_string,cabecalho,menu

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
    if not votos:
        print("Não há nada para mostrar!")
        return
    cabecalho("MOSTRAR CANDIDATOS")
    for canditado,valor in votos.items():
        c+=1
        print(f"{c} - {canditado} - {valor}")

def pessoa_mais_votada(votos):
    if not votos:
        print('Nenhum voto foi registrado no momento!')
        return
    cabecalho("VERIFICAR CANDIDATO MAIS VOTADO")
    mais_votado = 0
    maior_frequencia = None
    for nome,quantidade in votos.items():
        if quantidade > mais_votado:
            mais_votado = quantidade
            maior_frequencia = nome
    print(f"candidato com mais voto: {maior_frequencia} - Quantidade: {mais_votado} votos\n")

def mostrar_percentual(votos):
    lista = []
    if not votos:
        print('Não há candidados para mostrar no momemento!')
        return
    cabecalho("Mostrar percentual de candidatos mais votados")
    total_votos = sum(votos.values())
    
    for candidato,votos_recebidos in votos.items():
        percentual = (votos_recebidos/total_votos)* 100
        print(f'{candidato} - {percentual:.2f}%')
        


    return lista


def ordenar_votados(votos):
    if not votos:
        return
    ordenar = sorted(votos.items(),key=lambda x:x[1],reverse=True)
    return ordenar

def mostrar_ranking(resultado):
    if not resultado:
        print('Erro, não há nada para mostrar no ranking de resultados')
        return
    for c, (candidato,valor) in resultado(start=1):
        print(f'{c}°Lugar {candidato} - {valor }')


def main():
    votos = {}
    while True:
        cabecalho("VOTING SIMULATOR")
        menu(['Registrar Voto',
              'Ver Resultado',
              'Ver o mais votado',
              'ver percentual de votos',
              'ver vencedores ordenados',
              ])
        opc = leia_int('Escolha uma opção: ')
        if opc == 1:
            registrar_voto(votos)
            
        elif opc == 2:
            mostrar(votos)
        elif opc == 3:
            pessoa_mais_votada(votos)

        elif opc == 4:
            mostrar_percentual(votos) 
        elif opc == 5:
            resultado = ordenar_votados(votos)
            mostrar_ranking(resultado)
        elif opc == 6:
            cabecalho('Sair do sistema . . .')
            break
<<<<<<< HEAD
            
    
=======

>>>>>>> fdbc64ac4e92d1e5d8a9daf9ca69ee316e534af0
if __name__ == "__main__":
    main()


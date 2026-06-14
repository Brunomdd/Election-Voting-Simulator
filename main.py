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
    if not votos:
        print('Não há candidados para mostrar no momemento!')
        return
    cabecalho("Mostrar percentual de candidatos mais votados")
    total_votos = sum(votos.values())
    for candidato,votos_recebidos in votos.items():
        percentual = (votos_recebidos/total_votos)* 100
        print(f'{candidato} - {percentual:.2f}%')

    
def verificar_empate(votos):
    lista_empate = []
    if not votos:
        return
    maior_valor = max(votos.values())
    for canditado,votos_recebidos in votos.items():
        if votos_recebidos == maior_valor:
            lista_empate.append(canditado)

    if len(lista_empate) > 1:
        print(f'Empate entre {'|'.join(lista_empate)}')
   
    
def ordenar_votados(votos):
    if not votos:
        return
    ordenar = sorted(votos.items(),key=lambda x:x[1],reverse=True)
    return ordenar

def mostrar_ranking(resultado):
    c = 0
    if not resultado:
        print('Erro, não há nada para mostrar no ranking de resultados')
        return
    for candidato,valor in resultado:
        c +=1
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
              'verificar empate',
              'Sair',
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
            verificar_empate(votos)
        elif opc == 7:
            cabecalho('Saindo do sistema . . .')
            break
        
if __name__ == "__main__":
    main()


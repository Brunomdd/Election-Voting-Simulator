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
    cabecalho("Verificar Candidato mais votado")
    mais_votado = 0
    maior_frequencia = None
    for chave,candidato in votos.items():
        if candidato > mais_votado:
            qtd_votos = candidato
            maior_frequencia = chave
    print(f"candidato com mais voto: {maior_frequencia} - Quantidade: {qtd_votos} votos\n")

def mostrar_percentual(votos):
    if not votos:
        print('Não há candidados para mostrar no momemento!')
        return
    cabecalho("Mostrar percentual de candidatos mais votados")
    total_votos = 0
    for candidato,votos_recebidos in votos.items():
        total_votos += votos_recebidos
    
    for candidato,votos_recebidos in votos.items():
        percentual = (votos_recebidos/total_votos)* 100
        print(f'{candidato} - {percentual:.2f}%')
    

def main():
    votos = {}
    while True:
        cabecalho("VOTING SIMULATOR")
        menu(['Registrar Voto',
              'Ver Resultado',
              'Ver o mais votado',
              'ver percentual de votos'])
        opc = leia_int('Escolha uma opção ')
        if opc == 1:
            registrar_voto(votos)
        elif opc == 2:
            mostrar(votos)
        elif opc == 3:
            pessoa_mais_votada(votos)
               
        elif opc == 4:
            mostrar_percentual(votos) 
main()

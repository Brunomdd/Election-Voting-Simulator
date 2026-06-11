def linha(linha=42):
    return '-'*linha

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def executar(funcao,msg):
    while True:
        try:
            valor= input(msg)
            if not valor:
                print("Erro! não pode deixar vazio!")
                continue
            return funcao(valor)
        except ValueError:
            print("Erro, digite um valor inteiro!")
    
def leia_int(msg):
    return executar(int,msg)


def menu(opc):
    c = 0
    for valor in opc:
        c +=1
        print(f'{c} - {valor}')
def main():
    while True:
        cabecalho("VOTING SIMULATOR")
        menu(['Registrar Voto',
              'Ver Resultado',])
        
        opc = leia_int('Escolha uma opção ')

main()

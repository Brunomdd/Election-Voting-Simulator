def linha(linha=42):
    return '-'*linha

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

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
        opc = int(input('Escolha uma opção: '))

        
main()

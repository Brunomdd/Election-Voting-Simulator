def linha(linha=42):
    return '-'*linha

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def executar(funcao,msg):
    while True:
        try:
            valor= input(msg).strip()
            if not valor:
                print("Erro! não pode deixar vazio!")
                continue
            return funcao(valor)
        except ValueError:
            print("Erro, digite um número válido")
    
def leia_int(msg):
    return executar(int,msg)
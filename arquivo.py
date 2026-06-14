import json
from json import JSONDecodeError
def carregar():
    votos = {}
    try:
        with open('candidatos.json','r',encoding='utf-8') as arq:
            return json.load(arq)
    except (FileNotFoundError,JSONDecodeError):
        return {}
    return votos

def salvar(votos):
     with open('candidatos.json','w',encoding='utf-8') as arq:
         json.dump(votos,arq,ensure_ascii=False,indent=4)
# 🗳️ Voting Simulator - Simulador de Eleições em Python

Sistema de simulação de eleições desenvolvido em **Python**, com o objetivo de praticar conceitos fundamentais da linguagem, organização de código e manipulação de dados.

O projeto permite cadastrar candidatos, registrar votos, analisar resultados e gerenciar informações através de um menu interativo executado no terminal.

---

## 📌 Sobre o Projeto

O **Voting Simulator** é um sistema de votação onde o usuário pode registrar votos para candidatos, consultar resultados e realizar operações administrativas.

O projeto foi desenvolvido aplicando conceitos importantes da programação em Python, como:

* Estruturas de dados (`dict` e listas)
* Funções e modularização
* Manipulação de arquivos
* Separação de responsabilidades entre módulos
* Entrada e validação de dados
* Ordenação e análise de informações

---

## 🚀 Funcionalidades

O sistema possui **11 opções principais**:

### 1 - Registrar Voto

Permite registrar votos para candidatos. Caso o candidato ainda não exista, ele é cadastrado automaticamente.

### 2 - Ver Resultado

Exibe todos os candidatos cadastrados e a quantidade de votos recebidos.

### 3 - Ver Candidato Mais Votado

Identifica o candidato com maior número de votos.

### 4 - Ver Percentual de Votos

Calcula a porcentagem de votos de cada candidato em relação ao total registrado.

### 5 - Ranking de Candidatos

Organiza os candidatos em ordem decrescente de votos.

### 6 - Verificar Empates

Verifica se existem candidatos empatados na primeira colocação.

### 7 - Buscar Candidato

Permite pesquisar um candidato específico e visualizar sua quantidade de votos.

### 8 - Remover Candidato

Remove um candidato e seus votos registrados do sistema.

### 9 - Atualizar Votos

Permite alterar manualmente a quantidade de votos de um candidato.

### 10 - Resetar Sistema

Remove todos os votos registrados e reinicia os dados da votação.

### 11 - Sair

Encerra o sistema salvando as informações.

---

## 🏗️ Estrutura do Projeto

```text
📁 Voting-Simulator
│
├── main.py
├── arquivo.py
├── uteis.py
├── votos.json
└── README.md
```

### main.py

Arquivo principal responsável pela execução do sistema, controle do menu e chamada das funcionalidades.

### arquivo.py

Responsável pela persistência dos dados, realizando o carregamento e salvamento dos votos.

### uteis.py

Contém funções auxiliares utilizadas para melhorar a organização do código, como:

* Criação de menus
* Cabeçalhos
* Leitura de dados do usuário
* Funções de apoio

---

## 💾 Armazenamento de Dados

Os dados da votação são armazenados em arquivo, permitindo que os votos continuem disponíveis mesmo após o encerramento do programa.

Exemplo:

```json
{
    "CANDIDATO A": 15,
    "CANDIDATO B": 10,
    "CANDIDATO C": 5
}
```

---

## 🧠 Conceitos Aplicados

### Dicionários

O sistema utiliza dicionários para armazenar candidatos e suas respectivas quantidades de votos.

Exemplo:

```python
votos = {
    "JOAO": 20,
    "MARIA": 15
}
```

---

### List Comprehension

Utilizado para encontrar candidatos empatados na primeira colocação:

```python
[
    candidato
    for candidato, votos_recebidos in votos.items()
    if votos_recebidos == maior_valor
]
```

---

### Ordenação de Dados

Utilização do `sorted()` para criar um ranking de candidatos:

```python
sorted(votos.items(), key=lambda x:x[1], reverse=True)
```

---

### Modularização

O projeto foi dividido em diferentes módulos para facilitar organização, manutenção e evolução do código.

---

## ▶️ Como Executar

Clone o repositório:

```bash
git clone https://github.com/brunomdd/Voting-Simulator.git
```


## 🔮 Melhorias Futuras

Possíveis evoluções para o projeto:

* Implementar banco de dados
* Criar uma API utilizando FastAPI
* Criar uma interface gráfica
* Adicionar autenticação de usuários
* Criar relatórios de votação
* Implementar diferentes cargos eleitorais

---

## 👨‍💻 Autor

Desenvolvido por **Bruno** como projeto de estudo em Python, com foco em evolução para desenvolvimento Backend.

---

⭐ Projeto desenvolvido para praticar lógica de programação, estruturas de dados, modularização e construção de sistemas utilizando Python.

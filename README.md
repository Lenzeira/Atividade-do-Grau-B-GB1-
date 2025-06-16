# Guilherme Lenzi de Oliveira e Taimisson de Carvalho Schardosim

# Atividade-do-Grau-B-GB1
# Sistema de Gerenciamento de Biblioteca em Python (POO)

Este projeto é uma implementação de um sistema simples de gerenciamento de biblioteca, desenvolvido como atividade acadêmica. O sistema foi construído utilizando conceitos de Programação Orientada a Objetos (POO) em Python para modelar as entidades e suas interações.

## Objetivo

O objetivo é simular as operações básicas de uma biblioteca, como o cadastro de livros e usuários (alunos e professores), e o gerenciamento de empréstimos e devoluções, aplicando os pilares da POO como herança, polimorfismo e composição.

## Recursos

- **Cadastro de Livros**: Permite criar novos livros com título, autor, ISBN e status de disponibilidade.
- **Cadastro de Usuários**: Suporta dois tipos de usuários (Alunos e Professores) através de herança.
- **Sistema de Empréstimo**: Gerencia o empréstimo de um livro para um usuário, controlando a disponibilidade.
- **Sistema de Devolução**: Atualiza o status de um livro para "disponível" após a devolução.
- **Exibição de Informações**: Métodos para visualizar os dados de livros, usuários e resumos de empréstimos.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

```
.
├── main.py              # Arquivo principal com a simulação do sistema
├── models/             # Diretório contendo as classes do sistema
│   ├── livro.py       # Classe Livro e suas funcionalidades
│   ├── usuario.py     # Classes Usuario, Aluno e Professor
│   └── emprestimo.py  # Classe Emprestimo e suas funcionalidades
└── README.md          # Documentação do projeto
```

## Como Executar

Para rodar a simulação do sistema, siga os passos abaixo.

**Pré-requisitos:**
- Ter o [Python 3](https://www.python.org/downloads/) instalado em sua máquina.

**Passos:**
1. Clone este repositório ou baixe os arquivos para uma pasta em seu computador.
2. Abra um terminal ou prompt de comando na pasta do projeto.
3. Execute o seguinte comando:
    ```bash
    python main.py
    ```
4. A simulação completa será impressa no terminal.

## Autores

- Guilherme Lenzi de Oliveira
- Taimisson de Carvalho Schardosim

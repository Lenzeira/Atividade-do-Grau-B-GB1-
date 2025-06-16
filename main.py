# Guilherme Lenzi de Oliveira e Taimisson de Carvalho Schardosim
import time
from models.livro import Livro
from models.usuario import Aluno, Professor
from models.emprestimo import Emprestimo
    

def banner(titulo: str) -> None:
    print(f" \n {titulo.center(60, '=')} \n ")
    time.sleep(1)

def informacao_sistema_alunos() -> None:
    print("""
    O sistema de biblioteca é um sistema que permite aos alunos emprestar livros.
    O sistema é composto por:
    - Livros
    - Usuários
    - Empréstimos
          
    Sistema desenvolvido por:
    - Guilherme Lenzi de Oliveira
    - Taimisson de Carvalho Schardosim
    """)

def main() -> None:
    informacao_sistema_alunos()

    time.sleep(1.5)
    banner("SIMULAÇÃO DO SISTEMA DA BIBLIOTECA")

    banner("1. Cadastro de Livros")
    livros = [
        Livro("Tornar-se Pessoa", "Carl R. Rogers", "978-8578270858"),
        Livro("Entendendo Algoritmos", "Aditya Y. Bhargava", "978-8575225639"),
    ]
    for livro in livros:
        print(livro)
    time.sleep(1.5)

    banner("2. Cadastro de Usuários")
    aluno1  = Aluno("Taimisson de Carvalho Schardosim", "Ciência da Computação")
    aluno2  = Aluno("Guilherme Lenzi de Oliveira",       "Ciência da Computação")
    prof1   = Professor("Maria Adelina Raupp Sganzerla", "Departamento de Ciência da Computação")

    for usuario in (aluno1, aluno2, prof1):
        print(usuario.exibir_tipo_usuario())
    time.sleep(1.5)

    banner("3. Empréstimos Iniciais")
    emprestimos = []

    print(f"O livro '{livros[0].titulo}' será emprestado para o aluno '{aluno1.nome}'")
    print(f"O livro '{livros[1].titulo}' será emprestado para o professor '{prof1.nome}'")
    time.sleep(1.5)

    try:
        emprestimos.append(Emprestimo(livros[0], aluno1))
        emprestimos.append(Emprestimo(livros[1], prof1))
        
        # Tentativa de emprestar o mesmo livro para outro aluno
        print("\nTentando emprestar o mesmo livro para outro aluno...")
        emprestimos.append(Emprestimo(livros[0], aluno2))
    except ValueError as e:
        print(f"Erro: {e}")

    banner("4. Lista de Empréstimos Ativos")
    for emp in emprestimos:
        print(emp, end="\n\n")
    time.sleep(1.5)

    banner("5. Devolução de Livro")
    emprestimos[0].concluir()
    print(f"O livro '{livros[0].titulo}' foi devolvido com sucesso.\n")
    time.sleep(1.5)

    banner("6. Novo Empréstimo do Livro Devolvido")
    try:
        emprestimos.append(Emprestimo(livros[0], aluno2))
        print(f"O livro '{livros[0].titulo}' foi emprestado com sucesso para '{aluno2.nome}'")
    except ValueError as e:
        print(f"Erro: {e}")

    banner("7. Empréstimos Finais")
    for emp in emprestimos:
        print(emp, end="\n\n")

    banner("FIM DA DEMONSTRAÇÃO")


if __name__ == "__main__":
    main()

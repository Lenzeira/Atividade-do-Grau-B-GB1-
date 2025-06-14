import datetime

# --- DEFINIÇÃO DAS CLASSES ---

class Livro:
    """Representa um livro na biblioteca."""
    def __init__(self, titulo: str, autor: str, isbn: str):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def emprestar(self):
        """Marca o livro como indisponível para empréstimo."""
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado com sucesso!")
            return True
        else:
            print(f"Desculpe, o livro '{self.titulo}' não está disponível para empréstimo.")
            return False

    def devolver(self):
        """Marca o livro como disponível após a devolução."""
        self.disponivel = True
        print(f"O livro '{self.titulo}' foi devolvido e agora está disponível.")

    def exibir_informacoes(self):
        """Exibe os dados completos do livro."""
        status = "Disponível" if self.disponivel else "Emprestado"
        print(f"--- Info Livro ---\nTítulo: {self.titulo}\nAutor: {self.autor}\nISBN: {self.isbn}\nStatus: {status}")

class Usuario:
    """Classe base para os usuários da biblioteca."""
    def __init__(self, nome: str, id_usuario: int):
        self.nome = nome
        self.id_usuario = id_usuario

    def exibir_tipo_usuario(self):
        """Método base para exibir o tipo de usuário."""
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

class Aluno(Usuario):
    """Representa um usuário do tipo Aluno."""
    def __init__(self, nome: str, id_usuario: int, curso: str):
        super().__init__(nome, id_usuario)
        self.curso = curso

    def exibir_tipo_usuario(self) -> str:
        """Retorna a string identificando o usuário como Aluno."""
        return f"{self.nome} (Aluno do curso de {self.curso})"

class Professor(Usuario):
    """Representa um usuário do tipo Professor."""
    def __init__(self, nome: str, id_usuario: int, departamento: str):
        super().__init__(nome, id_usuario)
        self.departamento = departamento

    def exibir_tipo_usuario(self) -> str:
        """Retorna a string identificando o usuário como Professor."""
        return f"{self.nome} (Professor do departamento de {self.departamento})"

class Emprestimo:
    """Gerencia o empréstimo de um livro para um usuário."""
    def __init__(self, livro: Livro, usuario: Usuario):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = datetime.date.today()
        # A data de devolução poderia ser calculada, ex: hoje + 15 dias
        self.data_devolucao = self.data_emprestimo + datetime.timedelta(days=15)

    def exibir_resumo_emprestimo(self):
        """Mostra um resumo com os dados do empréstimo."""
        print("\n--- Resumo do Empréstimo ---")
        print(f"Livro: {self.livro.titulo}")
        print(f"Usuário: {self.usuario.exibir_tipo_usuario()}")
        print(f"Data do Empréstimo: {self.data_emprestimo.strftime('%d/%m/%Y')}")
        print(f"Data para Devolução: {self.data_devolucao.strftime('%d/%m/%Y')}")
        print("--------------------------")


# --- FUNÇÃO PRINCIPAL (MAIN) PARA SIMULAÇÃO ---

def main():
    """Função principal que simula o uso do sistema da biblioteca."""
    print("### Início da Simulação do Sistema da Biblioteca ###\n")

    # 1. Cadastro de Livros
    print("--- 1. Cadastrando Livros ---")
    livro1 = Livro("Introdução à POO", "Carlos Silva", "978-85-12345-67-8")
    livro2 = Livro("Estruturas de Dados em Python", "Maria Souza", "978-85-98765-43-2")
    livro3 = Livro("Inteligência Artificial", "Ana Costa", "978-85-54321-98-7")
    livro1.exibir_informacoes()
    print("-" * 20)
    livro2.exibir_informacoes()
    print("-" * 20)
    livro3.exibir_informacoes()

    # 2. Cadastro de um Aluno e um Professor
    print("\n--- 2. Cadastrando Usuários ---")
    aluno = Aluno("João Silva", 101, "Engenharia de Software")
    professor = Professor("Dra. Beatriz Lima", 202, "Ciência da Computação")
    print(f"Usuário cadastrado: {aluno.exibir_tipo_usuario()}")
    print(f"Usuário cadastrado: {professor.exibir_tipo_usuario()}")

    # 3. Empréstimo de Livros
    print("\n--- 3. Realizando Empréstimos ---")
    emprestimos = []

    # Tentativa de emprestar o livro1 para o aluno
    if livro1.emprestar():
        emprestimo1 = Emprestimo(livro1, aluno)
        emprestimos.append(emprestimo1)
    
    # Tentativa de emprestar o livro3 para o professor
    if livro3.emprestar():
        emprestimo2 = Emprestimo(livro3, professor)
        emprestimos.append(emprestimo2)

    # Tentativa de emprestar o livro1 novamente (que já está emprestado)
    print("\nTentando emprestar um livro já em uso:")
    if livro1.emprestar():
        # Este bloco não será executado
        emprestimo_extra = Emprestimo(livro1, professor)
        emprestimos.append(emprestimo_extra)

    # 4. Exibição de dados do empréstimo e dos usuários
    print("\n--- 4. Exibindo Dados dos Empréstimos Atuais ---")
    if not emprestimos:
        print("Nenhum empréstimo ativo.")
    else:
        for emp in emprestimos:
            emp.exibir_resumo_emprestimo()

    # 5. Devolução de livros e atualização da disponibilidade
    print("\n--- 5. Realizando Devolução ---")
    print(f"Status do livro '{livro1.titulo}' antes da devolução: {'Disponível' if livro1.disponivel else 'Emprestado'}")
    livro1.devolver()
    print(f"Status do livro '{livro1.titulo}' após a devolução: {'Disponível' if livro1.disponivel else 'Emprestado'}")

    print("\n### Fim da Simulação ###")


# Executa a função principal
if __name__ == "__main__":
    main()
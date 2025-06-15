from datetime import date, timedelta # timedelta é para calcular a data de devolução
from .livro import Livro
from .usuario import Usuario

class Emprestimo:
    def __init__(self, livro: Livro, usuario: Usuario, prazo_dias: int = 15):
        if not livro.disponivel:
            raise ValueError(f"{livro.titulo} indisponível para empréstimo")
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = date.today()
        self.data_devolucao = self.data_emprestimo + timedelta(days=prazo_dias)
        self.ativo = True
        livro.emprestar()

    def concluir(self) -> None:
        self.ativo = False
        self.livro.devolver()

    def __str__(self) -> str:
        if not self.ativo:
            return f"[DEVOLVIDO] {self.livro.titulo} -> {self.usuario.nome}"
        return (f"Livro: {self.livro.titulo}\n"
                f"Usuário: {self.usuario.exibir_tipo_usuario()}\n"
                f"Data de empréstimo: {self.data_emprestimo:%d/%m/%Y}\n"
                f"Devolver até: {self.data_devolucao:%d/%m/%Y}\n")
    

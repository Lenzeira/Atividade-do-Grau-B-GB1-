from dataclasses import dataclass

@dataclass
class Livro:
    titulo: str
    autor: str 
    isbn: str
    disponivel: bool = True


    def emprestar(self) -> None: # a flecha é para indicar que o metodo não retorna nada
        if not self.disponivel:
            raise ValueError(f"{self.titulo} não está disponível")
        self.disponivel = False

    def devolver(self) -> None:
        self.disponivel = True

    def __str__(self) -> str:
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"Livro: {self.titulo} - {self.autor} - ISBN: {self.isbn} - {status}"

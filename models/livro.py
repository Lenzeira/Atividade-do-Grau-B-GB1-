from dataclasses import dataclass
from datetime import date
from typing import Optional
from .usuario import Usuario

@dataclass
class Livro:
    titulo: str
    autor: str 
    isbn: str
    disponivel: bool = True
    usuario: Optional[Usuario] = None
    data_devolucao: Optional[date] = None

    def emprestar(self, usuario: Usuario, data_devolucao: date) -> None:
        if not self.disponivel:
            raise ValueError(f"{self.titulo} não está disponível")
        self.disponivel = False
        self.usuario = usuario
        self.data_devolucao = data_devolucao

    def devolver(self) -> None:
        self.disponivel = True
        self.usuario = None
        self.data_devolucao = None

    def __str__(self) -> str:
        status = "Disponível" if self.disponivel else f"Emprestado para {self.usuario.nome} até {self.data_devolucao:%d/%m/%Y}"
        return f"Livro: {self.titulo} - {self.autor} - ISBN: {self.isbn} - {status}"

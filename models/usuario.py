from abc import ABC, abstractmethod
from dataclasses import dataclass, field

class Usuario(ABC):
    _contador = 0

    def __init__(self, nome: str):
        self.nome = nome
        Usuario._contador += 1
        self.id_usuario = Usuario._contador

    @abstractmethod
    def exibir_tipo_usuario(self) -> str:
        pass

@dataclass
class Aluno(Usuario):
    nome: str
    curso: str
    id_usuario: int = field(init=False)

    def __post_init__(self):
        super().__init__(self.nome)

    def exibir_tipo_usuario(self) -> str:
        return f"Aluno: {self.nome} - Curso: {self.curso}"
    
@dataclass
class Professor(Usuario):
    nome: str
    departamento: str
    id_usuario: int = field(init=False)

    def __post_init__(self):
        super().__init__(self.nome)

    def exibir_tipo_usuario(self) -> str:
        return f"Professor: {self.nome} - Departamento: {self.departamento}"
from abc import ABC

class Person(ABC):
 def __init__(self, name: str, age: int, cpf: str):
   self.name: str  = name
   self.age: int = age
   self.cpf: str = cpf
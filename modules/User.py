from modules.Person import Person


class User(Person):
    
    def __init__(
        self, 
        name: str,
        age: int,
        cpf: str,
        login: str, 
        password: str, 
        email: str
    ): 
        super().__init__(name, age, cpf)
        self.login: str = login
        self.password: str = password
        self.email: str = email
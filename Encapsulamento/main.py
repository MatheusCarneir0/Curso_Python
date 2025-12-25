"""
Encapsulamento em Python - Atributos Privados
public, protected, private
_ (protected) -> convenção para atributos/métodos protegidos
__ (private) -> atributos/métodos privados
"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if "clientes" not in self.__dados:
            self.__dados["clientes"] = {id: nome}
        else:
            self.__dados["clientes"].update({id: nome})

    def listar_clientes(self):
        for id, nome in self.__dados["clientes"].items():
                print(f'ID: {id}, Nome: {nome}')

    def apagar_cliente(self, id):
        # if "clientes" in self.__dados and id in self.__dados["clientes"]:
            del self.__dados["clientes"][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Matheus')
bd.inserir_cliente(2, 'Vitória')
bd.inserir_cliente(3, 'João')
print(bd.dados)
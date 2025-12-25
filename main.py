from pessoa import Pessoa           

# p1 = Pessoa('Matheus', 2000)
# p2 = Pessoa('Maria', 2005)


p1 = Pessoa('Matheus', 2000)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
print(Pessoa.gera_id())
print(f'{p1.nome} - ID {p1.gera_id()}')
from pessoa import Pessoa           

p1 = Pessoa('Matheus', 2000)
p2 = Pessoa('Maria', 2005)


print(f'{p1.nome} tem {p1.get_ano_nascimento()}')
print(p2.get_ano_nascimento())
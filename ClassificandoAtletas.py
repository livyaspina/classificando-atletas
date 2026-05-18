from datetime import date   #CONSEGUE OBTER A IDADE ATUAL DE ACORDO COM O ANO
atual = date.today().year
data = int (input("Qual seu ano de nascimento? "))
idade = atual - data
print("O atleta tem {} anos".format(idade))

if idade <= 9:
    print("Categoria MIRIM")
elif idade <= 14:
    print("Categoria INFANTIL")
elif idade <= 19:
    print("Categoria JÚNIOR")
elif idade <= 25:
    print("Categoria SÊNIOR")
else: 
    print("Categoria MASTER")
    
    
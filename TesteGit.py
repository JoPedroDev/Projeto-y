nome = input('Qual o seu nome? ')
print(f'Bem vindo, {nome}')
idade = int(input('Qual a sua idade? '))
if idade >= 18:
    print('Ok, voçe é maior de idade')
else:
    print('Voçe ainda é menor de idade')
nome = input('Qual o seu nome? ').capitalize()
print(f'Bem vindo, {nome}')
idade = int(input('Qual a sua idade? '))
if idade >= 18:
    print('Ok, voçe é maior de idade')
else:
    print('Voçe ainda é menor de idade')
print('Desenvolvimento de software é considerado complexo, não exige esforço físico mas bastante mental')
tempo = input(f'Faz quanto tempo {nome}, que voçe estuda Desenvolvimento de Software? ')
if '1' and 'ano' in tempo:
    print('Já faz um bom tempo, se ainda não está trabalhando com isso, logo irá se for da tua vontade')
elif '1' and 'mes' in tempo:
    print('Decisão recente, te desejo bons estudos, logo irá poder atuar na área')
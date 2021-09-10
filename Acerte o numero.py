import random

resu = random.randint (1, 10)
resposta = 0
x = 1 #X é as tentaivas, preguiça de mudar
record1 = 1
record2 = 1
record3 = 2

print ('''------NÍVEIS------
1 = 15 tentativas
2 = 10 tentativas
3 = 5 tentativas ''')
print ("--"*9)
print ("""Os records são:
Nivel 1= {}x
Nivel 2= {}x
Nivel 3= {}x""".format (record1, record2, record3))
print ("--"*9)
duvidas = input('Você quer entender como funciona? [S/N]: ').upper ()
escolha = int(input('Digite um número para escolher a difículdade [1/2/3]: '))

while escolha > 3:
    print ('Erro tente novamente')
    escolha = int(input('Digite um número para escolher a difículdade [1/2/3]: '))
    if escolha <= 3:
        break

if duvidas == "S":
    print ('''-----------------------------------------------------------------------------------------------------
O jogo funciona assim:

Você irá tentar acertar o número que o computador estiver pensando, ele vai mudar toda vez o núemero.
-----------------------------------------------------------------------------------------------------''')

if escolha == 3: 
    while resposta != resu:
        resu = random.randint (1, 10)
        resposta = int(input('Digite um número entre 1 a 10: '))
        print ('Já foram {}x de 5'.format (x))
        x = x + 1 
        if x == 5: 
            print ('Você atingiu o maximo de tentativas possiveis')
            break

elif escolha == 2: 
    while resposta != resu: 
        resu = random.randint (1, 10)
        resposta = int(input('Digite um número entre 1 a 10: '))
        print ('Já foram {}x de 10'.format (x))
        x = x + 1 
        if x == 10: 
            print ('Você atingiu o maximo de tentativas possiveis')
            break

elif escolha == 1: 
    while resposta != resu:  
        resu = random.randint (1, 10)
        resposta = int(input('Digite um número entre 1 a 10: '))
        print ('Já foram {}x de 15'.format (x))
        x = x + 1 
        if x == 15: 
            print ('Você atingiu o maximo de tentativas possiveis')
            break



print ('--'*4)
print ('Acabou')
print ('Você tentou: {}x'.format (x))

if resu == resposta:
    print ('--'*4)
    print ('Você acertou o número')


elif escolha == 3:
	if x < 5:
		record3 -= record3
		record3 = x
		print ("Você bateu o record do dificil, agora é: {}".format (x))

elif escolha == 2:
	if x < 5:
		record2 -= record2
		record2 = x
		print ("Você bateu o record do mediano, agora é: {}".format (x))
		
if escolha == 1:
	if x < 15:
		record1 -= record1
		record1 = x
		print ("Você bateu o record do facil, agora é: {}".format (x))

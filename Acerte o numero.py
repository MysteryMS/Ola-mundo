#Esse seria o Beta, ainda ta em processo de desenvolvimento
import random

resu = random.randint (1, 10)
resposta = 0
x = 0 #X é as tentaivas, preguiça de mudar
record1 = 15
record2 = 5
record3 = 5

print ('''------NÍVEIS------
1 = 15 tentativas
2 = 10 tentativas
3 = 5 tentativas ''')
print ("--"*9)
print ("""Os records são:
Nivel 1= 5x
Nivel 2= 5x
Nivel 3= 15x""")
print ("--"*9)
escolha = int(input('Digite um número para escolher a difículdade [1/2/3]: '))

if escolha == 3: 
    while resposta != resu: 
        
        resu = random.randint (1, 10)
        print (resu)
        resposta = int(input('Digite um número entre 1 a 10: '))
        x = x + 1 
        if x == 5: 
            print ('Você atingiu o maximo de tentativas possiveis')
            break

if escolha == 2: 
    while resposta != resu: 
        
        resu = random.randint (1, 10)
        print (resu)
        resposta = int(input('Digite um número entre 1 a 10: '))
        x = x + 1 
        if x == 10: 
            print ('Você atingiu o maximo de tentativas possiveis')
            break

if escolha == 1: 
    while resposta != resu: 
        resu = random.randint (1, 10)
        print (resu)
        resposta = int(input('Digite um número entre 1 a 10: '))
        x = x + 1 
        if x == 15: 
            print ('Você atingiu o maximo de tentativas possiveis')
            break

print ('-=-'*4)
print ('Acabou')
print ("Tentativas: {}".format (x))

if escolha == 3:
	if x < 5:
		record3 -= record3
		record3 = x
		print ("Você bateu o record do dificil, agora o record é: {}".format (x))

if escolha == 2:
	if x < 5:
		record2 -= record2
		record2 = x
		print ("Você bateu o record do mediano, agora o record é: {}".format (x))
		
if escolha == 1:
	if x < 15:
		record1 -= record1
		record1 = x
		print ("Você bateu o record do facil, agora o record é: {}".format (x))
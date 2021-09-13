import random

resultado = random.randint(1, 10)
respostaDoJogador = 0
tentativas = 0
record1 = 5
record2 = 6
record3 = 3
TentarNovamente = 'S'


def como_jogar():
    resposta = input(
        'Você quer entender como funciona o jogo? [S/N]: ').lower()
    if resposta == 's' or resposta == 'n':
        return resposta
    else:
        print('--'*9)
        print('Erro tente novamente')
        como_jogar()


def dificuldade():
    difi = int(input('Digite um número para escolher a difículdade [1/2/3]: '))
    if difi == 1 or difi == 2 or difi == 3:
        return difi
    else:
        print('--'*9)
        print('Erro tente novamente')
        dificuldade()


while True:  # a pergunta para que ele quer tentar de novo vai aparecer na linha 107

    print('''------NÍVEIS------
1 = 15 tentativas
2 = 10 tentativas           
3 = 5 tentativas ''')
    print("--"*9)
    print("""  Os records são:
    Nivel 1= {}x
    Nivel 2= {}x
    Nivel 3= {}x""".format(record1, record2, record3))
    print("--"*9)

    ComoJogar = como_jogar()
    NivelDaDificuldade = dificuldade()

    if ComoJogar == 's':
        print('''---------------------------------------------------------------------------------------------------------
                            O jogo funciona assim:
    * Você ira tentar acertar o número que o computador estiver pensando, ele vai mudar toda vez o número;
    * Enquanto você errar ele não vai parar de rodar, a menos que ele atinja o seu limite de tentativas;
    OBS: Toda vez que você erra ele muda de número;
    ---------------------------------------------------------------------------------------------------------''')

    if NivelDaDificuldade == 3:
        while respostaDoJogador != resultado:
            tentativas = tentativas + 1
            resultado = random.randint(1, 10)
            respostaDoJogador = int(input('Digite um número entre 1 a 10: '))
            print('Já foram {}x de 5'.format(tentativas))
            if tentativas == 5:
                print('Você atingiu o maximo de tentativas possiveis')
                break

    elif NivelDaDificuldade == 2:
        while respostaDoJogador != resultado:
            tentativas = tentativas + 1
            resultado = random.randint(1, 10)
            respostaDoJogador = int(input('Digite um número entre 1 a 10: '))
            print('Já foram {}x de 10'.format(tentativas))
            if tentativas == 10:
                print('Você atingiu o maximo de tentativas possiveis')
                break

    elif NivelDaDificuldade == 1:
        while respostaDoJogador != resultado:
            tentativas = tentativas + 1
            resultado = random.randint(1, 10)
            respostaDoJogador = int(input('Digite um número entre 1 a 10: '))
            print('Já foram {}x de 15'.format(tentativas))
            if tentativas == 15:
                print('Você atingiu o maximo de tentativas possiveis')
                break

    print('--'*4)
    print('Acabou o jogo')
    print('Você tentou: {}x'.format(tentativas))

    if resultado == respostaDoJogador:
        print('--'*4)
        print('Você GANHOU o jogo')
        print('Você acertou o número ')

    elif NivelDaDificuldade == 3:
        if tentativas < 3:
            print("Você bateu o record do dificil, agora é: {}".format(tentativas))

    elif NivelDaDificuldade == 2:
        if tentativas < record2:
            print("Você bateu o record do mediano, agora é: {}".format(tentativas))

    elif NivelDaDificuldade == 1:
        if tentativas < record1:
            print("Você bateu o record do facil, agora é: {}".format(tentativas))

    TentarNovamente = input('Você deseja continuar [S/N]: ').lower()
    if TentarNovamente == 'n':
        print('--'*4)
        print('--'*4)
        break

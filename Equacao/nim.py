def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        if n % (m+1) > 0:
            return n % (m+1)
        return m

def campeonato(n):
    c = 0
    if computador_escolhe_jogada(n,m) == 0:
        c = c + 1
        if c == 3:
            print("O computador ganhou!")
            print("Placar: Você 0 X 3 Computador")
    elif compuatador_escolhe_jogada(n,m) != 0:
        return usuario_escolhe_jogada(n, m)
            
    
def usuario_escolhe_jogada(n, m):
    x = 0
    while x != m:
        x = int(input("Quantas peças você vai tirar? "))
        if x <= m and x > 0:
            n = n - x
            print("Você tirou ", x, " peças")
            print("Agora resta ", n, " peças no tabuleiro")
            return n
        else:
            print("Jogada inválida, tente de novo!")
        
        
def partida():
    i = 0
    resp = 0
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("[1] - Para jogar uma partida isolada: ")
    print("[2] - Para jogar um campeonato: ")
    while resp != 1 or resp != 2:
        resp = int(input("escolha uma opção ==> "))
        if resp == 1:
            print("Você escolheu partida Isolada!")
            print("==="*10)
            return pecas()
        elif resp == 2:
            print("Você escolheu Campeonato!")
            while i <= 3:
                i =+ 1
                print("*** RODADA ", i, "***")
                return pecas()
        else:
            print("Opção Inválida! Tente novamente")
            

def pecas():            
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    resto = n % (m + 1)
    if resto == 0:
        print("Você começa!")
        print("==="*10)
        return usuario_escolhe_jogada(n, m)
    else:
        print("Computador começa!")
        print("==="*10)
        return computador_escolhe_jogada(n, m)


partida()

def menu():
    print("Bem-vindo ao jogo do NIM!")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    
    escolha = int(input("Escolha: "))
    print("===" * 10)
    while escolha != 1 and escolha != 2:
        print("Escolha uma opção válida!")
        escolha = int(input("Escolha: "))
        print("===" * 10)
        
    if escolha == 1:
        print("\nVocê escolheu uma partida isolada!\n")
        print("===" * 10)
        partida()
    else:
        if escolha == 2:
            print("\nVocê escolheu um campeonato!\n")
            print("===", * 10)
            campeonato()
            
def campeonato():
    rodada = 1
    placar_computador = placar_usuario = 0
    
    while rodada < 4:
        print("**** Rodada", rodada ,"****\n")
        if partida() == 1:
            usuario =+ 1
        else:
            computador =+ 1
        rodada =+ 1
        
    print("**** Final do campeonato! ****\n")
    print("Placar: Você", usuario, "X", computador, "Computador")
            
def computador_escolhe_jogada(n, m):    
    if n <= m:
        return n
    else:
        if n % (m+1) > 0:
            return n % (m+1)
        return m

def usuario_escolhe_jogada(n, m):
    x = int(input("\nQuantas peças você vai tirar? "))
    print("===" * 10)
    while x > m or x <= 0 or x > n:    
        print("Oops! Jogada inválida! Tente de novo.")
        x = int(input("\nQuantas peças você vai tirar? "))
        print("===" * 10)    
    return x

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print("===" * 10)
    while m < 1:
        print("A quantidade de peças por jogadas devem ser menor ou igual as peças totais")
        m = int(input("Limite de peças por jogada? "))
        print("===" * 10)
    
    x = 0
    j = 0
    if (n % (m+1)) == 0:
        print("\nVocê começa!")
        j = 1 
        while n > 0:
            if j == 1:
                valor = usuario_escolhe_jogada(n, m)
                print("\nVocê tirou", x, "peça(s).")
                n = n - x
                print("Agora restam", n, "peças no tabuleiro.")
                print("===" * 10)
                j = 2
            else:
                x = computador_escolhe_jogada(n, m)
                print("\nO computador tirou", x, "peça(s)")
                n = n - x
                print("Agora restam", n, "peças no tabuleiro.")
                print("===" * 10)
                j = 1
                
        if j == 1:
            print("Fim do jogo! O computador ganhou!\n")
            return 2 
        else:
            print("Fim do jogo! Você ganhou!\n")
            print("===" * 10)
            return 1 
                
    else:
        print("\nComputador começa!")
        j = 2 
        while n > 0:
            if j == 2:
                x = computador_escolhe_jogada(n, m)
                print("\nO computador tirou", x, "peça(s)")
                n = n - x
                print("Agora restam", n, "peças no tabuleiro.")
                print("===" * 10)
                j = 1
            else:
                x = usuario_escolhe_jogada(n, m)
                print("\nVocê tirou", x, "peça(s).")
                n = n - x
                print("Agora restam", n, "peças no tabuleiro.")
                print("===" * 10)
                j = 2
                
        if j == 1:
            print("Fim do jogo! O computador ganhou!\n")
            print("===" * 10)
            return 2
        else:
            print("Fim do jogo! O você ganhou!\n")
            print("===" * 10)
            return 1

menu()

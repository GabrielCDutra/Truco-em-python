import random

# Cartas do baralho: =========================================================================================

baralho = ['4o', '4e', '4c', '4p', '5o', '5e', '5c', '5p', '6o', '6e', '6c', '6p',
           '7o', '7e', '7c', '7p', 'Qo', 'Qe', 'Qc', 'Qp', 'Jo', 'Je', 'Jc', 'Jp',
           'Ko', 'Ke', 'Kc', 'Kp', 'Ao', 'Ae', 'Ac', 'Ap', '2o', '2e', '2c', '2p',
           '3o', '3e', '3c', '3p']

# Distribuição das cartas: =========================================================================================

carta1 = baralho.pop(random.randint(0,39))
carta2 = baralho.pop(random.randint(0,38))
carta3 = baralho.pop(random.randint(0,37))

mao1 = [carta1, carta2, carta3]

carta4 = baralho.pop(random.randint(0,36))
carta5 = baralho.pop(random.randint(0,35))
carta6 = baralho.pop(random.randint(0,34))

mao2 = [carta4, carta5, carta6]

print("Mão do jogador 1 -> ",*mao1)
print("Mão do jogador 2 -> ",*mao2)

vira = baralho.pop(random.randint(0,33))

print("Vira -> ",vira)

baralho = ['4o', '4e', '4c', '4p', '5o', '5e', '5c', '5p', '6o', '6e', '6c', '6p',
           '7o', '7e', '7c', '7p', 'Qo', 'Qe', 'Qc', 'Qp', 'Jo', 'Je', 'Jc', 'Jp',
           'Ko', 'Ke', 'Kc', 'Kp', 'Ao', 'Ae', 'Ac', 'Ap', '2o', '2e', '2c', '2p',
           '3o', '3e', '3c', '3p']

if (baralho.index(vira)/4 - (baralho.index(vira)%4)/4) < 9:
    manilha = (baralho.index(vira)/4 - (baralho.index(vira)%4)/4) + 1
else:
    manilha = 0
    
# Primeira rodada: =========================================================================================

print()
print(*mao1)
print()
jogada1 = input("Jogador 1 -> ")

if jogada1 == mao1[0]:
    j1 = mao1.pop(0)
elif jogada1 == mao1[1]:
    j1 = mao1.pop(1)
elif jogada1 == mao1[2]:
    j1 = mao1.pop(2)
else:
    j1 = mao1.pop(random.randint(0,2))

print(j1)
  
if (baralho.index(j1)/4 - (baralho.index(j1)%4)/4) == manilha:
    j1 = (baralho.index(j1)/4) + 10
else:
    j1 = (baralho.index(j1)/4 - (baralho.index(j1)%4)/4)
    
print(j1)
    
    
    
print()
print(*mao2)
print()
jogada2 = input("Jogador 2 -> ")

if jogada2 == mao2[0]:
    j2 = mao2.pop(0)
elif jogada2 == mao2[1]:
    j2 = mao2.pop(1)
elif jogada2 == mao2[2]:
    j2 = mao2.pop(2)
else:
    j2 = mao2.pop(random.randint(0,2))

print(j2)

if (baralho.index(j2)/4 - (baralho.index(j2)%4)/4) == manilha:
    j2 = (baralho.index(j2)/4) + 10
else:
    j2 = (baralho.index(j2)/4 - (baralho.index(j2)%4)/4)
    
print(j2)
    
# Resultado da primeira rodada: =========================================================================================

pontos1 = 0
pontos2 = 0
desempate = 0
vencedor = 0

print()
if j1 > j2:
    pontos1 = pontos1 + 1
    desempate = 1
    vencedor = 1
    print("j1 ganhou")
elif j1 < j2:
    pontos2 = pontos2 + 1
    desempate = 2
    vencedor = 2
    print("j2 ganhou")
else:
    pontos1 = pontos1 + 1
    pontos2 = pontos2 + 1
    vencedor = 2
    print("melou")

print()
print(pontos1)
print(pontos2)

# Segunda rodada: =========================================================================================

if vencedor == 1:
    print()
    print(*mao1)
    print()
    jogada1 = input("Jogador 1 -> ")
    
    if jogada1 == mao1[0]:
        j1 = mao1.pop(0)
    elif jogada1 == mao1[1]:
        j1 = mao1.pop(1)
    else:
        j1 = mao1.pop(random.randint(0,1))
    
    print(j1)
      
    if (baralho.index(j1)/4 - (baralho.index(j1)%4)/4) == manilha:
        j1 = (baralho.index(j1)/4) + 10
    else:
        j1 = (baralho.index(j1)/4 - (baralho.index(j1)%4)/4)
        
    print(j1)
    
    
    
    print()
    print(*mao2)
    print()
    jogada2 = input("Jogador 2 -> ")
    
    if jogada2 == mao2[0]:
        j2 = mao2.pop(0)
    elif jogada2 == mao2[1]:
        j2 = mao2.pop(1)
    else:
        j2 = mao2.pop(random.randint(0,1))
    
    print(j2)
    
    if (baralho.index(j2)/4 - (baralho.index(j2)%4)/4) == manilha:
        j2 = (baralho.index(j2)/4) + 10
    else:
        j2 = (baralho.index(j2)/4 - (baralho.index(j2)%4)/4)
        
    print(j2)

else:
    print()
    print(*mao2)
    print()
    jogada2 = input("Jogador 2 -> ")
    
    if jogada2 == mao2[0]:
        j2 = mao2.pop(0)
    elif jogada2 == mao2[1]:
        j2 = mao2.pop(1)
    else:
        j2 = mao2.pop(random.randint(0,1))
    
    print(j2)
    
    if (baralho.index(j2)/4 - (baralho.index(j2)%4)/4) == manilha:
        j2 = (baralho.index(j2)/4) + 10
    else:
        j2 = (baralho.index(j2)/4 - (baralho.index(j2)%4)/4)
        
    print(j2)
    
    
    
    print()
    print(*mao1)
    print()
    jogada1 = input("Jogador 1 -> ")
    
    if jogada1 == mao1[0]:
        j1 = mao1.pop(0)
    elif jogada1 == mao1[1]:
        j1 = mao1.pop(1)
    else:
        j1 = mao1.pop(random.randint(0,1))
    
    print(j1)
      
    if (baralho.index(j1)/4 - (baralho.index(j1)%4)/4) == manilha:
        j1 = (baralho.index(j1)/4) + 10
    else:
        j1 = (baralho.index(j1)/4 - (baralho.index(j1)%4)/4)
        
    print(j1)

# Resultado da segunda rodada: =========================================================================================

final = 0

print()
if j1 > j2:
    pontos1 = pontos1 + 1
    vencedor = 1
    print("j1 ganhou")
elif j1 < j2:
    pontos2 = pontos2 + 1
    vencedor = 2
    print("j2 ganhou")
else:
    pontos1 = pontos1 + 1
    pontos2 = pontos2 + 1
    print("melou")

if pontos1 == 2:
    vencedor = 0
    final = 1
    print("JOGADOR UM VENCEU!!!")

if pontos2 == 2:
    vencedor = 0
    final = 1
    print("JOGADOR DOIS VENCEU!!!")
    

print()
print(pontos1)
print(pontos2)

# Última rodada: =========================================================================================

if vencedor == 1:
    print()
    print(*mao1)
    print()
    jogada1 = input("Jogador 1 -> ")
    
    j1 = mao1.pop(0)
    
    print(j1)
      
    if (baralho.index(j1)/4 - (baralho.index(j1)%4)/4) == manilha:
        j1 = (baralho.index(j1)/4) + 10
    else:
        j1 = (baralho.index(j1)/4 - (baralho.index(j1)%4)/4)
        
    print(j1)
    
    
    
    print()
    print(*mao2)
    print()
    jogada2 = input("Jogador 2 -> ")
    
    j2 = mao2.pop(0)
    
    print(j2)
    
    if (baralho.index(j2)/4 - (baralho.index(j2)%4)/4) == manilha:
        j2 = (baralho.index(j2)/4) + 10
    else:
        j2 = (baralho.index(j2)/4 - (baralho.index(j2)%4)/4)
        
    print(j2)
    
elif vencedor == 2:
    print()
    print(*mao2)
    print()
    jogada2 = input("Jogador 2 -> ")
    
    j2 = mao2.pop(0)
    
    print(j2)
    
    if (baralho.index(j2)/4 - (baralho.index(j2)%4)/4) == manilha:
        j2 = (baralho.index(j2)/4) + 10
    else:
        j2 = (baralho.index(j2)/4 - (baralho.index(j2)%4)/4)
        
    print(j2)
    
    
    print()
    print(*mao1)
    print()
    jogada1 = input("Jogador 1 -> ")
    
    j1 = mao1.pop(0)
    
    print(j1)
      
    if (baralho.index(j1)/4 - (baralho.index(j1)%4)/4) == manilha:
        j1 = (baralho.index(j1)/4) + 10
    else:
        j1 = (baralho.index(j1)/4 - (baralho.index(j1)%4)/4)
        
    print(j1)
    
# Resultado da última rodada: =========================================================================================

print()
if final != 1:
    if j1 > j2:
        pontos1 = pontos1 + 1
        print("j1 ganhou")
    elif j1 < j2:
        pontos2 = pontos2 + 1
        print("j2 ganhou")
    else:
        print("melou")
    
    if pontos1 == 2:
        print("JOGADOR UM VENCEU!!!")
    elif pontos2 == 2:
        print("JOGADOR DOIS VENCEU!!!")
    else:
        if desempate == 1:
            print("JOGADOR UM VENCEU!!!")
        else:
            print("JOGADOR DOIS VENCEU!!!")


    print()
    print(pontos1)
    print(pontos2)
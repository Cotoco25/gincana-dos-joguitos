import random
vida = 6
lista_palavras = ["arroz", "banana", "queijo", "alface", "frango"]

palavra_escolhida = random.choice(lista_palavras)
print(palavra_escolhida)
while vida >0:
    letra = input("Qual letra vc quer?")
    if letra != palavra_escolhida[0]:
        print("errou")
        vida = vida-1
        print(f"sobraram {vida} vidas")
    else:
        print("Acertou!")
    letra != palavra_escolhida[0]
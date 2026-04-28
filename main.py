from pygame import *
import sys
import random


init()

window = display.set_mode((1280,720))

teclado_img = image.load("teclado.webp")
teclado_img = transform.scale(teclado_img, (1200,300))

running = True
clock=time.Clock()

vidas=6
lista_palavras = ["arroz", "banana", "queijo", "alface", "frango"]
palavra_escolhida = random.choice(lista_palavras)
letras_acertadas = ["_"] * len(palavra_escolhida)

timer_erro = 0

def verificar_letra(letra):
     global vidas, timer_erro, errou_texto, letras_acertadas
     if letra in palavra_escolhida:
        print("Acertou!")
        for i in range(len(palavra_escolhida)):
            if palavra_escolhida[i] == letra:
                letras_acertadas[i] = letra
     else:
        vidas-=1
        timer_erro = 120

background_color = (112, 128, 144)
font = font.Font("fonte.ttf", 40)

while running:
    clock.tick(60)
    key_pressed = key.get_pressed()
    window.fill(background_color)
    mouse_x, mouse_y = mouse.get_pos()

    if timer_erro > 0:
        errou_texto = font.render(f"voce errou, e agora tem {vidas} vidas", True, (255,0,0))
        window.blit(errou_texto, (570,100))
        timer_erro -= 1
    
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            running = False
            sys.exit()
        
        if ev.type == MOUSEBUTTONDOWN:
            if 235<mouse_x<296 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("q")
        
        if ev.type == MOUSEBUTTONDOWN:
            if 309<mouse_x<369 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("w")

        if ev.type == MOUSEBUTTONDOWN:
            if 381<mouse_x<443 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("e")

        if ev.type == MOUSEBUTTONDOWN:
            if 454<mouse_x<517 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("r")

        if ev.type == MOUSEBUTTONDOWN:
            if 529<mouse_x<592 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("t")

        if ev.type == MOUSEBUTTONDOWN:
            if 600<mouse_x<664 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("y")

        if ev.type == MOUSEBUTTONDOWN:
            if 677<mouse_x<739 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("u")

        if ev.type == MOUSEBUTTONDOWN:
            if 748<mouse_x<811 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("i")

        if ev.type == MOUSEBUTTONDOWN:
            if 822<mouse_x<883 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("o")

        if ev.type == MOUSEBUTTONDOWN:
            if 895<mouse_x<960 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("p")

        if ev.type == MOUSEBUTTONDOWN:
            if 248<mouse_x<309 and 593<mouse_y<629:
                if ev.button == 1:
                    verificar_letra("a")

        if ev.type == MOUSEBUTTONDOWN:
            if 320<mouse_x<382 and 593<mouse_y<629:
                if ev.button == 1:
                    verificar_letra("s")

        if ev.type == MOUSEBUTTONDOWN:
            if 393<mouse_x<456 and 593<mouse_y<629:
                if ev.button == 1:
                    verificar_letra("d")
                    
        if ev.type == MOUSEBUTTONDOWN:
            if 469<mouse_x<530 and 593<mouse_y<629:
                if ev.button == 1:
                    verificar_letra("f")

        if ev.type == MOUSEBUTTONDOWN:
            if 541<mouse_x<604 and 593<mouse_y<629:
                if ev.button == 1:
                    verificar_letra("g")
        
        if ev.type == MOUSEBUTTONDOWN:
            if 614<mouse_x<677 and 593<mouse_y<629:
                if ev.button == 1:
                    verificar_letra("h")
        
        if ev.type == MOUSEBUTTONDOWN:
            if 688<mouse_x<752 and 593<mouse_y<629:
                if ev.button == 1:
                    verificar_letra("j")
        
        if ev.type == MOUSEBUTTONDOWN:
            if 762<mouse_x<825 and 593<mouse_y<629:
                if ev.button == 1:
                    verificar_letra("k")
        
        if ev.type == MOUSEBUTTONDOWN:
            if 836<mouse_x<896 and 593<mouse_y<629:
                if ev.button == 1:
                    verificar_letra("l")
    
        if ev.type == MOUSEBUTTONDOWN:
            if 278<mouse_x<340 and 637<mouse_y<674:
                if ev.button == 1:
                    verificar_letra("z")
        
        if ev.type == MOUSEBUTTONDOWN:
            if 352<mouse_x<413 and 637<mouse_y<674:
                if ev.button == 1:
                    verificar_letra("x")
    
        if ev.type == MOUSEBUTTONDOWN:
            if 426<mouse_x<488 and 637<mouse_y<674:
                if ev.button == 1:
                    verificar_letra("c")
        
        if ev.type == MOUSEBUTTONDOWN:
            if 499<mouse_x<560 and 637<mouse_y<674:
                if ev.button == 1:
                    verificar_letra("v")
    
        if ev.type == MOUSEBUTTONDOWN:
            if 571<mouse_x<635 and 637<mouse_y<674:
                if ev.button == 1:
                    verificar_letra("b")

        if ev.type == MOUSEBUTTONDOWN:
            if 645<mouse_x<708 and 637<mouse_y<674:
                if ev.button == 1:
                    verificar_letra("n")

        if ev.type == MOUSEBUTTONDOWN:
            if 719<mouse_x<781 and 637<mouse_y<674:
                if ev.button == 1:
                    verificar_letra("m")



    palavra_text = font.render(palavra_escolhida, True, (0,0,0))
    window.blit(palavra_text, (570,400))

    texto_exibido = " ".join(letras_acertadas)
    letras_text = font.render(texto_exibido, True, (0,0,0))
    window.blit(letras_text, (570,200))


    window.blit(teclado_img, (50,450))
    print(mouse_x,mouse_y)
    print(vidas)
                    
    

    display.update()
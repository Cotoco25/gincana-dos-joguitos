from pygame import *
import sys
import random


init()

window = display.set_mode((1280,720))

teclado_img = image.load("teclado.webp")
teclado_img = transform.scale(teclado_img, (1200,300))

running = True
clock=time.Clock()

vidas = 6
lista_palavras = ["arroz", "banana", "queijo", "alface", "frango"]
palavra_escolhida = random.choice(lista_palavras)
letras_acertadas = ["_"] * len(palavra_escolhida)
timer_erro = 0

def verificar_letra(letra):
     if letra in palavra_escolhida:
        print("Acertou!")
        for i in range(len(palavra_escolhida)):
            if palavra_escolhida[i] == letra:
                letras_acertadas[i] = letra
     else:
        vidas = vidas - 1
        timer_erro = 120
        if timer_erro > 0:
            errou_texto = font.render(f"voce errou, e agora tem {vidas} vidas", True, (255,0,0))
            window.blit(errou_texto, (570,100))
            timer_erro = timer_erro - 1

background_color = (112, 128, 144)
font = font.Font("fonte.ttf", 40)

while running:
    clock.tick(60)
    key_pressed = key.get_pressed()
    window.fill(background_color)
    
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            running = False
            sys.exit()
        
        if ev.type == MOUSEBUTTONDOWN:
            if 235<mouse_x<296 and 551<mouse_y<586:
                if ev.button == 2:
                        verificar_letra("q")
                else:
                    vidas = vidas - 1
                    timer_erro = 120
                    if timer_erro > 0:
                        errou_texto = font.render(f"voce errou, e agora tem {vidas} vidas", True, (255,0,0))
                        window.blit(errou_texto, (570,100))
                        timer_erro = timer_erro - 1
                    
        
        
          
                
    
    
    mouse_x, mouse_y = mouse.get_pos()

    palavra_text = font.render(palavra_escolhida, True, (0,0,0))
    window.blit(palavra_text, (570,400))

    texto_exibido = " ".join(letras_acertadas)
    letras_text = font.render(texto_exibido, True, (0,0,0))
    window.blit(letras_text, (570,200))


    window.blit(teclado_img, (50,450))
    print(mouse_x,mouse_y)
    print(vidas)
                    
    

    display.update()
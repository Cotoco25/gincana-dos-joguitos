from pygame import *
import sys
import random

init()

window = display.set_mode((1280,720))

teclado_img = image.load("teclado.webp")
teclado_img = transform.scale(teclado_img, (1200,300))

running = True
clock=time.Clock()

lista_palavras = ["arroz", "banana", "queijo", "alface", "frango"]
palavra = random.choice(lista_palavras)
background_color = (112, 128, 144)
font = font.Font("fonte.ttf", 40)

while running:
    clock.tick(60)
    key_pressed = key.get_pressed()

    for ev in event.get():
        if ev.type == QUIT:
            quit()
            running = False
            sys.exit()
    
    window.fill(background_color)
    mouse_x, mouse_y = mouse.get_pos()

    palavra_text = font.render(palavra, True, (0,0,0))
    window.blit(palavra_text, (570,400))

    window.blit(teclado_img, (50,450))
    print(mouse_x,mouse_y)

    if ev.type == MOUSEBUTTONDOWN:
        while 235<mouse_x<296 and 551<mouse_y<586:
            if ev.button == 2:
                    print("q")
    

    display.update()
from pygame import *
import sys
import random


init()

window = display.set_mode((1280,720))

teclado_img = image.load("teclado.webp")
teclado_img = transform.scale(teclado_img, (1200,300))

coracao = image.load("heart.png")
coracao = transform.scale(coracao, (60,50))


mixer.music.load("musica_fundo.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1)

dor = mixer.Sound("dor_fortnite.mp3")
acerto = mixer.Sound("acertou.mp3")
regenera = mixer.Sound("regenera.mp3")
vitoria = mixer.Sound("vitoria.mp3")
derrota = mixer.Sound("derrota.mp3")
adlib = mixer.Sound("adlib.mp3")
adlib.play()
running = True
clock=time.Clock()



temas = ["animais", "comidas/bebidas", "objetos", "profissoes", "marcas famosas", "PUC", "PUC RIO"]
tema_escolhido = random.choice(temas)
vidas=6
if tema_escolhido == "animais":
    lista_palavras = ["cachorro", "gato", "elefante", "leao", "girafa", "tigre", "urso", "coelho", "macaco", "pinguim", "zebra", "hipopotamo", "rinoceronte", "cavalo", "ovelha", "vaca", "porco", "galinha", "pato", "coruja", "lobo", "raposa", "cervo", "baleia", "golfinho", "tartaruga", "crocodilo", "jacare", "camelo", "panda", "leopardo", "pantera", "canguru", "coala", "foca"]

if tema_escolhido == "comidas/bebidas":
    lista_palavras = ["arroz", "banana", "queijo", "alface", "frango", "tomate", "chocolate", "pao", "leite", "feijao", "macarrao", "sorvete", "abacaxi", "cenoura", "batata", "melancia", "cafe", "churrasco", "pizza", "hamburguer", "salada", "suco", "iogurte", "bolo", "pipoca", "sanduiche", "biscoito", "manteiga", "mel", "guarana", "cerveja", "vinho", "whisky", "vodka", "tequila", "rum", "champanhe", "energetico", "agua", "pitaya"]

if tema_escolhido == "objetos":
    lista_palavras = ["celular", "computador", "televisao", "cadeira", "mesa", "cama", "sofa", "geladeira", "fogao", "microondas", "ventilador", "arcondicionado", "impressora", "teclado", "mouse", "airpods", "relogio", "carregador", "lampada", "caneta", "caderno", "mochila", "chaveiro", "carteira", "oculos", "ferramenta", "brinquedo", "roupa"]

if tema_escolhido == "profissoes":
    lista_palavras = ["medico", "engenheiro", "professor", "advogado", "enfermeiro", "policial", "bombeiro", "piloto", "cozinheiro", "jornalista", "programador", "arquiteto", "dentista", "veterinario", "psicologo", "musico", "artista", "atleta", "cientista", "agricultor", "bicalho"]

if tema_escolhido == "marcas famosas":
    lista_palavras = ["nike", "adidas", "apple", "samsung", "cocacola", "pepsi", "mcdonalds", "starbucks", "google", "facebook", "amazon", "netflix", "disney", "honda", "toyota", "ford", "chevrolet", "bmw", "benz", "audi"]

if tema_escolhido == "PUC":
        lista_palavras = ["juiza", "joisa", "bicalho", "strogonoff", "julianofloss", "mralkmin", "dralkmin", "mrcookie", "ze", "fecundacao"]

if tema_escolhido == "PUC RIO":
    lista_palavras = ["juiza", "joisa", "bicalho", "strogonoff", "julianofloss", "mralkmin", "dralkmin", "mrcookie", "ze", "fecundacao"]
    

palavra_escolhida = random.choice(lista_palavras)
letras_acertadas = ["_"] * len(palavra_escolhida)
contador = (f"Vidas: {vidas}")

timer_erro = 0
timer = 0
timer_derrota = 0
timer_erro_chute = 0

def verificar_letra(letra):
     global vidas, timer_erro, errou_texto, letras_acertadas
     if letra in palavra_escolhida:
        acerto.play()
        for i in range(len(palavra_escolhida)):
            if palavra_escolhida[i] == letra:
                letras_acertadas[i] = letra
     else:
        dor.play()
        vidas-=1
        timer_erro = 120

def reiniciar_jogo():
    global palavra_escolhida, letras_acertadas, vidas, timer, timer_derrota, tema_escolhido
    regenera.play()
    tema_escolhido = random.choice(temas)
    if tema_escolhido == "animais":
        lista_palavras = ["cachorro", "gato", "elefante", "leao", "girafa", "tigre", "urso", "coelho", "macaco", "pinguim", "zebra", "hipopotamo", "rinoceronte", "cavalo", "ovelha", "vaca", "porco", "galinha", "pato", "coruja", "lobo", "raposa", "cervo", "baleia", "golfinho", "tartaruga", "crocodilo", "jacare", "camelo", "panda", "leopardo", "pantera", "canguru", "coala", "foca"]
    if tema_escolhido == "comidas/bebidas":
        lista_palavras = ["arroz", "banana", "queijo", "alface", "frango", "tomate", "chocolate", "pao", "leite", "feijao", "macarrao", "sorvete", "abacaxi", "cenoura", "batata", "melancia", "cafe", "churrasco", "pizza", "hamburguer", "salada", "suco", "iogurte", "bolo", "pipoca", "sanduiche", "biscoito", "manteiga", "mel", "guarana", "cerveja", "vinho", "whisky", "vodka", "tequila", "rum", "champanhe", "energetico", "agua", "pitaya"]
    if tema_escolhido == "objetos":
        lista_palavras = ["celular", "computador", "televisao", "cadeira", "mesa", "cama", "sofa", "geladeira", "fogao", "microondas", "ventilador", "arcondicionado", "impressora", "teclado", "mouse", "airpods", "relogio", "carregador", "lampada", "caneta", "caderno", "mochila", "chaveiro", "carteira", "oculos", "ferramenta", "brinquedo", "roupa"]
    if tema_escolhido == "profissoes":
        lista_palavras = ["medico", "engenheiro", "professor", "advogado", "enfermeiro", "policial", "bombeiro", "piloto", "cozinheiro", "jornalista", "programador", "arquiteto", "dentista", "veterinario", "psicologo", "musico", "artista", "atleta", "cientista", "agricultor", "bicalho"]
    if tema_escolhido == "marcas famosas":
        lista_palavras = ["nike", "adidas", "apple", "samsung", "cocacola", "pepsi", "mcdonalds", "starbucks", "google", "facebook", "amazon", "netflix", "disney", "honda", "toyota", "ford", "chevrolet", "bmw", "benz", "audi"]
    
    if tema_escolhido == "PUC":
        lista_palavras = ["juiza", "joisa", "bicalho", "strogonoff", "julianofloss", "mralkmin", "dralkmin", "mrcookie", "ze", "fecundacao"]

    if tema_escolhido == "PUC RIO":
        lista_palavras = ["juiza", "joisa", "bicalho", "strogonoff", "julianofloss", "mralkmin", "dralkmin", "mrcookie", "ze", "fecundacao"]
    
    palavra_escolhida = random.choice(lista_palavras)
    letras_acertadas = ["_"] * len(palavra_escolhida)
    vidas = 6
    timer = 0
    timer_derrota = 0


background_color = (112, 128, 144)
fonte = font.Font("fonte.ttf", 40)
chique = font.Font("fontechique.ttf", 60)
chique_pequena = font.Font("fontechique.ttf", 25)

while running:
    clock.tick(60)
    key_pressed = key.get_pressed()
    window.fill(background_color)
    mouse_x, mouse_y = mouse.get_pos()

    if timer_erro > 0:
        errou_texto = fonte.render(f"voce errou, e agora tem {vidas} vidas", True, (255,0,0))
        window.blit(errou_texto, (370,50))
        timer_erro -= 1
    
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            running = False
            sys.exit()
        
        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 235<mouse_x<296 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("q")
        
        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 309<mouse_x<369 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("w")

        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 381<mouse_x<443 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("e")

        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 454<mouse_x<517 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("r")

        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 529<mouse_x<592 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("t")

        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 600<mouse_x<664 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("y")

        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 677<mouse_x<739 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("u")

        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 748<mouse_x<811 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("i")

        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 822<mouse_x<883 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("o")

        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 895<mouse_x<960 and 551<mouse_y<586:
                if ev.button == 1:
                    verificar_letra("p")

        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 248<mouse_x<309 and 593<mouse_y<629:
                if ev.button == 1:
                    verificar_letra("a")

        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 320<mouse_x<382 and 593<mouse_y<629:
                if ev.button == 1:
                    verificar_letra("s")

        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 393<mouse_x<456 and 593<mouse_y<629:
                if ev.button == 1:
                    verificar_letra("d")
                    
        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 469<mouse_x<530 and 593<mouse_y<629:
                if ev.button == 1:
                    verificar_letra("f")

        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 541<mouse_x<604 and 593<mouse_y<629:
                if ev.button == 1:
                    verificar_letra("g")
        
        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 614<mouse_x<677 and 593<mouse_y<629:
                if ev.button == 1:
                    verificar_letra("h")
        
        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 688<mouse_x<752 and 593<mouse_y<629:
                if ev.button == 1:
                    verificar_letra("j")
        
        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 762<mouse_x<825 and 593<mouse_y<629:
                if ev.button == 1:
                    verificar_letra("k")
        
        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 836<mouse_x<896 and 593<mouse_y<629:
                if ev.button == 1:
                    verificar_letra("l")
    
        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 278<mouse_x<340 and 637<mouse_y<674:
                if ev.button == 1:
                    verificar_letra("z")
        
        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 352<mouse_x<413 and 637<mouse_y<674:
                if ev.button == 1:
                    verificar_letra("x")
    
        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 426<mouse_x<488 and 637<mouse_y<674:
                if ev.button == 1:
                    verificar_letra("c")
        
        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 499<mouse_x<560 and 637<mouse_y<674:
                if ev.button == 1:
                    verificar_letra("v")
    
        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 571<mouse_x<635 and 637<mouse_y<674:
                if ev.button == 1:
                    verificar_letra("b")

        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 645<mouse_x<708 and 637<mouse_y<674:
                if ev.button == 1:
                    verificar_letra("n")

        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 719<mouse_x<781 and 637<mouse_y<674:
                if ev.button == 1:
                    verificar_letra("m")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_q:
                verificar_letra("q")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_w:
                verificar_letra("w")
        
        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_e:
                verificar_letra("e")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_r:
                verificar_letra("r")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_t:
                verificar_letra("t")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_y:
                verificar_letra("y")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_u:
                verificar_letra("u")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_i:
                verificar_letra("i")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_o:
                verificar_letra("o")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_p:
                verificar_letra("p")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_a:
                verificar_letra("a")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_s:
                verificar_letra("s")
        
        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_d:
                verificar_letra("d")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_f:
                verificar_letra("f")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_g:
                verificar_letra("g")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_h:
                verificar_letra("h")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_j:
                verificar_letra("j")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_k:
                verificar_letra("k")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_l:
                verificar_letra("l")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_z:
                verificar_letra("z")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_x:
                verificar_letra("x")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_c:
                verificar_letra("c")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_v:
                verificar_letra("v")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_b:
                verificar_letra("b")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_n:
                verificar_letra("n")

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_m:
                verificar_letra("m")


    
        
        
        if ev.type == KEYDOWN and vidas>1:
                if ev.key == K_SPACE:
                    print("\n" + "="*30)
                    print("MODO CHUTE ATIVADO!")
                    print("DIGITE SUA RESPOSTA E PRESSIONE ENTER")
                    print("="*30)
                    chute = input("Seu chute: ").lower().strip()

                    if chute == palavra_escolhida:
                        print("ACERTOU TUDO!")
                        letras_acertadas = list(palavra_escolhida)
                    else:
                        print("ERROU O CHUTE!")
                        vidas -= 2 
                        timer_erro_chute = 300

    if timer_erro_chute > 0:
        mensagem_erro = fonte.render(f"Chute errado!", True, (255,0,0))
        perdeu_vida2 = fonte.render(f"Perdeu 2 vidas!", True, (255,0,0))
        window.blit(mensagem_erro, (900,200))
        window.blit(perdeu_vida2, (900,250))
        timer_erro_chute -= 1


    #PALAVRA ESCOLHIDA
    #palavra_text = font.render(palavra_escolhida, True, (0,0,0))
    #window.blit(palavra_text, (570,400))

    texto_exibido = " ".join(letras_acertadas)
    letras_text = chique.render(texto_exibido, True, (0,0,0))
    window.blit(letras_text, (400,200))


    window.blit(teclado_img, (50,450))
    #print(mouse_x,mouse_y)
    #print(vidas)
    
    tema = fonte.render(f"O tema e {tema_escolhido}", True, (255,255,0))
    window.blit(tema, (50,400))

    contador = fonte.render(f"Vidas: {vidas}", True, (255,0,0))
    window.blit(contador, (50,10))

    mensagem_chute = chique_pequena.render(f"use o modo chute com espaco, escreva sua resposta no terminal", True, (255,255,255))
    window.blit(mensagem_chute, (780,10))

    if vidas>5:
            window.blit(coracao, (170,145))

    if vidas>4:
        window.blit(coracao, (90,145))

    if vidas>3:
        window.blit(coracao, (10,145))
    
    if vidas > 2:
        window.blit(coracao, (170,70))

    if vidas > 1:
        window.blit(coracao, (90,70))
    
    if vidas >0:
        window.blit(coracao, (10,70))
    

   


    if "_" not in letras_acertadas and timer == 0:
        vitoria.play()
        timer = 180
    
    if timer > 0:
        vit_texto = fonte.render("Parabens, voce venceu!", True, (0,255,0))
        restart_texto = fonte.render("Agora o jogo ira reiniciar", True, (0,0,0))
        window.blit(vit_texto, (420,100))
        window.blit(restart_texto, (400,300))
        timer -= 1
    
    if timer == 1:
        reiniciar_jogo()
    
    if vidas == 0 and timer_derrota == 0:
        derrota.play()
        timer_derrota = 180

    if timer_derrota > 0:
        perdeu_texto = fonte.render("Voce perdeu, tente novamente!", True, (255,0,0))
        palavra_secreta = fonte.render(f"A palavra era: {palavra_escolhida}", True, (255,255,255))
        restart_texto = fonte.render("Agora o jogo ira reiniciar", True, (0,0,0))
        window.blit(palavra_secreta, (400,150))
        window.blit(perdeu_texto, (370,100))
        window.blit(restart_texto, (400,300))
        timer_derrota -= 1
    
    if timer_derrota == 1:
        reiniciar_jogo()



    display.update()
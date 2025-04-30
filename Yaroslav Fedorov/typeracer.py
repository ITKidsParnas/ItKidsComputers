# Example file showing a basic pygame "game loop"
import pygame
from pygame_widgets.button import Button
import pygame_widgets
import random
"""
цели:
добавить текст, изменить шрифт, меняющийся фон, текст меняет цвету зеленый и красный, измеряем время. и тд.
"""
game_stardet = False
menu_bg = False
current_bg = 0

menu_bg = False
current_bg = 0
texts = [
    "Вы работаете в ЦРУ, который отправляет вас в секретные документы в ФБР, которые отправляют вас под прикрытием в МИ-6, которые отправляют вас под прикрытием в ЦРУ, которые очень смущены тем, что вы вернулись только через две недели.",
    "Марья Ивановна достала из сумочки большой огурец, откусила кусок и сказала: Надо успокоиться! Тут медведь вырвался из наших рук, подбежал и тоже откусил кусок.",
    "К счастью, мы располагаем другой возможностью для установления контактов с животным миром - приблизить его к себе, сделать его другом своего дома или, по крайней мере, спутником."

]
def menu_bg_switch():
    global menu_bg
    if menu_bg == False:
        menu_bg = True
    else:
        menu_bg = False
def exitgame():
    global running
    running = False
def change_bg(number):
        global current_bg
        current_bg = number
def start_game():
    global menu_bg
    global game_stardet
    menu_bg = False
    game_stardet = True

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
f1 = pygame.font.Font(None, 36)
text1 = f1.render(random.choice(texts), 1, (180, 0, 0))
bg1 = pygame.image.load("пейзаж.jpg")
bg1_rescale = pygame.transform.scale(bg1,(190, 165))
bg1_rescale_fs = pygame.transform.scale(bg1,(1280, 720))
bg2 = pygame.image.load("пейзаж 8.jpg")
bg2_rescale = pygame.transform.scale(bg2,(190, 165))
bg2_rescale_fs = pygame.transform.scale(bg2,(1280, 720))
bg3 = pygame.image.load("пейзаж 5.jpg")
bg3_rescale = pygame.transform.scale(bg3,(190, 165))
bg3_rescale_fs = pygame.transform.scale(bg3,(1280, 720))
bg4 = pygame.image.load("пейзаж 4.jpg")
bg4_rescale = pygame.transform.scale(bg4,(190, 165))
bg4_rescale_fs = pygame.transform.scale(bg4,(1280, 720))
bg5 = pygame.image.load("пейзаж 3.jpg")
bg5_rescale = pygame.transform.scale(bg5,(190, 165))
bg5_rescale_fs = pygame.transform.scale(bg5,(1280, 720))
bg6 = pygame.image.load("пейзаж 2.jpg")
bg6_rescale = pygame.transform.scale(bg6,(190, 165))
bg6_rescale_fs = pygame.transform.scale(bg6,(1280, 720))



while running:

    if menu_bg == True:
        button_bbg1 = Button(screen, 500, 200, 200, 175, image=bg1_rescale, onClick= lambda: change_bg(1))
        button_bbg2 = Button(screen, 750, 200, 200, 175, image=bg6_rescale, onClick= lambda: change_bg(2))
        button_bbg3 = Button(screen, 1000, 200, 200, 175, image=bg5_rescale, onClick= lambda: change_bg(3))
        button_bbg4 = Button(screen, 500, 400, 200, 175, image=bg4_rescale, onClick= lambda: change_bg(4))
        button_bbg5 = Button(screen, 750, 400, 200, 175, image=bg3_rescale, onClick= lambda: change_bg(5))
        button_bbg6 = Button(screen, 1000, 400, 200, 175, image=bg2_rescale, onClick= lambda: change_bg(6))


    else:
        button_bbg1 = ""
        button_bbg2 = ""
        button_bbg3 = ""
        button_bbg4 = ""
        button_bbg5 = ""
        button_bbg6 = ""
    print (menu_bg)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    if current_bg ==1:
        screen.blit(bg1_rescale_fs, (0,0))
    elif current_bg ==2:
         screen.blit(bg2_rescale_fs, (0,0))
    elif current_bg ==3:
         screen.blit(bg3_rescale_fs, (0,0))
    elif current_bg ==4:
         screen.blit(bg4_rescale_fs, (0,0))
    elif current_bg ==5:
     screen.blit(bg5_rescale_fs, (0,0))
    elif current_bg ==6:
     screen.blit(bg6_rescale_fs, (0,0))

    if not game_stardet:
        button = Button(screen, 50, 100, 250, 40, text="Играть", onClick=lambda: start_game())
        button2 = Button(screen, 50, 150, 250, 40, text="Сменить фон", onClick=lambda: menu_bg_switch())
        button3 = Button(screen, 50, 200, 250, 40, text="Выход", onClick=lambda: exitgame())
    else:
        button = ""
        button2 = ""
        button3 = ""
        screen.blit(text1,(20,20))
    # RENDER YOUR GAME HERE
    pygame_widgets.update(event)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
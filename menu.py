import pygame
import time 
import play
pygame.init()
pygame.mixer.music.load("Shot.wav") # Reproducir el archivo de audio
''' 
    metodo menu 
    se encarga de mostrar el menu principal del juego
    y de llamar a los metodos de instrucciones y creditos
    y de iniciar el juego

'''

def menu():
    credi=0
    instruccion=0
    Ventana = pygame.display.set_mode((1000,700))
    pygame.display.set_caption("Menu")
    pygame.display.update()
    while True:
        for Eventos in pygame.event.get():
            if Eventos.type == pygame.QUIT:
                pygame.quit()
                quit()

            if Eventos.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()     ##obtine   la posicion del mouse
                x = mouse_pos[0]                       #guardamos en la variable x la posicion x  del mouse
                y = mouse_pos[1]                       #guardamos en la variable y la posicion y del mouse
                if Eventos.button==1:                  #condicion que no indica que oprimimos el clic izquierdo del mouse
                    x,y = Eventos.pos
                    if x>= 0 and x<= 1000 and y>= 0 and y<= 700: # verificamos que el clic este  en la ventana
                        if x > 350 and x<= 609 and y>= 242 and y<= 350: #  posicion del boton play  activamos el metodo iniciar juego del modulo play y depues que termine vuelve al menu
                            pygame.mixer.music.play()
                            play.iniciar_juego()
                            menu()
                        elif x >158 and x<= 418 and y>= 440 and y<= 550: ## posicion del boton instruciones le asignamos a la variable instruciones=1 
                            instruccion=1
                           
                        if x > 550 and x<= 810 and y>= 447 and y<= 550:  ## posicion del boton credito le asignamos a la variable credito =1
                            credi=1
                            
                        if x > 870 and x<= 950 and y>= 16 and y<= 107:  ## posicion del boton  X de la ventanta creditos y instruciones 
                            credi=0
                            instruccion=0
                                    
                 
    
        mouse_pos = pygame.mouse.get_pos()
        x = mouse_pos[0]
        y = mouse_pos[1]  
        if instruccion==1:                                 ##condicion que muestra la ventan instruciones
            ImgMenu=pygame.image.load("instruciones.png")
            Ventana.blit(ImgMenu,(0,0))
            pygame.display.update()
        elif credi==1:                                     #condicion que muestra la ventan creditos
            ImgMenu=pygame.image.load("bacreditos.png")
            Ventana.blit(ImgMenu,(0,0))
            pygame.display.update()
           
        else:   
            ## animacion de boton     
            if x>= 0 and x<= 1000 and y>= 0 and y<= 700:  # condicion que verifica el  mouse este en la ventana
                if x > 350 and x<= 609 and y>= 242 and y<= 350: ## condicion que verifica si pasamos el mouse por esas posicion de la ventana  y muestra el boton play
                    ImgMenu=pygame.image.load("play.png")           
                    Ventana.blit(ImgMenu,(330,230))
                    pygame.display.update()
                elif x >158 and x<= 418 and y>= 440 and y<= 550: ## condicion que verifica si pasamos el mouse por esas posicion de la ventana  y muestra el boton instrucciones
                    ImgMenu=pygame.image.load("bbinstrucciones.png")
                    Ventana.blit(ImgMenu,(140,425))
                    pygame.display.update()
                elif x > 550 and x<= 810 and y>= 447 and y<= 550:## condicion que verifica si pasamos el mouse por esas posicion de la ventana  y muestra el boton  creditos 
                    ImgMenu=pygame.image.load("creditos.png")
                    Ventana.blit(ImgMenu,(535,430))
                    pygame.display.update()
                else:
                    ImgMenu=pygame.image.load("MENU principal.png") ### mostramos la ventana pricipal en el caso que no estemos sobre ninguno de los botones 
                    Ventana.blit(ImgMenu,(0,0))
                    pygame.display.update()
    
        
#-------------------------------------------------------
menu()
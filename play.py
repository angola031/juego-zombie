
'''
modulo que inicia el juego   tenemos varias clase de objeto que son creadas para  la funcionalidad del juego :soldado,boss, zombie, zombie, balas, recarga(municion), botiquin
'''
import pygame
import time
from threading import Thread
import gc
from pygame.sprite import  Group
import imagen
import threading
def iniciar_juego():
    pygame.init()
    ### SONIDOS DE NUESTROS JUEGO
    disparo=pygame.mixer.Sound("disparo.mp3")
    sonido_fondo= pygame.mixer.Sound("fondo.mp3")
    golpe= pygame.mixer.Sound("doble golpe.mp3")
    
    
    ### COLORES UTILIZADOS EN EL JUEGO
    blanco=(255,255,255)
    fuente = pygame.font.Font(None, 50) ## fuente utilizada para mostrar texto en  la pantalla
    grupo_objeto=pygame.sprite.Group() ## GRUPO DE ESPRIA PRINCIPAL MOSTRAMOS LA ACTUALIZACION DE CADA OBJETO DENTRO DE ESTE GRUPO
    grupo_zombie=pygame.sprite.Group()### GRUPO DE OBTIENE TODO LOS OBJETO ZOMBIE
    lista_balas=pygame.sprite.Group()## GRUPO DE OBJETO QUE OBTIENE TODAS LAS BALAS DISPARADAS
    lista_botiquin=pygame.sprite.Group()## GRUPO DE OBJETO QUE OBTIENE TODOS LOS BOTIQUINES 
    lista_recarga=pygame.sprite.Group()## GRUPO DE OBJETO QUE OBTIENE TODO LAS MUNICIONES 
   
    ancho = 40  ## VARIABLE UTIL PARA NO SACAR EL SOLDADO DEL MAPA
    velocidad = 7  ## CONTROLA LA VELOCIDAD DEL JUGADOR
    
    ANCHO, ALTO = 1000, 700 ## dimesiones de la ventana
    # Crea una superficie de pantalla
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO))## TAMAÑO DE LA VENTANA
  
    ###IMAGENES UTILIZADA EN EL JUEGO
    fondo = pygame.image.load("background.png").convert()   # CONVERT MEJORA EL PROCESAMIENTO DE IMAGENES
    reanudar=pygame.image.load("reanudar.png")
    instruciones=pygame.image.load("instruciones.png")
    ganastes=pygame.image.load("ganaste.png")
    perdistes=pygame.image.load("perdiste.png")
    breintentar=pygame.image.load("reintentar.png")
    bsalir=pygame.image.load("salir.png")
    b_instruciones=pygame.image.load("binstruciones.png")

        
    #SONIDO DEL FONDO 
    sonido_fondo.play()
    # Define la clase Soldado
    '''la clase soldado es el objeto soldado las variable del objeto son:
    variables que recibe el objeto
    x , y : la posicion del soldado
    ancho , alto : el tamaño del soldado 
    velocidad : la velocidad del soldado
    salud : la salud del soldado
    -----
    variables que se crean en el objeto
    corrie_dispara_izquierda : variable que controla la imagen de correr y disparar a la izquierda
    corrie_dispara_derecha : variable que controla la imagen de correr y disparar a la derecha
    gancho : variable booleana activa movimiento de la imagen de mover el arma hacia arriba
    balas : cantidad de balas que tiene el soldado
    cuentaPasos : contador de pasos para la animacion de caminar
    mov_disparo : contador de pasos para la animacion de disparar
    score : contador de puntos 
    muert : contador de muertes para la animacion de muerte  
    izquierda : variable booleana que controla la imagen de correr a la izquierda 
    derecha : variable booleana que controla la imagen de correr a la derecha
    mov_x: movimiento del ecenario sobre el eje x
    disparar : variable que controla la imagen de disparar
    c_gancho : contador de pasos para la animacion de mover el arma hacia arriba
    rect : variable  obtine un objeto rectangulo con las posicion inicial del soldado y su tamaño
    -------------------------
    metodos
    movimientos : controla la animacion del soldado movimiento izquierda, derecha, dispara estatico, gancho  dependiendo de las variable (izquierda, derecha, gancho, disparar,soldadado quieto) si se encuetra en True   
    muerte : controla la animacion de muerte
    disparar_coriendo_derecha : controla la animacion de disparar hacia la derecha
    disparar_coriendo_izquierda : controla la animacion de disparar hacia la izquierda
    barra_salud : muestra la palabra score en la pantalla y el puntaje obtenido, la cantidad de bala, imagen de las municiones  y la barra de salud dependiendo de la variable de salud se muestra la bara de salud con sus diferentes rangos
    update: actualiza los estado que son dados por el jugador,tenenos condicion muerte que me activa la animacion muerte,corrie_dispara_derecha activa animicion de disparo con movimieno izquierda,
    corrie_dispara_izquierda   codicion que activa el movimiento corriendo hacia la izquierda disparando y si no entra por alguno de esto condiciones activa el  metodo movimiento
    activa el metodo de la barra de salud y el deplazamiento del objeto  rectangulo

    '''
    class Soldado(pygame.sprite.Sprite):
        def __init__(self,  x, y, ancho, alto, velocidad, salud) -> None:
            super().__init__()
            self.x = x
            self.y = y
            self.corrie_dispara_izquierda=False
            self.corrie_dispara_derecha=False
            self.ancho = ancho
            self.gancho=False
            self.alto = alto
            self.balas=200
            self.velocidad = velocidad
            self.salud = salud
            self.cuentaPasos=0
            self.mov_x=0
            self.mov_disparo=0
            self.score=0
            self.muert=0
            self.izquierda=False
            self.derecha=False
            self.disparar=False
            self.c_gancho=0
            self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
            
            
        def movimientos(self):
        # Contador de pasos
            if self.cuentaPasos + 1 >= 8:
                self.cuentaPasos = 0
            if self.mov_disparo + 1 >= 4:
                self.mov_disparo = 0
            if self.c_gancho + 1 >= 4:
                self.c_gancho = 0
            # Movimiento de immagen a la izquierda
            if self.izquierda:
                PANTALLA.blit(imagen.personaje_caminado_izquierda[self.cuentaPasos // 1], (int(self.x), int(self.y)))
                self.cuentaPasos += 1
            elif self.gancho:
                PANTALLA.blit(imagen.personaje_gancho_derecha[self.c_gancho // 1], (int(self.x), int(self.y)))
                self.c_gancho+=1
                # Movimiento imagen a la derecha
            elif self.derecha:
                PANTALLA.blit(imagen.personaje_caminando_derecha[self.cuentaPasos // 1], (int(self.x), int(self.y)))
                self.cuentaPasos += 1
            #MOVIMIENTO IMAGEN DE DISPARAR
            elif self.disparar:
                PANTALLA.blit(imagen.personaje_disparar_derecha[self.mov_disparo // 1], (int(self.x), int(self.y)))
                self.mov_disparo+=1
            else:
                PANTALLA.blit(imagen.personaje_quieto,(int(self.x), int(self.y)))
        ##
        def muerte(self):
            if self.muert + 1 >= 4:
                self.muert = 0
            PANTALLA.blit(imagen.personaje_muerte_derecha[self.muert // 1], (int(self.x), int(self.y)))
            self.muert+=1
        def dispar_coriendo_derecha(self):
            if self.cuentaPasos + 1 >= 8:
                self.cuentaPasos = 0
            PANTALLA.blit(imagen.personaje_corriendo_atac_derecha[self.cuentaPasos // 1], (int(self.x), int(self.y)))
            self.cuentaPasos += 1
        def dispar_coriendo_izquierda(self):
            if self.cuentaPasos + 1 >= 8:
                self.cuentaPasos = 0
            PANTALLA.blit(imagen.personaje_corriendo_atac_izquierda[self.cuentaPasos // 1], (int(self.x), int(self.y)))
            self.cuentaPasos += 1
        ##metodo de salud del soldao    
        def barra_salud(self):
            PANTALLA.blit( fuente.render("Score", True, blanco),(250,5))
            PANTALLA.blit( fuente.render(str(self.score), True, blanco),(355,5))
            c_bala = fuente.render(str(self.balas), True, blanco)
            PANTALLA.blit(c_bala,(490,5))
            PANTALLA.blit(imagen.recargari,(450,5))
            if self.salud>=0:
                if self.salud>90:
                    PANTALLA.blit(imagen.vida[0],(0,0))
                elif self.salud>80 and self.salud<=90:
                    PANTALLA.blit(imagen.vida[1],(0,0))
                elif self.salud>70 and self.salud<=80:
                    PANTALLA.blit(imagen.vida[2],(0,0))
                elif self.salud>60 and self.salud<=70: 
                    PANTALLA.blit(imagen.vida[3],(0,0))
                elif self.salud>50 and self.salud<=60:
                    PANTALLA.blit(imagen.vida[4],(0,0))
                elif self.salud>40 and self.salud<=50:
                    PANTALLA.blit(imagen.vida[5],(0,0))
                elif self.salud>30 and self.salud<=40:
                    PANTALLA.blit(imagen.vida[6],(0,0))
                elif self.salud>20 and self.salud<=30:
                    PANTALLA.blit(imagen.vida[7],(0,0))
                elif self.salud>10 and self.salud<=20:
                    PANTALLA.blit(imagen.vida[8],(0,0))
                elif self.salud>0 and self.salud<=10:
                    PANTALLA.blit(imagen.vida[9],(0,0))
                else:
                    PANTALLA.blit(imagen.vida[10],(0,0))
                    
        def update(self):
            if self.salud <=0:
                self.muerte()
            elif self.corrie_dispara_derecha:
                self.dispar_coriendo_derecha()
            elif  self.corrie_dispara_izquierda:
                self.dispar_coriendo_izquierda()
            else:
                self.movimientos()
            self.barra_salud()
            self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
            #pygame.draw.rect(PANTALLA, (255, 0, 0), (self.x,self.y,self.ancho,self.alto), 2)
    '''
    creamos la clase boss que contiene nuestro objeto boos con sus metodos
    variables del objeto:
    x,y: la posicion del boss
    ancho,alto: tamaño del jefe
    muerte_boss: contador de pasos para la  animacion de muerte 
    ataq: contador de paso para la animacion de ataque
    derecha: contador de pasos para la animacion de movimiento
    muert: variable booleana para saber si el boss esta muerto
    a: variable booleana para saber si el boss esta atacando
    soldado : obtiene el objeto soldado para poder saber la posicion de soldado 
    mv_derecha: variable booleana para saber si el boss se mueve a la derecha
    mv_izquierda: variable booleana para saber si el boss se mueve a la izquierda
    salud: variable para la salud del boss
    alejarce: variable booleana para saber si el boss se aleja
    activar_saltos: variable booleana para saber si el boss esta saltando
    salt_alejarce: variable booleana para saber si el boss esta saltando para alejarse
    salt_acercarce: variable booleana para saber si el boss esta saltando para acercarse
    tiempo_a: variable para el tiempo de ataque del boss
    activ_atacar: variable booleana para saber si el boss esta atacando
    animation_muerte: variable para la animacion de muerte del boss
    image: variable para crear superficie rectangulo
    rect: variable para crear rectangulo
    velocidad:velocidad del boss
    cuenta_Paso: contador de pasos para movimiento del boss camina izquierda,salto izquierda,derecha
    ----------------------
    metodos:
    caminar_izquierda: metodo para animacion del movimiento del boss caminar izquierda
    caminar_derecha: metodo para animacion del movimiento del boss caminar derecha
    muerte: metodo para animacion del movimiento del boss muerte
    ataque_izquierda:metodo para animacion movimiento ataque por izquierda boss
    ataque_derecha: metodo para animacion movimiento de ataque por derecha boss
    movi_salto_izquierda: metodo para animacion del movimiento del boss salto izquierda
    movi_salto_derecha: metodo para animacion del movimiento del boss salto derecha
    barra_salud: muestra la barra de salud del boss depediendo del rango que tiene la variable salud
    
    seguir objetivo: metodo hace es ir hacia el objeto soldado  dependiendo de la posicion en la que este si la posicion en el eje x  es mayor comienza a restarle la posicion en x con el valor de velocidad del bos
    si el  la posicion en x es menor comienza a aumentarle cuando llega a la posicion del soldado se pone en True  o False  las variables mv_derecha y mv_izquierda,
    si la variable mv_derecha es True comienza a llamar al metodo caminar_derecha y si la variable mv_izquierda es True comienza a llamar al metodo caminar_izquierda

    alejarce: el metodo alejarce tiene condiciones si la posicion x del boss es mayor comienza a aumentar la posicion en x para alejarce hasta una distancia de 700 px la variable mov_derecha =True activar animacion moverse ala dereceh
    si la posicion x del boss es menor comienza a disminuir la posicion en x para alejarce hasta una distancia de -700 px  la variable mov_izquierda =True activar animacion moverse ala izquierda
    tenemos una variable distancia que va obtener un valor absoluto positivo para saber la distaci siempre nos de 700 px positivo
    cuando la distacia sea 700  la variable alejarce = False activa la fucion acercarce, la variable salt_acercace=True esta variable es funcional cuando esta activado activa_saltos 

    tiempo_espera_muerte= metodo hace una espera 0.35 segundo para poder tene la animacion de muerte y activar la variable muert:True
    
    tiempo_espera: metodo desactiva el salto acercarce  salt_acercace=False y activa tiempo_a=True con esta variable controlamos que solo una vez se active el desactivar el ataque

    update: actualiza el los estado del boos con una condiciones implicadad:
    si la variable muert es True muestra la imagen del boss en el suelo
    si la variable activar_saltos es True llama los metodos de saltar izquierda o derecha dependiendo de la varible mv_derecha controla si es para la derecha o es para la iquierda el moviemiento
    si la variable alejarce es True  dependiendo de la variable mv_derecha activa al metodo  de animacion izquierda o caminar derecha 
    si la variable activ_atacar es True dependiendo de la variable mv_derecha  activa animacion de ataque izquieda o derecha, 
    creamos una variable timer que obtiene un nuevo hilo del sistema operactibo para poder tener un tiempo de espera de la animacion de ataque y no se para la animacion, depues de tener su timpo de espera activamos la funcion de alejerce:True
    si la variable animation_muerte es True activa la animacion de muerte, 
    creamos una variable timer esta variable obtiene un nuevo hilo del sistema llamando la funcion tiempo de espera_muerte dandole una espera a la animacion para activar la variable muert=True
    en el caso que no se active ninguna de estas funciones se activa el metodo de seguir objetivo dependiendo de la variable mv_derecha para activar animimacion si es izquiedad o derecha
    llama el metodo de la barra de salud del boss y actualiza la posicion del objeto rect  del bos

    '''
    #DEEFINE EL OBJETO JEFE FINAL     
    class boss(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()	
                self.x=0
                self.y=0
                self.ancho=40
                self.alto=110
                self.muerte_boss=0
                self.ataq=0
                self.derecha=0
                self.muert=False
                self.a=0
                self.mv_derecha=False
                self.mv_izquierda=False
                self.salud=300
                self.alejarce=False
                self.activar_saltos=False
                self.salt_alejarce=False
                self.salt_acercarce=True
                self.tiempo_a=0
                self.activ_atacar=False
                self.animation_muerte=0
                self.image = pygame.Surface((20, 10))  # Crea una superficie para la imagen 
                self.image.fill((255, 0, 0))  # Rellena la superficie con un color (en este caso, rojo)
                self.rect = self.image.get_rect() 
                self.rect = pygame.Rect(self.rect.x, self.rect.y, self.ancho, self.alto)
                self.velocidad = 15
                self.cuentaPasos=0
        ## Movimiento a la izquierda
        def caminar_izquierda(self):
            # Contador de pasos
            if self.cuentaPasos + 1 >= 6:
                self.cuentaPasos = 0
            #PASA POR LA LISTA Y VA CAMBIANDO LA IMAGEN UNA POR UNA CREANDO UN MOVIMIENTO
            if True:
                PANTALLA.blit(imagen.boss_caminar_izquierda[self.cuentaPasos // 1], (int(self.rect.x-320), int(self.rect.y-350)))
                self.cuentaPasos += 1
        ##MOVIMIENTO DE MUERTE 
        def muerte(self):
            if self.muerte_boss + 1 >= 9:
                self.muerte_boss = 0
            PANTALLA.blit(imagen.boss_muerte_izquierda[self.muerte_boss // 1], (int(self.rect.x-320), int(self.rect.y-250)))
            self.muerte_boss+=1
        ##MOVIMIENTO DE ATAQUE ALA IZQUIERDA
        def ataque_izquierda(self):
            if self.ataq + 1 >= 9:
                self.ataq=0
            PANTALLA.blit(imagen.boss_atacar_izquierda[self.ataq // 1], (int(self.rect.x-150), int(self.rect.y-350)))
            self.ataq+=1
        ##MOVIMIENTO DE ATAQUE ALA DERECHA
        def ataque_derecha(self):
            if self.ataq + 1 >= 9:
                self.ataq=0
            PANTALLA.blit(imagen.boss_atacar_derecha[self.ataq // 1], (int(self.rect.x-400), int(self.rect.y-350)))
            self.ataq+=1
        ##MOVIMIENTO DE CAMINAR ALA DERECHA
        def caminar_derecha(self):
            if self.derecha + 1 >= 9:
                self.derecha = 0
            PANTALLA.blit(imagen.boss_caminar_derecha[self.derecha // 1], (int(self.rect.x-320), int(self.rect.y-350)))
            self.derecha+=1
        ##MOVIMIENTO DE SALTO A LA DERECHA
        def movi_saltos_derecha(self):          
            if self.cuentaPasos + 1 >= 9:
                self.cuentaPasos=0
            PANTALLA.blit(imagen.boss_salto_derecha[self.cuentaPasos // 1], (int(self.rect.x-280), int(self.rect.y-350)))
            self.cuentaPasos += 1
        ##MOVIMIENTO DE SALTO A LA IZQUIERDA
        def movi_saltos_izquierda(self):
            if self.cuentaPasos + 1 >= 9:
                self.cuentaPasos=0
            PANTALLA.blit(imagen.boss_salto_izquierda[self.cuentaPasos // 1], (int(self.rect.x-400), int(self.rect.y-350)))
            self.cuentaPasos += 1
        ## METODO QUE MUESTRA LA SALUDA DEL JEFE DEPEDIENDO DE LA VARIABLE SALUD
        def barra_salud(self):
            if self.salud>=0:
                if self.salud>270:
                    PANTALLA.blit(imagen.bos_vida[0],(750,0))
                elif self.salud>240 and self.salud<=270:
                    PANTALLA.blit(imagen.bos_vida[1],(750,0))
                elif self.salud>210 and self.salud<=240:
                    PANTALLA.blit(imagen.bos_vida[2],(750,0))
                elif self.salud>180 and self.salud<=210: 
                    PANTALLA.blit(imagen.bos_vida[3],(750,0))
                elif self.salud>150 and self.salud<=180:
                    PANTALLA.blit(imagen.bos_vida[4],(750,0))
                elif self.salud>120 and self.salud<=150:
                    PANTALLA.blit(imagen.bos_vida[5],(750,0))
                elif self.salud>90 and self.salud<=120:
                    PANTALLA.blit(imagen.bos_vida[6],(750,0))
                elif self.salud>60 and self.salud<=90:
                    PANTALLA.blit(imagen.bos_vida[7],(750,0))
                elif self.salud>30 and self.salud<=60:
                    PANTALLA.blit(imagen.bos_vida[8],(750,0))
                elif self.salud>1 and self.salud<=30:
                    PANTALLA.blit(imagen.bos_vida[9],(750,0))
                else:
                    PANTALLA.blit(imagen.bos_vida[10],(750,0))
        ## METODO QUE PERSIGUE EL OBJETO SOLDADO  DEPENDIENDO LA POSICION
        def seguir_objetivo(self):
            if self.rect.x < self.soldado.rect.x:
                if self.rect.x+self.velocidad>=self.soldado.rect.x:
                    self.rect.x=self.soldado.rect.x-39
                else:
                    self.rect.x += self.velocidad
                self.mv_derecha=True
                self.mv_izquierda=False
            elif self.rect.x > self.soldado.rect.x:
                if self.rect.x-self.velocidad<=self.soldado.rect.x:
                    self.rect.x=self.soldado.rect.x+39
                else:
                    self.rect.x -= self.velocidad
                self.mv_izquierda=True
                self.mv_derecha=False
            if self.rect.y<self.soldado.rect.y:
                self.rect.y+=self.velocidad
            elif self.rect.y>self.soldado.rect.y:
                self.rect.y-=self.velocidad
        ## METODO QUE ALEJA AL JEFE DESPUES DE AVERLO ATACADO
        def alejarse_objetivo(self):
            if self.rect.x > self.soldado.rect.x:
                self.rect.x += self.velocidad
                self.mv_derecha=True
                self.mv_izquierda=False
            elif self.rect.x < self.soldado.rect.x:
                self.rect.x -= self.velocidad
                self.mv_derecha=False
                self.mv_izquierda=True
            distancia=abs(self.rect.x-self.soldado.rect.x)
            if distancia>=700:
                self.alejarce=False
                self.salt_acercarce=True    
        ## METODO QUE DA UN LAPSO DE TIEMPO PARA PODER MOSTRA LA ANIMACION DE MUERTE DEL JEFE     
        def tiempo_espera_muerte(self):
            time.sleep(0.35)
            self.muert=True
            self.animation_muerte=False
        ## METODO QUE DA UN LAPSO DE TIEMPO PARA PODER MOSTRA LA ANIMACION DE ATAQUE DEL JEFE
        def tiempo_espera(self):
            self.salt_acercarce=False
            self.tiempo_a=True
        ## METODO QUE ACTUALIZA LOS MOVIMIENTO DEL JEFE Y LOS MUESTRA EN LA PANTALLA   
        def update(self):
            #CONDICION  QUE MUESTRA LA IMAGEN  CUANDO EL JEFE ESTA MUERTO
            if self.salud<=0 and self.muert:
                PANTALLA.blit(pygame.image.load("boss/muerte/muerte10_izquierda.png"),(self.rect.x-320,self.rect.y-250))
            ##CONDICION QUE ACTIVA LOS METODOS DE MOVIMIENTO DE SALTO DEL JEFE
            elif self.activar_saltos:
                if self.salt_acercarce:
                    if  self.mv_derecha:
                        self.movi_saltos_derecha()
                    else:
                        self.movi_saltos_izquierda()
                    self.seguir_objetivo()
                else:
                    if  self.mv_derecha:
                        self.movi_saltos_derecha()
                    else:
                        self.movi_saltos_izquierda()
                    self.alejarse_objetivo()
             ##CONDICION QUE ACTIVA LOS MOVIMIENTO DE ALEJAR JEFE          
            elif self.alejarce:
                if self.mv_derecha:
                    self.caminar_derecha()
                else:
                    self.caminar_izquierda()
                self.alejarse_objetivo()
            ##CONDICION QUE ACTIVA LOS MOVIMIENTO DE ATAQUE DEL JEFE   
            elif self.activ_atacar:
                if self.mv_izquierda:   
                    self.ataque_izquierda()
                else:
                    self.ataque_derecha()
                
                if self.a==0:
                    timer = threading.Timer(1, self.tiempo_espera)
                    timer.start()
                    self.a=1
                if self.tiempo_a:
                    self.activ_atacar=False
                    self.alejarce=True
                    self.tiempo_a=False
            ##CONDICION QUE ACTIVA LA ANIMACION DE MUERTE DEL JEFE        
            elif self.animation_muerte:
                self.muerte()
                hilo= Thread(target=self.tiempo_espera_muerte)  ## UTILIZO UN HILO ADICIONAL PARA PODER DARLE LA ESPERA ALA ANIMACION
                hilo.start()
                hilo.join()
            else:
                if self.mv_izquierda:
                    self.caminar_izquierda()
                else:
                    self.caminar_derecha()
                self.seguir_objetivo()
                self.tiempo_a=False
            self.barra_salud()
            self.rect = pygame.Rect(self.rect.x, self.rect.y, self.ancho, self.alto)
            #pygame.draw.rect(self.superficie, (255, 0, 0), (self.rect.x,self.rect.y,self.ancho,self.alto), 2)
    
    '''
    creamos la clase zombi que contiene el objeto zombie con sus metodos es igua para el objeto zombie2
    variables:
    x: posicion en x del zombie
    y: posicion en y del zombie
    ancho: ancho del zombie
    alto: alto del zombie
    salud: vida del zombie
    soldado: objeto soldado
    atacar: variable que activa el ataque del zombie
    activ_atacar: variable que activa el ataque del zombie
    muerte_zomvi: variable que activa la animacion de muerte del zombie
    animacion_muerte: variable que activa la animacion de muerte del zombie
    image: imagen del zombie
    rect: rectangulo del zombie
    superficie: superficie del zombie
    --------------------
    metodos:
    movimientos: metodo que activa la animacion caminando hacia la izquierada
    muerte: metodo que activa la animacion muerte
    ataca: metodo que activa  la animacion de ataque 
    seguir_objetivo: metodo que deplaza el objeto zombie sobre la posicion del soldado 
    tiempo_espera: metodo que queda un tiempo de expera para cargar la animacion de muerte
    update: actualiza los movimientos del zombie
    si activ_atacar=True activa el metodo actacar
    si animacion_muerte=True activa el metodo muerte
    si activ_atacar=False y animacion_muerte=False activa el metodo movimientos
    
    '''
## OBJETO ZOMBIE
    class zombie(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()	
                self.x=0
                self.y=0
                self.ancho=100
                self.alto=170
                self.salud=2
                self.soldado=0
                self.atacar=0
                self.activ_atacar=False
                self.muerte_zomvi=0
                self.animacion_muerte=0
                self.image = pygame.Surface((20, 10))  # Crea una superficie para la imagen de la bala láser
                self.image.fill((255, 0, 0))  # Rellena la superficie con un color (en este caso, rojo)
                self.rect = self.image.get_rect()  # O
                self.superficie=PANTALLA
                self.rect = pygame.Rect(self.rect.x, self.rect.y, self.ancho, self.alto)
                self.velocidad = 5
                self.cuentaPasos=0
        ## ANIMACION DEL MOVIMIENTO DEL ZOMBIE  QUE CAMNA HACIA LA IZQUIERDA
        def movimientos(self):
            # Contador de pasos
            if self.cuentaPasos + 1 >= 6:
                self.cuentaPasos = 0
            # Movimiento a la izquierda
            if True:
                PANTALLA.blit(imagen.zombie1_caminar_izquierda[self.cuentaPasos // 1], (int(self.rect.x), int(self.rect.y)))
                self.cuentaPasos += 1
        ##ANIMACION DE MUERTE DEL ZOMBIEN 
        def muerte(self):
            if self.muerte_zomvi + 1 >= 15:
                self.muerte_zomvi = 0
            PANTALLA.blit(imagen.zombie1_muerte_izquierda[self.muerte_zomvi // 1], (int(self.rect.x), int(self.rect.y)))
            self.muerte_zomvi+=1
        ##ANIMACION DE ATAQUE DEL ZOMBIE
        def ataca(self):
            if self.atacar +1>=4:
                self.atacar=0
            PANTALLA.blit(imagen.zombie1_atacar_izquierda[self.atacar // 1], (int(self.rect.x), int(self.rect.y)))
            self.atacar+=1
        ##METODO QUE PERMITE AL ZOMBIE SEGUIR AL OBJETIVO
        def seguir_objetivo(self):
            if self.rect.x < self.soldado.rect.x:
                self.rect.x += self.velocidad
            elif self.rect.centerx > self.soldado.rect.x:
                self.rect.x -= self.velocidad
            if self.rect.y<self.soldado.rect.y:
                self.rect.y+=self.velocidad
            elif self.rect.y>self.soldado.rect.y:
                self.rect.y-=self.velocidad
        ##METODO QUE PERMITE AL ZOMBIE TENER LA ANIMACION DE MUERTE
        def tiempo_espera(self):
            time.sleep(0.35)
          ## METODO QUE ACTUALIZA LOS MOVIMIENTO DEL ZOMBIE Y LOS MUESTRA EN LA PANTALLA  
        def update(self):
            ##CONDICIONAL QUE ACTIVA EL METODO ATACAR DEL ZOMBIE
            if self.activ_atacar:
                self.ataca()
                if self.rect.colliderect(self.soldado.rect):
                    pass
                else:
                    self.activ_atacar=False
            ##CONDICIONAL QUE ACTIVA LA MUERTE DEL ZOMBIE
            elif self.animacion_muerte:
                self.muerte()
                hilo= Thread(target=self.tiempo_espera)
                hilo.start()  
            else:
                self.movimientos()
                self.seguir_objetivo()
            
            self.rect = pygame.Rect(self.rect.x, self.rect.y, self.ancho, self.alto)
            #pygame.draw.rect(self.superficie, (255, 0, 0), (self.rect.x,self.rect.y,self.ancho,self.alto), 2)
    class zombie2(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()	
                self.x=0
                self.y=0
                self.ancho=100
                self.alto=170
                self.soldado=0
                self.atacar=0
                self.salud=2
                self.activ_atacar=False
                self.muerte_zomvi=0
                self.animacion_muerte=0
                self.image = pygame.Surface((20, 10))  # Crea una superficie para la imagen de la bala láser
                self.image.fill((255, 0, 0))  # Rellena la superficie con un color (en este caso, rojo)
                self.rect = self.image.get_rect()  # O
                self.superficie=PANTALLA
                self.rect = pygame.Rect(self.rect.x, self.rect.y, self.ancho, self.alto)
                self.velocidad = 5
                self.cuentaPasos=0
        ## ANIMACION DEL MOVIMIENTO DEL ZOMBIE  QUE CAMNA HACIA LA IZQUIERDA
        def movimientos(self):
            # Contador de pasos
            if self.cuentaPasos + 1 >= 6:
                self.cuentaPasos = 0
            # Movimiento a la izquierda
            if True:
                PANTALLA.blit(imagen.zombie2_caminar_izquierda[self.cuentaPasos // 1], (int(self.rect.x), int(self.rect.y)))
                self.cuentaPasos += 1
        ##ANIMACION DE MUERTE DEL ZOMBIE
        def muerte(self):
            if self.muerte_zomvi + 1 >= 15:
                self.muerte_zomvi = 0
            PANTALLA.blit(imagen.zombie2_muerte_izquierda[self.muerte_zomvi // 1], (int(self.rect.x), int(self.rect.y)))
            self.muerte_zomvi+=1
        ##ANIMACION DE ATAQUE DEL ZOMBIE
        def ataca(self):
            if self.atacar +1>=4:
                self.atacar=0
            PANTALLA.blit(imagen.zombie2_atacar_izquierda[self.atacar // 1], (int(self.rect.x), int(self.rect.y)))
            self.atacar+=1
            ##METODO QUE PERMITE AL ZOMBIE TENER LA ANIMACION DE MUERTE
        def tiempo_espera(self):
            time.sleep(0.35)
        # el objeto  sigue al soldado
        def seguir_objetivo(self):
            if self.rect.x < self.soldado.rect.x:
                self.rect.x += self.velocidad
            elif self.rect.centerx > self.soldado.rect.x:
                self.rect.x -= self.velocidad
            if self.rect.y<self.soldado.rect.y:
                self.rect.y+=self.velocidad
            elif self.rect.y>self.soldado.rect.y:
                self.rect.y-=self.velocidad
        # actualiza  movimiento del zombie 
        def update(self):
            #CONDICION QUE ACTIVA EL ATAQUE DEL ZOMBIE
            if self.activ_atacar:
                self.ataca()
                if self.rect.colliderect(self.soldado.rect):
                    pass
                else:
                    self.activ_atacar=False
            #CONDICION QUE ACTIVA LA MUERTE DEL ZOMBIE
            elif self.animacion_muerte:
                self.muerte()
                hilo= Thread(target=self.tiempo_espera)
                hilo.start()  
            else:
                self.movimientos()
                self.seguir_objetivo()
            
            self.rect = pygame.Rect(self.rect.x, self.rect.y, self.ancho, self.alto)
            #pygame.draw.rect(self.superficie, (255, 0, 0), (self.rect.x,self.rect.y,self.ancho,self.alto), 2)
    
    '''
    clase que crea las balas del proyectil del soldado
    variable:
    x: posicion en x del proyectil
    y: posicion en y del proyectil
    derecha: variable que indica si el proyectil se mueve hacia la derecha
    izquierda: variable que indica si el proyectil se mueve hacia la izquierda
    image: imagen del proyectil
    rect: rectangulo del proyectil
    metodos:
    upadate:
    si derecha=True el movimiento de proyectil es hacia la derecha
    si izquierda=True el movimiento de proyectil es hacia la izquierda
    si no es ninguna de las dos el proyectil se mueva hacia la derecha
    '''
      ##objeto del proyectil del soldado
    class balas(pygame.sprite.Sprite):
        def __init__(self) :
            super().__init__()
            self.x=0
            self.y=0
            n=0
            self.derecha=False
            self.izquierda=False
            self.image = pygame.Surface((10, 7))  # Crea una superficie para la imagen de la bala láser
            self.image.fill((255, 255, 0))  # Rellena la superficie con un color (en este caso, rojo)
            self.rect = self.image.get_rect()  # Obtiene el rectángulo que representa la imagen
            self.rect.midleft = (self.x, self.y)  # Coloca el centro de la imagen en la posición (x, y)
        ## metodo que actuliza el movimiento del proyectil
        def update(self):
            ## movimiento del proyectil izquierda y derecha
            if self.derecha:
                self.rect.x += 7
            elif self.izquierda:
                self.rect.x -= 7
            else:
                self.rect.x += 7
    ##objeto    botiquin recupera vida
    '''
    clase que crea el botiquin que recupera vida al soldado
    variable:
    x: posicion en x del botiquin
    y: posicion en y del botiquin
    vida: cantidad de vida que recupera el botiquin
    tiempo: tiempo que se muestra en pantalla el botiquin
    image: imagen del botiquin
    rect: rectangulo del botiquin
    metodos:
    mostrar:
    si el tiempo es mayor a 150 se muestra el botiquin y aumenta la vida del soldado en 50
    si no es mayor a 150 y mayor a 50  se muestra el botiquin un poco transparente  y aumenta la vida del soldado en 30
    si no es mayor a 50 y mayor a 0  se muestra el botiquin un poco mas transparente  y aumenta la vida del soldado en 10
    update:
    disminuye el tiempo, activa el metodo mostrar 
    '''
    class  botiquin(pygame.sprite.Sprite): 
        def __init__(self) :
            super().__init__()
            self.x=0
            self.y=0
            self.vida=0
            self.tiempo=0
            self.image = pygame.Surface((60, 50))  # Crea una superficie para la imagen del botiquib
            self.rect = self.image.get_rect()  # Obtiene el rectángulo que representa la imagen
            self.rect.midleft = (self.x, self.y)  # Coloca el centro de la imagen en la posición (x, y)
        ## METODO QUE MUESTRA EN LA PANTALLA EL BOTIQUIN PERO EN UN TIEMPO  PROLONGADO
        def mostrar(self):
            if self.tiempo>150:
                PANTALLA.blit(imagen.botiquin[0],(self.x,self.y))
                self.vida=50
            elif self.tiempo<=50 and self.tiempo<=150:
                PANTALLA.blit(imagen.botiquin[1],(self.x,self.y))
                self.vida=30
            else:
                PANTALLA.blit(imagen.botiquin[2],(self.x,self.y))
                self.vida=10
        ## METODO QUE ACTUALIZA EL TIEMPO DE VIDA DEL BOTIQUIN Y LO MUESTRA
        def update(self):
            self.tiempo-=1
            self.mostrar()
            self.rect = pygame.Rect(self.x, self.y, 60, 50)
            #pygame.draw.rect(PANTALLA, (255, 0, 0), (self.x,self.y,60,50), 2)
    '''
    clase que crea la recarga de municion del soldado
    variable:
    x: posicion en x de la recarga
    y: posicion en y de la recarga
    recarga: cantidad de municion que recupera la recarga
    tiempo: tiempo que puede mostrarse en pantalla la municion
    image: imagen de la recarga
    rect: rectangulo de la recarga
    metodos:
    mostrar:
    si el tiempo es mayor a 150 se muestra la recarga y aumenta la municion del soldado en 50
    si no es mayor a 150 y mayor a 50  se muestra la recarga un poco transparente  y aumenta la municion del soldado en 30
    si no es mayor a 50 y mayor a 0  se muestra la recarga un poco mas transparente  y aumenta la municion del soldado en 10
    update:
    disminuye el tiempo, activa el metodo mostrar
    
    '''
    ##objeto   de recarga de municion
    class  recarga(pygame.sprite.Sprite): 
        def __init__(self) :
            super().__init__()
            self.x=0
            self.y=0
            self.recarga=0
            self.tiempo=0
            self.image = pygame.Surface((60, 50))  # Crea una superficie para la imagen del botiquib
            self.rect = self.image.get_rect()  # Obtiene el rectángulo que representa la imagen
            self.rect.midleft = (self.x, self.y)  # Coloca el centro de la imagen en la posición (x, y)
        ## METODO QUE MUESTRA EN LA PANTALLA LA RECARGA PERO EN UN TIEMPO  PROLONGADO
        def mostrar(self):
            if self.tiempo>150:
                PANTALLA.blit(imagen.recarga[0],(self.x,self.y))
                self.recarga=100
            elif self.tiempo<=50 and self.tiempo<=150:
                PANTALLA.blit(imagen.recarga[1],(self.x,self.y))
                self.recarga=50
            else:
                PANTALLA.blit(imagen.recarga[2],(self.x,self.y))
                self.recarga=20
        ## METODO QUE ACTUALIZA EL TIEMPO DE VIDA DEL BOTIQUIN Y LO MUESTRA
        def update(self):
            self.tiempo-=1
            self.mostrar()
            self.rect = pygame.Rect(self.x, self.y, 60, 50)
            #pygame.draw.rect(PANTALLA, (255, 0, 0), (self.x,self.y,60,50), 2)
    
    '''
      Metodo que  agrega botiquin en el ecenario  obtiene como parametro el objeto soldado
      para poder ponerlo cerca de la poscion de soldado dependiendo de la posicion en la que este el soldado,
      creamos  un objeto nuevo donde es agregado al grupo de sprite  de(lista_botiquin, grupos_objeto)
      
    '''
    #metodo agregar botiquin
    def agregar_botiquin(soldado):
        botiqui=botiquin()
        ## condiciones que  agrega en el mapa el bitiquin pero que no se pase de las dimensiones de la pantalla 
        if soldado.x+150>900 and soldado.y+100>=700:
            botiqui.x=soldado.x-150
            botiqui.y=soldado.y-100
        elif soldado.x+150>900 and soldado.y+100<700:
            botiqui.x=soldado.x-150
            botiqui.y=soldado.y+100
        elif soldado.x+150<900 and soldado.y+100>700:
            botiqui.x=soldado.x+150
            botiqui.y=soldado.y-100
        else:
            botiqui.x=soldado.x+150
            botiqui.y=soldado.y+100
        botiqui.tiempo=200
        grupo_objeto.add(botiqui)
        lista_botiquin.add(botiqui)
    '''
        Metodo que  agrega recarga en el ecenario  obtiene como parametro el objeto soldado
        para poder ponerlo cerca de la poscion de soldado dependiendo de la posicion en la que este el soldado,
        creamos  un objeto nuevo donde es agregado al grupo de sprite  de(lista_recarga, grupos_objeto)
    '''
    #metodo agregar recarga
    def agregar_recarga(soldado):
        recar=recarga()
        ## condiciones que  agrega en el mapa la municion pero que no se pase de las dimensiones de la pantalla 
        if soldado.x+300>900 and soldado.y+100>=700:
            recar.x=soldado.x-250
            recar.y=soldado.y-100
        elif soldado.x+300>900 and soldado.y+100<700:
            recar.x=soldado.x-250
            recar.y=soldado.y+100
        elif soldado.x+300<900 and soldado.y+100>700:
            recar.x=soldado.x+250
            recar.y=soldado.y-100
        else:
            recar.x=soldado.x+250
            recar.y=soldado.y+100
        recar.tiempo=300
        grupo_objeto.add(recar)
        lista_recarga.add(recar)
    '''
     metodo que simula movimiento del ecenario donde obtiene por parametro la tecla:izquierda, derecha y el objeto soldado
     en la variable x_rekativa se calcula el desplazamiento relativo en el eje x del soldado con respecto al fondo.
     Utiliza la propiedad mov_x del objeto soldado y obtiene el ancho del fondo con fondo.get_rect().width.
     El operador % se utiliza para asegurarse de que el desplazamiento relativo siempre esté dentro del ancho del fondo.
     si la variable x_relativa es menor que el ancho del la pantalla dibuja el fondo. 
     Esto se hace para asegurarse de que haya un fondo continuo mientras el jugador se mueve hacia la derecha.
     con la condicion derecha  se reduce el valor de soldado.mov_x en 15. Esto indica que el soldado se está moviendo hacia la derecha.
     con la condicion izquierda se aumenta el valor de soldado.mov_x en 15. Esto indica que el soldado se está moviendo hacia la izquierda
    '''
    # Fondo en movimiento creando animacion de movimiento sobre el eje x
    def movimiento_fondo(derecha,izquierda,soldado):
        #mueve la imagen sobre el eje x
            x_relativa = soldado.mov_x % fondo.get_rect().width 
            PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
            if x_relativa < ANCHO:
                PANTALLA.blit(fondo, (x_relativa, 0))
            if derecha:
                soldado.mov_x  += -15
            if izquierda:
                soldado.mov_x  += 15
    
    '''
        metodo que activa los enemigo en el mapa devuelva la variable tiempo, n 
        la variable tiempo : tiempo que necesita para que sea agregado cada zombie en el ecenario
        la variable n: es un contador que me permite intercalar los dos tipos de zombie
        el metodo recibe como parametro el objeto soldado, tiempo, velocidad y salida
        el objeto soldado: para poder obtener la posicion del soldado y agregar el zombie cerca de el
        tiempo: es el tiempo que necesita para que sea agregado cada zombie en el ecenario
        velocidad: es la velocidad que tiene el zombie
        salida: es la distanci con respecto al soldado 
        llama el metodo agrega_enemigos
        
    '''
    ### utilizo dos metodos para agregar los zombie en el mapa  en este metodo intercalo los dos zombie diferentes
    def activa_enemigo(soldado,tiempo,velocidad,n,salida):
        if n==0:
            zombi=zombie()   
            tiempo=agregar_enemigos(zombi,soldado,tiempo,velocidad,salida)
            n=1
        else:
            zombi=zombie2()   
            tiempo=agregar_enemigos(zombi,soldado,tiempo,velocidad,salida)
            n=0
        return tiempo,n
    '''
        metodo que agrega los enemigos en el mapa dependiendo la posicion del soldado pero alejado 900 px
        el metodo recibe como parametro el objeto soldado, tiempo, velocidad y salida
        el objeto soldado: para poder obtener la posicion del soldado y agregar el zombie cerca de el
        tiempo: es el tiempo que necesita para que sea agregado cada zombie en el ecenario
        velocidad: es la velocidad que tiene el zombie
        salida: es la distancia con respecto al soldado
        retorna tiempo_agregar enemigos 
        cuando score es mayor o igual a 100 la distancia de salida de los zombie disminuye a 800

    '''
    ## metodo que agrega los enemigos en el mapa dependiendo la posicion del soldado pero alejado 900 px
    def agregar_enemigos(zombi,soldado,tiempo_agregar_enemigo,velocidad,salida):
        if soldado.score<100 and pygame.time.get_ticks() >= tiempo_agregar_enemigo:
            zombi.rect.x  = soldado.x+900
            zombi.rect.y= soldado.y
            zombi.soldado=soldado
            zombi.velocidad=velocidad
            grupo_zombie.add(zombi)
            grupo_objeto.add(zombi )
            tiempo_agregar_enemigo = pygame.time.get_ticks() + salida
        elif  soldado.score>100 and pygame.time.get_ticks() >= tiempo_agregar_enemigo:
            zombi.rect.x  = soldado.x+800
            zombi.rect.y= soldado.y
            zombi.velocidad=velocidad
            zombi.soldado=soldado
            grupo_zombie.add(zombi)
            grupo_objeto.add(zombi )
            tiempo_agregar_enemigo = pygame.time.get_ticks() + salida
            
        return tiempo_agregar_enemigo
    '''
        metodo que inicia el juego variable:
        sound_playing: variable que me permite saber si el sonido esta activo o no
        pausar: variable que me permite saber si el juego esta pausado o no
        terminado: variable que me permite saber si el juego esta terminado o no
        bos: objeto de la clase boss
        soldado: objeto de la clase soldado
        bala: objeto de la clase balas
        tiem1: variable que me permite agregar botiquin y municiones al ecenario 
        tiem2: variable que me permite agregar botiquin y municiones al ecenario
        grupo_objeto: grupo de objetos que me permite agregar los objetos al ecenario
        n: variable que me permite intercalar los dos tipos de zombie
        activa_botiquin: variable que me permite saber si el botiquin esta activo o no
        activar_jefe: variable que me permite saber si el jefe esta activo o no
        reloj: variable que me permite controlar los cuadros por segundo del juego la fluidez 
        tiempo: variable que me permite controlarel tiempo de salida de los zombie
        jueg: variable que me permite saber si el juego esta activo o no
        condiciones:
        si el juego esta activo:
        con el ciclo for recoremos los eventos ala hora de utilizar el teclado 
        si el evento es igual a pygame.QUIT:
        el juego se termina y se limpia la memoria
        en la variables :
        derecha: se le asigna el valor de la tecla derecha
        izquierda: se le asigna el valor de la tecla A
        arriba: se le asigna el valor de la tecla W
        abajo: se le asigna el valor de la tecla S
        dispara: se le asigna el valor de la tecla E
        gancho  se la asifna el valor de la tecl R
        p: se le asigna el valor de la tecla p
        si la tecla derecha esta activa: el soldado se mueve a la derecha
        si la tecla izquierda esta activa:el soldado se mueve a la izquierda
        si la tecla arriba esta activa: el soldado se mueve arriba
        si la tecla abajo esta activa: el soldado se mueve abajo
        si la tecla dispara esta activa: se activa el sonido de la bala y crea una nueva bala 
        si la tecla gancho esta activa: se activa el movimiento del gancho
        si la tecla p esta activa: se pausa el juego
        si el juego esta terminado: muestra la ventana (gano o perdio)
        si el juego no esta terminado:
         se agrega zombi en el ecenario
         se agrega municiones y botiquin en el ecenario
         se verifican coliciones de balas con zombi
         soldado con zombie
        si el soldado tiene un score mayor o igua a 100 se agrega el jefe en el ecenario
        se verifica coliciones de boss con solado
        se verifica las coliciones de las balas con el boss
        
    '''
### metodo que inicia le juego  
    def juego():
        sound_playing = False
        pausar=0
        terminado=False
        bos= boss()
        soldado = Soldado(50, 400, 40, 110,7,120)### creo el objeto del soldado
        bala = balas()
        tiem1=0
        tiem2=0
        grupo_objeto.add(soldado)
        grupo_objeto.add(bala)
        n=0
        activa_botiquin=1
        activar_jefe=0
        pygame.init()
        reloj = pygame.time.Clock()
        tiempo=0
        jueg=True
        while jueg:
            reloj.tick(18)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    jueg=False
                    gc.collect()
                    sonido_fondo.stop()
                ## variable que me obtine  el valor de las teclas w,s,d,e,a,r,p
                teclas_presionadas = pygame.key.get_pressed()
                tecla_arriba_presionada = teclas_presionadas[pygame.K_w]
                tecla_abajo_presionada = teclas_presionadas[pygame.K_s]
                tecla_derecha_presionada = teclas_presionadas[pygame.K_d]
                tecla_izquierda_presionada = teclas_presionadas[pygame.K_a]
                tecla_dispara_presionada = teclas_presionadas[pygame.K_e]
                tecla_pausar_juego= teclas_presionadas[pygame.K_p]
                tecla_gancho= teclas_presionadas[pygame.K_r]

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    x = mouse_pos[0]
                    y = mouse_pos[1]
                ## CONDICION QUE PAUSA EL JUEGO 
                if tecla_pausar_juego:
                    pausar=True
                    PANTALLA.blit(reanudar,(350,200))
                    PANTALLA.blit(b_instruciones,(350,330))
                    pygame.display.update()
                ## CONDICION QUE PUEDE DESPAUSAR EL JUEGO Y MOSTRAR LAS INSTRUCCIONES 
                if pausar:
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()          # obtenemos la posicion del mouse
                        x = mouse_pos[0]                            
                        y = mouse_pos[1]    
                        if evento.button==1:                         ## cuando damos clic derecho      
                            x,y = evento.pos
                            if x>= 0 and x<= 1000 and y>= 0 and y<= 700:  ## validamos que el clic este dentro de la pantalla del juego
                                if x > 350 and x<= 620 and y>= 200 and y<= 316: ## posicion del boton reanudar 
                                    pausar=False                                #desabilitamos pausar
                                if x > 350 and x<= 620 and y>= 330 and y<= 446: # posicion del boton instruciones
                                    PANTALLA.blit(instruciones,(0,0))           #muestra ventana de instruciones 
                                    pygame.display.update()
                                if x > 861 and x<= 953 and y>= 17 and y<= 108:  #boton  cerrar ventana de instruciones 
                                    pausar=False                                #desabilita variable pausar
                ## CONDICION QUE TERMINA EL JUEGO Y PUEDE SELECIONAR SI REINICIA EL JUEGO O SALIR DEL JUEGO
                elif terminado:
                    
                    if bos.salud<=0 or soldado.salud<=0:                           ##condicion  que se activa cuando la vida del soldado o del boss es menor a 0
                            if bos.salud<=0:                                       ## condicion que verifica si gano  el jugado 
                               PANTALLA.blit(ganastes,(0,0))                       ## muestra la pantalla de ganador
                            else:                                                  
                                PANTALLA.blit(perdistes,(0,0))                     ## muestra la pantalla de perdio
                            pygame.display.update()
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()                         ## obtenemo la posicion del mouse cundamos clic 
                        x = mouse_pos[0]
                        y = mouse_pos[1]
                        if evento.button==1:                                       ## cuando damos clic derecho 
                            x,y = evento.pos
                            if x>= 0 and x<= 1000 and y>= 0 and y<= 700:           ## validamos que el clic este dentro de la pantalla del juego 
                              
                                if x > 350 and x<= 620 and y>= 330 and y<= 446:    ## la posicion donde esta el boton de reiniciar juego
                                   iniciar_juego()                                 ## reinicia el juego
                                if x > 377 and x<= 620 and y>= 514 and y<= 618:    #posicion del boton salir
                                    jueg=False                                     ## sale del juego 
                    sound_playing = False
                    disparo.stop()
                ## APLICAMOS LOS MOVIEMINTO DEL JUEGADOR                     
                else:
                    ### ACIONA EL MOVIMIENTOD DEL GANCHO DEL JUGADOR
                    if tecla_gancho:
                        soldado.gancho=True
                        ##SI ENCONTRAMOS UNA COLISION CON UN ZOMBI ACIONANDO EL MOVIMIENTO LO ELIMINAMOS 
                        colision=pygame.sprite.spritecollide(soldado,grupo_zombie,True)
                        for zomb in colision:           ## CON ESTE FOR BUSCAMOS LOS ZOMBIE QUE COLISIONA CON EL SOLDAO PARA ELIMINARLOS
                            grupo_zombie.remove(zomb)
                            grupo_objeto.remove(zomb)
                            soldado.score+=1
                            
                        if soldado.rect.colliderect(bos.rect):
                            bos.salud-=1
                            soldado.score+=1
                            if bos.salud==0:
                                bos.animation_muerte=True
                                bos.update()
                         
                    ### condicion que activa todos los movimiento de desplazamiento del soldado       
                    else:
                        soldado.gancho=False
                    ##condicion que activa el movimiento de disparar mientra que se mueve hacia la derecha verificando que nos se salga de la pantalla
                    if tecla_dispara_presionada and tecla_derecha_presionada and soldado.x < 900 - velocidad - ancho:
                            if soldado.balas>0:                        ### condicion que verifica que el soldado tenga disponible balas para poder activar movimiento
                                soldado.corrie_dispara_izquierda=False ## desactiva la animacion que corre hacia la izquierad
                                soldado.corrie_dispara_derecha=True     ## activa animacion que corre hacia la derecha
                                soldado.balas-=1                        ## disminuye la cantidad de bala que tiene el soldado disponible
                                soldado.x += velocidad                  ## el solado se desplaza sobre el eje x
                                if not sound_playing:
                                    # Reproducir el sonido de golpe solo si no se está reproduciendo actualmente
                                    disparo.play(-1)  # -1 indica reproducción en bucle
                                    sound_playing = True
                                bala = balas()                         ## creamos el bojeto de bala  
                                bala.derecha=tecla_derecha_presionada  ## direcion de la bala oprimimos derecha sale hacia la dereca
                                bala.izquierda=tecla_izquierda_presionada ## direcion de bala hacia la izquierda
                                bala.rect.x = soldado.x + 120           ## aumentamos la posicion en los ejes para simular que la bala sale del proyectil
                                bala.rect.y = soldado.y + 70 
                                lista_balas.add(bala)                   ## agregamos ala lista de bala de sprite el objeto crado    
                                grupo_objeto.add(bala)                  ## agragamos al grupo de sprite principal el objeto nuevo creado
                    ##condicion que activa el movimiento de disparar mientra que se mueve hacia la izquierda 
                    elif tecla_dispara_presionada and tecla_izquierda_presionada:
                            if soldado.balas>0:
                                soldado.balas-=1
                                soldado.x -= velocidad
                                soldado.corrie_dispara_izquierda=True
                                soldado.corrie_dispara_derecha=False
                                if not sound_playing:
                                    # Reproducir el sonido de golpe solo si no se está reproduciendo actualmente
                                    disparo.play(-1)  # -1 indica reproducción en bucle
                                    sound_playing = True
                                bala = balas()
                                bala.derecha=tecla_derecha_presionada   ##  bala_derecha  obtiene el valor de la tecla presiona para saber la trayectorial de la bala
                                bala.izquierda=tecla_izquierda_presionada
                                bala.rect.x = soldado.x                 #obtiene  la posicion del soldado en el eje x
                                bala.rect.y = soldado.y + 70            #obtiene la posicion del soldado en el eje y  le aumentamos 70 tener la animacion corecta que sale del proyectil
                                lista_balas.add(bala)
                                grupo_objeto.add(bala)
                    ##condicion que activa el movimiento de disparar quieto
                    elif tecla_dispara_presionada:
                        if soldado.balas>0:
                            soldado.disparar = True
                            soldado.balas-=1
                            if not sound_playing:
                                # Reproducir el sonido de golpe solo si no se está reproduciendo actualmente
                                disparo.play(-1)  # -1 indica reproducción en bucle
                                sound_playing = True
                           
                            bala = balas()
                            bala.derecha=tecla_derecha_presionada
                            bala.izquierda=tecla_izquierda_presionada
                            bala.rect.x = soldado.x + 115
                            bala.rect.y = soldado.y + 62
                            lista_balas.add(bala)
                            grupo_objeto.add(bala)
                    ##condicion que activa el movimiento de correr diagona hacia bajo y hacia la derecha poniendo condiciones de un espacio reducido por donde se puede mover el soldado
                    elif tecla_izquierda_presionada and tecla_abajo_presionada and soldado.y < 600 and soldado.x > velocidad:
                        soldado.x -= velocidad
                        soldado.y += velocidad
                        soldado.izquierda = True  ## variable que activa la animacion hacia la izquierda
                        soldado.derecha = False    ## variable que activa la animiacion hacia la derecha
                    # condicion que activa el movimiento  diagonal hacia ariba hacia la izquierda  poniendo condicion de un espacio reducido en el cual se pude mover el soldado
                    elif tecla_izquierda_presionada and tecla_arriba_presionada and soldado.y > 410 and soldado.x > velocidad:
                        soldado.x -= velocidad
                        soldado.y -= velocidad
                        soldado.izquierda = True
                        soldado.derecha = False
                    # condicion que activa el movimiento  diagonal hacia ariba, hacia la derecha poniendo condicion de un espacio reducido en el cual se pude mover el soldado
                    elif tecla_derecha_presionada and tecla_arriba_presionada and soldado.y > 410 and soldado.x < 900 - velocidad - ancho:
                        soldado.x += velocidad
                        soldado.y -= velocidad
                        soldado.izquierda = False
                        soldado.derecha = True
                    # condicion que activa el movimiento  diagonal hacia abajo, hacia la derecha poniendo condicion de un espacio reducido en el cual se pude mover el soldado
                    elif tecla_derecha_presionada and tecla_abajo_presionada and soldado.y < 600 and soldado.x < 900 - velocidad - ancho:
                        soldado.x += velocidad
                        soldado.y += velocidad
                        soldado.izquierda = False
                        soldado.derecha = True
                    ## condicional que activa movimiento hacia la izquierda
                    elif tecla_izquierda_presionada and soldado.x > velocidad:
                        soldado.x -= velocidad
                        soldado.izquierda = True
                        soldado.derecha = False
                    ## condicional que activa movimiento hacia la derecha
                    elif tecla_derecha_presionada and soldado.x < 900 - velocidad - ancho:
                        soldado.x += velocidad
                        soldado.izquierda = False
                        soldado.derecha = True
                    ## condicional que activa movimiento hacia arriba
                    elif tecla_arriba_presionada and soldado.y > 410:
                        soldado.y -= 7
                        soldado.derecha = True
                        soldado.izquierda = False
                    
                    ## condicional que activa movimiento hacia abajo
                    elif tecla_abajo_presionada and soldado.y < 600:
                        soldado.y += 7
                        soldado.derecha = True
                        soldado.izquierda = False
                    ## condicion que activa el movimiento estatico cuando no se oprime ninguna tecla que active un movimiento del soldado
                    else:
                        soldado.izquierda = False
                        soldado.derecha = False
                        soldado.cuentaPasos = 0
                        soldado.disparar = False
                        soldado.corrie_dispara_izquierda=False
                        soldado.corrie_dispara_derecha=False
                        sound_playing = False
                        disparo.stop()
            ## condicion  que muestra la pantalla si el jugador gano o perdio       
            if terminado:
                mouse_pos = pygame.mouse.get_pos()          # se 
                x = mouse_pos[0]
                y = mouse_pos[1]  
                if x>= 0 and x<= 1000 and y>= 0 and y<= 700:      
                    if x > 370 and x<= 620 and y>= 330 and y<= 446:
                       PANTALLA.blit(breintentar,(355,320))
                    elif x > 377 and x<= 620 and y>= 514 and y<= 618:
                        PANTALLA.blit(bsalir,(355,510))
                    else:
                        if bos.salud<=0:
                            PANTALLA.blit(ganastes,(0,0))
                        else:
                            PANTALLA.blit(perdistes,(0,0))
                    puntaje = fuente.render(str(soldado.score), True, blanco)
                    PANTALLA.blit(puntaje,(458,251))
                    pygame.display.update()
            ## condicion que pausa el juego si oprime la tecla de pausa (p)     
            elif pausar:
                pass
            else:
                if bos.salud<=0 or soldado.salud<=0:
                    terminado=True
                #Activar jefe despues de un puntaje de 100
                if soldado.score>=100:
                    if activa_botiquin==1:
                        if soldado.salud<=30:
                            agregar_botiquin(soldado)
                            agregar_recarga(soldado)
                            activa_botiquin=0
                    ### condicion que agrega al jefe uan sola vez                  
                    if activar_jefe==0:
                        bos.soldado=soldado
                        bos.rect.x = soldado.x+900
                        bos.rect.y= soldado.y
                        #bos.activar_saltos=True
                        grupo_objeto.add(bos)
                        activar_jefe=1
                    else:
                        ##codicion que aumenta la velocidad del jefe despues que su salud esta en 100
                        if bos.salud<=100:
                            bos.velocidad=30
                        # CONDICION QUE ACTIVA EL MOVIENTO DOS DEL JEFE  LOS SALTOS              
                        if bos.salud<=250 and bos.salud>=200 :
                            bos.activar_saltos=True
                            if bos.rect.colliderect(soldado.rect): ## CONDICION QUE VERIFICA SI HAY COLISION CON EL SOLDADO
                                soldado.salud-=1
                                timer = threading.Timer(2, bos.tiempo_espera) ## UTILIZAMOS UN NUEVO HILO PARA PODER HACER ESPERA Y NO SE DEVUELVA DE UNA EL JEFE DESPUES DE HABER  GOLPEADO el soldao
                                timer.start()  ## activamos el hilo
                                
                        else:
                            #MOVIMIENTO 1
                            bos.activar_saltos=False
                            #COLISION DE JEFE CON SOLDADO
                            if bos.rect.colliderect(soldado.rect) :
                                soldado.salud-=1
                                bos.activ_atacar=True
                                bos.a=0
                            ## CONDICION QUE ACTIVA EL SONIDO DEL GOLPE
                            if bos.rect.colliderect(soldado.rect) and not sound_playing:
                                golpe.play()
                                sound_playing = True
                                bos.activ_atacar=True
                                bos.a=0
                            ## CONDICION QUE PARA EL SONIDO DEL GOLPE
                            elif not bos.rect.colliderect(soldado.rect):
                                sound_playing = False
    
                            #CONDICION QUE ACTIVA ZOMBIE DESPUES QUE LA SALUDE DLE JEFE ESTA EN MENOS DE BOS<200 Y BOS>100 
                            if bos.salud<=100 and bos.salud>50 or bos.salud<200 and bos.salud>150 :
                                tiempo,n=activa_enemigo(soldado,tiempo,20,n,700)
                        #COLISION DE BALAS CON EL JEFE
                        for bal in lista_balas:
                            if bal.rect.colliderect(bos.rect):
                                lista_balas.remove(bal)
                                grupo_objeto.remove(bal)
                                bos.salud-=1
                                soldado.score+=1
                                if bos.salud==0:
                                    bos.animation_muerte=True
                                    bos.update()
                                   
                else:
                    #AGREGAMOS ZOMBIE AL MAPA CON UN LAPSO DE TIEMPO PARA QUE NO APARESCA EN MANADA
                    if soldado.score<10:
                        tiempo,n=activa_enemigo(soldado,tiempo,5,n,1000)   ###  devuelve  el tiempo para tener una referencia de cada tiempo de salida del zombie y el n es para el cambio del zombie(zombi1 zombie2)  
                    elif soldado.score>=10 and soldado.score<20:
                        tiempo,n=activa_enemigo(soldado,tiempo,20,n,700)   ### acortamos la distacia de salida cada vez que elimina mas enemigos
                    elif soldado.score>=20 and soldado.score<69:
                        tiempo,n=activa_enemigo(soldado,tiempo,15,n,600)
                    elif soldado.score>=69 and soldado.score<100:
                        tiempo,n=activa_enemigo(soldado,tiempo,30,n,500)
                   
                    #AGREGANDO BOTIQUIN EN EL MAPA EN DOS LAPSO DEL JUEGO ANTES DE LLEGAR AL JEFE:
                    if soldado.score>=30 and soldado.score <31 :
                         if tiem1==0:                               #condicion que agrega botiquin y municione en un 
                            agregar_botiquin(soldado)
                            agregar_recarga(soldado)
                            tiem1=1
                        
                    if  soldado.score>=70 and soldado.score<=71:
                         if tiem2==0:
                            agregar_botiquin(soldado)
                            agregar_recarga(soldado)
                            tiem2=1
                ##ACTUALIZAMOS EL MOVIMIENTO DEL FONDO  DEL JUEGO
                movimiento_fondo(tecla_derecha_presionada, tecla_izquierda_presionada, soldado)
                grupo_objeto.update()
                #colision de balas con zombie
                for bal in lista_balas:
                    for zomb in grupo_zombie:
                        if bal.rect.colliderect(zomb.rect):   ## verificamo colision de balas con los zombie
                            lista_balas.remove(bal)           #eliminamos la bala de que colisiona con el zombie al grupo de esprite list_bala y grupo_objetos
                            grupo_objeto.remove(bal)
                            zomb.salud-=1
                            if zomb.salud<=0:                 #verificamos la salud del zombie para poderlo eliminar del ecenario
                                if not zomb.animacion_muerte:
                                    zomb.animacion_muerte = True
                                    zomb.update()   
                                grupo_zombie.remove(zomb)    ##eliminamos el zombie  del grupo de sprite de grupo _zombie
                                grupo_objeto.remove(zomb)    # eliminamos el zombien del grupo de sprite del grupo_objeto 
                            soldado.score += 1               # aumentamos el score del  soldado
    
                            break
                #colision botiquin con soldado
                for bot in lista_botiquin:                # recoremos todos los botiquin que estan  la lista de botiquin
                    if bot.tiempo<0:                       ##si el tiempo del botiqui es menor a 0 eliminamos el botiquin
                        lista_botiquin.remove(bot)         # eliminamos el botiquin del grupo de sprite de lista_botiqun
                        grupo_objeto.remove(bot)           #eliminamos el botiquin del grupo de sprite de grupo_objeto
                    if bot.rect.colliderect(soldado.rect): # verificamos si hay colision del  soldado con el botiquin  
                        soldado.salud+=bot.vida            # aumentamos la salud del soldado 
                        grupo_objeto.remove(bot)           # removemos el botiquin del ecenario y lo eliminamos de los grupos sprite en los que este
                        lista_botiquin.remove(bot)
                #colision recarga con soldado 
                for rec in lista_recarga:                   #recoremos todos las municionees que estan la lista_recarga
                    if rec.tiempo<0:                        ##si el tiempo de las municiones  es menor a 0 eliminamos la municion del eceneario        
                        lista_recarga.remove(rec)               
                        grupo_objeto.remove(rec)
                    if rec.rect.colliderect(soldado.rect):  #verificamos si hay colision del  soldado con  la municion
                        soldado.balas+=rec.recarga          # aumenta las municiones del soldado
                        grupo_objeto.remove(rec)            #eliminada del ecenario  y de la lista de grupo_objeto y lista_recarga
                        lista_recarga.remove(rec)
                #colision de zombie con soldado
                colisi = pygame.sprite.spritecollide(soldado, grupo_zombie,False) ## colisiona un zombie con el soldado
                for zombb in colisi:                                              # activa la funcion atacar del zombi
                    zombb.activ_atacar = True
                    zombb.update()
                    soldado.salud -= 1                                            # resta la vida del soldado 
                    if soldado.salud == 0:
                        soldado.update()
                    

                lista_balas.draw(PANTALLA)                                       # pinta las balas en el ecenenario 
                pygame.display.flip()                                            #actualiza la pantalla del ecenarios
    juego()
            
#iniciar_juego()
import pygame
''''
la funcionalidad de el modulo imagene es almacenar todas la animacion del soldado, zombi,zombi2, botiquin, munucion=recarga
Todas la variable exepto la variable personaje_quieto y recargari son una lista de imagenes de acuerdo a su nombre contiene la cantidad de imagenes para generar el movimiento de la accion ejecutada
'''
##TODAS LA IMAGENE UTILIZADA EN EL JUEGO 
personaje_quieto=pygame.image.load('soldado/caminar/caminando1_derecha.png')
personaje_corriendo_derecha=[pygame.image.load('soldado/run/run1_derecha.png'),
                             pygame.image.load('soldado/run/run2_derecha.png'),
                            pygame.image.load('soldado/run/run3_derecha.png'),
                            pygame.image.load('soldado/run/run4_derecha.png'),
                            pygame.image.load('soldado/run/run5_derecha.png'),
                            pygame.image.load('soldado/run/run6_derecha.png'),
                            pygame.image.load('soldado/run/run7_derecha.png'),
                            pygame.image.load('soldado/run/run8_derecha.png')
                            ]
personaje_corriendo_izquierda=[
                            pygame.image.load('soldado/run/run1_izquierda.png'),
                            pygame.image.load('soldado/run/run2_izquierda.png'),
                            pygame.image.load('soldado/run/run3_izquierda.png'),
                            pygame.image.load('soldado/run/run4_izquierda.png'),
                            pygame.image.load('soldado/run/run5_izquierda.png'),
                            pygame.image.load('soldado/run/run6_izquierda.png'),
                            pygame.image.load('soldado/run/run7_izquierda.png'),
                            pygame.image.load('soldado/run/run8_izquierda.png') 
                            ]
personaje_caminando_derecha=[
                pygame.image.load('soldado/caminar/caminando1_derecha.png'),
				pygame.image.load('soldado/caminar/caminando2_derecha.png'),
				pygame.image.load('soldado/caminar/caminando3_derecha.png'),
				pygame.image.load('soldado/caminar/caminando4_derecha.png'),
				pygame.image.load('soldado/caminar/caminando5_derecha.png'),
				pygame.image.load('soldado/caminar/caminando6_derecha.png'),
                pygame.image.load('soldado/caminar/caminando7_derecha.png')
                ]
personaje_caminado_izquierda=[
                pygame.image.load('soldado/caminar/caminando1_izquierda.png'),
                pygame.image.load('soldado/caminar/caminando2_izquierda.png'),
                pygame.image.load('soldado/caminar/caminando3_izquierda.png'),
                pygame.image.load('soldado/caminar/caminando4_izquierda.png'),
                pygame.image.load('soldado/caminar/caminando5_izquierda.png'),
                pygame.image.load('soldado/caminar/caminando6_izquierda.png'),
                pygame.image.load('soldado/caminar/caminando7_izquierda.png')
]
personaje_disparar_derecha=[
                    pygame.image.load('soldado/atacar/atacar1_derecha.png'),
                    pygame.image.load('soldado/atacar/atacar2_derecha.png'),
                    pygame.image.load('soldado/atacar/atacar3_derecha.png'),
                    pygame.image.load('soldado/atacar/atacar4_derecha.png')
                    
                    ]

personaje_disparar_izquierda=[pygame.image.load('soldado/atacar/atacar1_izquierda.png'),
                    pygame.image.load('soldado/atacar/atacar2_izquierda.png'),
                    pygame.image.load('soldado/atacar/atacar3_izquierda.png'),
                    pygame.image.load('soldado/atacar/atacar4_izquierda.png')
            ]
personaje_muerte_derecha=[pygame.image.load('soldado/muerte/muerte1_derecha.png'),
                pygame.image.load('soldado/muerte/muerte2_derecha.png'),    
                pygame.image.load('soldado/muerte/muerte3_derecha.png'),
                pygame.image.load('soldado/muerte/muerte4_derecha.png')
                
]
personaje_gancho_derecha=[
                pygame.image.load('soldado/gancho/gancho1_derecha.png'),
                pygame.image.load('soldado/gancho/gancho2_derecha.png'),
                pygame.image.load('soldado/gancho/gancho3_derecha.png')
                
]
personaje_gancho_izquierda=[
                pygame.image.load('soldado/gancho/gancho1_izquierda.png'),
                pygame.image.load('soldado/gancho/gancho2_izquierda.png'),
                pygame.image.load('soldado/gancho/gancho3_izquierda.png')
]
personaje_muerte_izquierda=[pygame.image.load('soldado/muerte/muerte1_izquierda.png'),
                pygame.image.load('soldado/muerte/muerte2_izquierda.png'),  
                pygame.image.load('soldado/muerte/muerte3_izquierda.png'),
                pygame.image.load('soldado/muerte/muerte4_izquierda.png')
]
zombie1_atacar_derecha=[
                pygame.image.load('zombie/atacar/atacar1_derecha.png'),
                pygame.image.load('zombie/atacar/atacar2_derecha.png'),
                pygame.image.load('zombie/atacar/atacar3_derecha.png'),
                pygame.image.load('zombie/atacar/atacar4_derecha.png')
]
zombie1_atacar_izquierda=[ 
                pygame.image.load('zombie/atacar/atacar1_izquierda.png'),
                pygame.image.load('zombie/atacar/atacar2_izquierda.png'),
                pygame.image.load('zombie/atacar/atacar3_izquierda.png'),
                pygame.image.load('zombie/atacar/atacar4_izquierda.png')
]
zombie1_caminar_derecha=[pygame.image.load('zombie/caminar/caminar1_derecha.png'),
                pygame.image.load('zombie/caminar/caminar2_derecha.png'),
                pygame.image.load('zombie/caminar/caminar3_derecha.png'),
                pygame.image.load('zombie/caminar/caminar4_derecha.png'),
                pygame.image.load('zombie/caminar/caminar5_derecha.png'),
                pygame.image.load('zombie/caminar/caminar6_derecha.png'),
                pygame.image.load('zombie/caminar/caminar7_derecha.png')
]
zombie1_caminar_izquierda=[
                pygame.image.load('zombie/caminar/caminar2_izquierda.png'),
                pygame.image.load('zombie/caminar/caminar3_izquierda.png'),
                pygame.image.load('zombie/caminar/caminar4_izquierda.png'),
                pygame.image.load('zombie/caminar/caminar5_izquierda.png'),
                pygame.image.load('zombie/caminar/caminar6_izquierda.png'),
                pygame.image.load('zombie/caminar/caminar7_izquierda.png')
                
]
zombie1_muerte_derecha=[
                pygame.image.load('zombie/muerte/muerte1_derecha.png'),
                pygame.image.load('zombie/muerte/muerte1_derecha.png'),
                pygame.image.load('zombie/muerte/muerte1_derecha.png'),
                pygame.image.load('zombie/muerte/muerte2_derecha.png'),
                pygame.image.load('zombie/muerte/muerte2_derecha.png'),
                pygame.image.load('zombie/muerte/muerte2_derecha.png'),
                pygame.image.load('zombie/muerte/muerte3_derecha.png'),
                pygame.image.load('zombie/muerte/muerte3_derecha.png'),
                pygame.image.load('zombie/muerte/muerte3_derecha.png'),
                pygame.image.load('zombie/muerte/muerte4_derecha.png'),
                pygame.image.load('zombie/muerte/muerte4_derecha.png'),
                pygame.image.load('zombie/muerte/muerte4_derecha.png'),
                pygame.image.load('zombie/muerte/muerte5_derecha.png'),
                pygame.image.load('zombie/muerte/muerte5_derecha.png'),
                pygame.image.load('zombie/muerte/muerte5_derecha.png')
]
zombie1_muerte_izquierda=[
                pygame.image.load('zombie/muerte/muerte1_izquierda.png'),
                pygame.image.load('zombie/muerte/muerte1_izquierda.png'),
                pygame.image.load('zombie/muerte/muerte1_izquierda.png'),
                pygame.image.load('zombie/muerte/muerte2_izquierda.png'),
                pygame.image.load('zombie/muerte/muerte2_izquierda.png'),
                pygame.image.load('zombie/muerte/muerte2_izquierda.png'),
                pygame.image.load('zombie/muerte/muerte3_izquierda.png'),
                pygame.image.load('zombie/muerte/muerte3_izquierda.png'),
                pygame.image.load('zombie/muerte/muerte3_izquierda.png'),
                pygame.image.load('zombie/muerte/muerte4_izquierda.png'),
                pygame.image.load('zombie/muerte/muerte4_izquierda.png'),
                pygame.image.load('zombie/muerte/muerte4_izquierda.png'),
                pygame.image.load('zombie/muerte/muerte5_izquierda.png'),
                pygame.image.load('zombie/muerte/muerte5_izquierda.png'),
                pygame.image.load('zombie/muerte/muerte5_izquierda.png')

]
zombie2_atacar_derecha=[
                pygame.image.load('zombie2/atacar/atacar1_derecha.png'),
                pygame.image.load('zombie2/atacar/atacar2_derecha.png'),
                pygame.image.load('zombie2/atacar/atacar3_derecha.png'),
                pygame.image.load('zombie2/atacar/atacar4_derecha.png')
]
zombie2_atacar_izquierda=[ 
                pygame.image.load('zombie2/atacar/atacar1_izquierda.png'),
                pygame.image.load('zombie2/atacar/atacar2_izquierda.png'),
                pygame.image.load('zombie2/atacar/atacar3_izquierda.png'),
                pygame.image.load('zombie2/atacar/atacar4_izquierda.png')
]
zombie2_caminar_derecha=[pygame.image.load('zombie2/caminar/caminar1_derecha.png'),
                pygame.image.load('zombie2/caminar/caminar2_derecha.png'),
                pygame.image.load('zombie2/caminar/caminar3_derecha.png'),
                pygame.image.load('zombie2/caminar/caminar4_derecha.png'),
                pygame.image.load('zombie2/caminar/caminar5_derecha.png'),
                pygame.image.load('zombie2/caminar/caminar6_derecha.png')
]
zombie2_caminar_izquierda=[
                pygame.image.load('zombie2/caminar/caminar2_izquierda.png'),
                pygame.image.load('zombie2/caminar/caminar3_izquierda.png'),
                pygame.image.load('zombie2/caminar/caminar4_izquierda.png'),
                pygame.image.load('zombie2/caminar/caminar5_izquierda.png'),
                pygame.image.load('zombie2/caminar/caminar6_izquierda.png')
                
]
zombie2_muerte_derecha=[
                pygame.image.load('zombie2/muerte/muerte1_derecha.png'),
                pygame.image.load('zombie2/muerte/muerte1_derecha.png'),
                pygame.image.load('zombie2/muerte/muerte1_derecha.png'),
                pygame.image.load('zombie2/muerte/muerte2_derecha.png'),
                pygame.image.load('zombie2/muerte/muerte2_derecha.png'),
                pygame.image.load('zombie2/muerte/muerte2_derecha.png'),
                pygame.image.load('zombie2/muerte/muerte3_derecha.png'),
                pygame.image.load('zombie2/muerte/muerte3_derecha.png'),
                pygame.image.load('zombie2/muerte/muerte3_derecha.png'),
                pygame.image.load('zombie2/muerte/muerte4_derecha.png'),
                pygame.image.load('zombie2/muerte/muerte4_derecha.png'),
                pygame.image.load('zombie/muerte/muerte4_derecha.png'),
                pygame.image.load('zombie2/muerte/muerte5_derecha.png'),
                pygame.image.load('zombie2/muerte/muerte5_derecha.png'),
                pygame.image.load('zombie2/muerte/muerte5_derecha.png')
]
zombie2_muerte_izquierda=[
                pygame.image.load('zombie2/muerte/muerte1_izquierda.png'),
                pygame.image.load('zombie2/muerte/muerte1_izquierda.png'),
                pygame.image.load('zombie2/muerte/muerte1_izquierda.png'),
                pygame.image.load('zombie2/muerte/muerte2_izquierda.png'),
                pygame.image.load('zombie2/muerte/muerte2_izquierda.png'),
                pygame.image.load('zombie2/muerte/muerte2_izquierda.png'),
                pygame.image.load('zombie2/muerte/muerte3_izquierda.png'),
                pygame.image.load('zombie2/muerte/muerte3_izquierda.png'),
                pygame.image.load('zombie2/muerte/muerte3_izquierda.png'),
                pygame.image.load('zombie2/muerte/muerte4_izquierda.png'),
                pygame.image.load('zombie2/muerte/muerte4_izquierda.png'),
                pygame.image.load('zombie2/muerte/muerte4_izquierda.png'),
                pygame.image.load('zombie2/muerte/muerte5_izquierda.png'),
                pygame.image.load('zombie2/muerte/muerte5_izquierda.png'),
                pygame.image.load('zombie2/muerte/muerte5_izquierda.png')

]
boss_atacar_derecha=[
                pygame.image.load('boss/atacar/atacar1_derecha.png'),
                pygame.image.load('boss/atacar/atacar2_derecha.png'),
                pygame.image.load('boss/atacar/atacar3_derecha.png'),
                pygame.image.load('boss/atacar/atacar4_derecha.png'),
                pygame.image.load('boss/atacar/atacar5_derecha.png'),
                pygame.image.load('boss/atacar/atacar6_derecha.png'),
                pygame.image.load('boss/atacar/atacar7_derecha.png'),
                pygame.image.load('boss/atacar/atacar8_derecha.png'),
                pygame.image.load('boss/atacar/atacar9_derecha.png'),
                pygame.image.load('boss/atacar/atacar10_derecha.png')
            
]   
boss_atacar_izquierda=[ 
                pygame.image.load('boss/atacar/atacar1_izquierda.png'),
                pygame.image.load('boss/atacar/atacar2_izquierda.png'),
                pygame.image.load('boss/atacar/atacar3_izquierda.png'),
                pygame.image.load('boss/atacar/atacar4_izquierda.png'),
                pygame.image.load('boss/atacar/atacar5_izquierda.png'),
                pygame.image.load('boss/atacar/atacar6_izquierda.png'),
                pygame.image.load('boss/atacar/atacar7_izquierda.png'),
                pygame.image.load('boss/atacar/atacar8_izquierda.png'),
                pygame.image.load('boss/atacar/atacar9_izquierda.png'),
                pygame.image.load('boss/atacar/atacar10_izquierda.png')
                
]
boss_caminar_derecha=[pygame.image.load('boss/caminar/caminar1_derecha.png'),
                pygame.image.load('boss/caminar/caminar2_derecha.png'),
                pygame.image.load('boss/caminar/caminar3_derecha.png'),
                pygame.image.load('boss/caminar/caminar4_derecha.png'),
                pygame.image.load('boss/caminar/caminar5_derecha.png'),
                pygame.image.load('boss/caminar/caminar6_derecha.png'),
                pygame.image.load('boss/caminar/caminar7_derecha.png'),
                pygame.image.load('boss/caminar/caminar8_derecha.png'),
                pygame.image.load('boss/caminar/caminar9_derecha.png'),
                pygame.image.load('boss/caminar/caminar10_derecha.png')
]
boss_caminar_izquierda=[
                pygame.image.load('boss/caminar/caminar2_izquierda.png'),
                pygame.image.load('boss/caminar/caminar3_izquierda.png'),
                pygame.image.load('boss/caminar/caminar4_izquierda.png'),
                pygame.image.load('boss/caminar/caminar5_izquierda.png'),
                pygame.image.load('boss/caminar/caminar6_izquierda.png'),
                pygame.image.load('boss/caminar/caminar7_izquierda.png'),
                pygame.image.load('boss/caminar/caminar8_izquierda.png'),
                pygame.image.load('boss/caminar/caminar9_izquierda.png'),
                pygame.image.load('boss/caminar/caminar10_izquierda.png')
                
]
boss_muerte_derecha=[
                pygame.image.load('boss/muerte/muerte1_derecha.png'),
                pygame.image.load('boss/muerte/muerte2_derecha.png'),
                pygame.image.load('boss/muerte/muerte3_derecha.png'),
                pygame.image.load('boss/muerte/muerte4_derecha.png'),
                pygame.image.load('boss/muerte/muerte5_derecha.png'),
                pygame.image.load('boss/muerte/muerte6_derecha.png'),
                pygame.image.load('boss/muerte/muerte7_derecha.png'),
                pygame.image.load('boss/muerte/muerte8_derecha.png'),
                pygame.image.load('boss/muerte/muerte9_derecha.png'),
                pygame.image.load('boss/muerte/muerte10_derecha.png')
                
]
boss_salto_derecha=[
                pygame.image.load('boss/salto/salto1_derecha.png'),
                pygame.image.load('boss/salto/salto2_derecha.png'),
                pygame.image.load('boss/salto/salto3_derecha.png'),
                pygame.image.load('boss/salto/salto4_derecha.png'),
                pygame.image.load('boss/salto/salto5_derecha.png'),
                pygame.image.load('boss/salto/salto6_derecha.png'),
                pygame.image.load('boss/salto/salto7_derecha.png'),
                pygame.image.load('boss/salto/salto8_derecha.png'),
                pygame.image.load('boss/salto/salto9_derecha.png'),
                pygame.image.load('boss/salto/salto10_derecha.png')
                
]
vida=[pygame.image.load("soldado/vida100.png"),
          pygame.image.load("soldado/vida90.png"),
          pygame.image.load("soldado/vida80.png"),
            pygame.image.load("soldado/vida70.png"),
            pygame.image.load("soldado/vida60.png"),
            pygame.image.load("soldado/vida50.png"),
            pygame.image.load("soldado/vida40.png"),
            pygame.image.load("soldado/vida30.png"),
            pygame.image.load("soldado/vida20.png"),
            pygame.image.load("soldado/vida10.png"),
            pygame.image.load("soldado/vida.png")
            ]
recarga=[pygame.image.load("soldado/recarga.png"),
          pygame.image.load("soldado/recarga2.png"),
          pygame.image.load("soldado/recarga3.png")
]
recargari=pygame.image.load("soldado/recarga_i.png")
bos_vida=[pygame.image.load("boss/vida100.png"),
          pygame.image.load("boss/vida90.png"),
          pygame.image.load("boss/vida80.png"),
          pygame.image.load("boss/vida70.png"),
          pygame.image.load("boss/vida60.png"),
          pygame.image.load("boss/vida50.png"), 
          pygame.image.load("boss/vida40.png"),
          pygame.image.load("boss/vida30.png"),
          pygame.image.load("boss/vida20.png"), 
          pygame.image.load("boss/vida10.png"), 
          pygame.image.load("boss/vida.png")    
  
]
botiquin=[pygame.image.load("soldado/botiquin100.png"),
          pygame.image.load("soldado/botiquin50.png"),
          pygame.image.load("soldado/botiquin20.png")
          
  
]
boss_salto_izquierda=[
                pygame.image.load('boss/salto/salto1_izquierda.png'),
                pygame.image.load('boss/salto/salto2_izquierda.png'),
                pygame.image.load('boss/salto/salto3_izquierda.png'),
                pygame.image.load('boss/salto/salto4_izquierda.png'),
                pygame.image.load('boss/salto/salto5_izquierda.png'),
                pygame.image.load('boss/salto/salto6_izquierda.png'),
                pygame.image.load('boss/salto/salto7_izquierda.png'),
                pygame.image.load('boss/salto/salto8_izquierda.png'),
                pygame.image.load('boss/salto/salto9_izquierda.png'),
                pygame.image.load('boss/salto/salto10_izquierda.png')
]
boss_muerte_izquierda=[
                pygame.image.load('boss/muerte/muerte1_izquierda.png'),
                pygame.image.load('boss/muerte/muerte2_izquierda.png'),
                pygame.image.load('boss/muerte/muerte3_izquierda.png'),
                pygame.image.load('boss/muerte/muerte4_izquierda.png'),
                pygame.image.load('boss/muerte/muerte5_izquierda.png'),
                pygame.image.load('boss/muerte/muerte6_izquierda.png'),
                pygame.image.load('boss/muerte/muerte7_izquierda.png'),
                pygame.image.load('boss/muerte/muerte8_izquierda.png'),
                pygame.image.load('boss/muerte/muerte9_izquierda.png'),
                pygame.image.load('boss/muerte/muerte10_izquierda.png')
                

]
personaje_corriendo_atac_derecha=[
                                  pygame.image.load('soldado/caminar disparando/caminando1_derecha.png'),
                                  pygame.image.load('soldado/caminar disparando/caminando2_derecha.png'),
                                  pygame.image.load('soldado/caminar disparando/caminando3_derecha.png'),
                                  pygame.image.load('soldado/caminar disparando/caminando4_derecha.png'),
                                  pygame.image.load('soldado/caminar disparando/caminando5_derecha.png'),
                                  pygame.image.load('soldado/caminar disparando/caminando6_derecha.png'),
                                  pygame.image.load('soldado/caminar disparando/caminando7_derecha.png'),
                                  pygame.image.load('soldado/caminar disparando/caminando8_derecha.png')
                                  
] 
personaje_corriendo_atac_izquierda=[  
                                  pygame.image.load('soldado/caminar disparando/caminando1_izquierda.png'),
                                  pygame.image.load('soldado/caminar disparando/caminando2_izquierda.png'),
                                  pygame.image.load('soldado/caminar disparando/caminando3_izquierda.png'),
                                  pygame.image.load('soldado/caminar disparando/caminando4_izquierda.png'),
                                  pygame.image.load('soldado/caminar disparando/caminando5_izquierda.png'),
                                  pygame.image.load('soldado/caminar disparando/caminando6_izquierda.png'),
                                  pygame.image.load('soldado/caminar disparando/caminando7_izquierda.png'),
                                  pygame.image.load('soldado/caminar disparando/caminando8_izquierda.png')
                                  ]
          

personaje_ariba=[pygame.image.load('soldado/caminar/caminando1_izquierda.png'),
                pygame.image.load('soldado/caminar/caminando2_izquierda.png'),
                pygame.image.load('soldado/caminar/caminando3_izquierda.png'),
                pygame.image.load('soldado/caminar/caminando4_izquierda.png'),
                pygame.image.load('soldado/caminar/caminando5_izquierda.png'),
                pygame.image.load('soldado/caminar/caminando6_izquierda.png'),
                pygame.image.load('soldado/caminar/caminando7_izquierda.png')]
personaje_abajo=[ pygame.image.load('soldado/caminar/caminando1_izquierda.png'),
                pygame.image.load('soldado/caminar/caminando2_izquierda.png'),
                pygame.image.load('soldado/caminar/caminando3_izquierda.png'),
                pygame.image.load('soldado/caminar/caminando4_izquierda.png'),
                pygame.image.load('soldado/caminar/caminando5_izquierda.png'),
                pygame.image.load('soldado/caminar/caminando6_izquierda.png'),
                pygame.image.load('soldado/caminar/caminando7_izquierda.png')]

salta = [pygame.image.load('soldado/caminar/caminando6_derecha.png'),
                pygame.image.load('soldado/caminar/caminando7_derecha.png')]
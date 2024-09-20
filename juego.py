from personaje import Personaje
import random

nombre=input("""
¡Bienvenido a Gran Fantasía!
Por favor indique nombre de su personaje:
            """)


p= Personaje(nombre)

print(p.estado)

print("¡Oh no!, ¡Ha aparecido un Orco!")

o = Personaje("orco")

probabilidad_de_ganar=p.mostrar_probabilidad(o)

opcion_orco=Personaje.mostrar_dialogo_opcion(probabilidad_de_ganar)

while opcion_orco==1:
    resultado = "G" if random.uniform(0,1) < probabilidad_de_ganar else "P"
    if resultado=="G":
        print("""
¡Le has ganado al orco, felicidades!
¡Recibirás 50 puntos de experiencia!
            """)
        p.estado = 50
        o.estado =-30
    else:
        print("""
¡Oh no! ¡El orco te ha ganado!
¡Has perdido 30 puntos de experiencia!
            """)
        p.estado=-30
        o.estado=50
    print(p.estado)
    print(o.estado)
    
    probabilidad_de_ganar=p.mostrar_probabilidad(o)
    opcion_orco=Personaje.mostrar_dialogo_opcion(probabilidad_de_ganar)
print("¡Has huido! El orco ha quedado atrás.")

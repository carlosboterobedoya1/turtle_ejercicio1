posicion = 0 

def adelante(n):
    global posicion 
    print(" " * posicion + "-" * n + ">")
    posicion += n  

def abajo(n):
    global posicion
    vertical = posicion 
    if n >= 1: 
        print(" " * vertical + "|")
    if n >= 2:
        print(" " * vertical + "|")
    if n >= 3:
        print(" " * vertical + "|")
    if n >= 4:
        print(" " * vertical + "|")
    if n >= 5:
        print(" " * vertical + "|")
    print(" " * vertical + "V")

def reiniciar():
    global posicion
    posicion = 0  
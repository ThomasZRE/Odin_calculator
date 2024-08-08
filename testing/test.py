from math import floor

# cantidad
n = int(input())
while n > 0:
    p = float(input())
    treintapc = (p-(p * 0.30))*n
    tresPorDos = (p*2*floor(n/3)) + (n%3)*p
    if n < 3:
        print("Mejor oferta 30%:", round(treintapc))
    elif tresPorDos < treintapc:  
        print("Mejor oferta 3x2:", round(tresPorDos))
    elif tresPorDos > treintapc:
        print("Mejor oferta 30%:", round(treintapc))
    else:
        print("Mejor oferta 3x2:", round(tresPorDos))
    
    n = int(input())
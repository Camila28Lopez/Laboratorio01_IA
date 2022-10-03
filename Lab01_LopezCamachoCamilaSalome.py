import random

def MLaberinto(Num_Filas, Num_Colummnas, Num_Paredes,Num_Espacios):
    #laberinto con paredes
    laberinto = []
    for i in range(0,Num_Filas):
        fila=[]
        for j in range(0,Num_Colummnas):
            fila.append("#")
        laberinto.append(fila)
    for b in range(Num_Filas-1):
         print(laberinto[b])
        
    #laberinto con espacios 
    Num_espaciosG = 0
    fila_actual = random.randrange(Num_Filas)
    columna_actual =random.randrange(Num_Colummnas)
    print("Laberinto con espacios")
    #print(columna_actual)
    laberinto[fila_actual][columna_actual] = " "  
    Num_espaciosG = 1
    
    #laberinto[fila_actual][columna_actual] = "x" 
    
    #se genera el espacio 
    while Num_espaciosG < Num_Espacios:
        direccion = random.randrange(4)
    #Derecha
        if direccion == 0 and columna_actual < Num_Colummnas -1 :
            columna_actual = columna_actual + 1
       
    #ARRIBA   
        elif direccion == 1 and fila_actual  > 0:
            fila_actual = fila_actual - 1
      
    #IZQUIERDA   
        elif direccion == 2 and columna_actual > 0:
            columna_actual = columna_actual - 1
        
    #ABAJO     
        elif direccion == 3 and fila_actual  < Num_Filas -1 :
            fila_actual = fila_actual + 1
        if laberinto[fila_actual][columna_actual] == "#":
           laberinto[fila_actual][columna_actual] = " "
           Num_espaciosG = Num_espaciosG +1 
    for u in range(Num_Filas-1):
         print(laberinto[u])
   
    #se gerna el caracter   
    
    
    fila_actual_ficha = random.randrange(Num_Filas)
    columna_actual_ficha =random.randrange(Num_Colummnas)
    print("Laberinto con caracteres")
    laberinto[fila_actual][columna_actual] = "X" 
    Numx = 0
    #el caracter se mueve por los espacios de manera aleatria
    while Numx < Num_espaciosG/3:
        direccion = random.randrange(4)
    #Derecha
        if direccion == 0 and columna_actual_ficha < Num_Colummnas -1 :
            columna_actual_ficha = columna_actual_ficha + 1
    #IZQUIERDA   
        elif direccion == 2 and columna_actual_ficha > 0:
            columna_actual_ficha = columna_actual_ficha - 1
       
    #ARRIBA   
        elif direccion == 1 and fila_actual_ficha  > 0:
            fila_actual_ficha = fila_actual_ficha - 1
    #ABAJO     
        elif direccion == 3 and fila_actual_ficha  < Num_Filas -1 :
            fila_actual_ficha = fila_actual_ficha + 1
        if laberinto[fila_actual_ficha][columna_actual_ficha] == " ":
           laberinto[fila_actual_ficha][columna_actual_ficha] = "X"
           Numx = Numx + 1

    
    return laberinto

Num_Filas = int(input("Introducir el número de Filas  "))
Num_Colummnas = int(input("Introducir el número de Columas  "))
Num_Paredes = int(input("Introducir el número de Paredes  "))
Num_Espacios = (Num_Filas * Num_Colummnas) - Num_Paredes
print("...................................")
print(Num_Filas, Num_Colummnas, Num_Paredes, Num_Espacios)

laberintos = MLaberinto(Num_Filas, Num_Colummnas, Num_Paredes, Num_Espacios)

for fila in laberintos:
    print(fila)



 








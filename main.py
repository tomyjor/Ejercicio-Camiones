#Funcion para espaciar la tabla.
def separador(value):
    for i in range(value):
        print("")

# Funcion de burbujeo para ordenar las listas
def burbujeo(lista1, lista2,lista3,lista4):
    largo = len(lista1)
    desordenado = True
    while desordenado:
        desordenado = False
    for i in range(largo - 1):
         if lista2[i] > lista2[i + 1]:
                aux = lista2[i]
                lista2[i] = lista2[i + 1]
                lista2[i + 1] = aux
                aux = lista1[i]
                lista1[i] = lista1[i+1]
                lista1[i+1] = aux
                aux = lista3[i]
                lista3[i] = lista3[i + 1]
                lista3[i + 1] = aux
                aux = lista4[i]
                lista4[i] = lista4[i + 1]
                lista4[i + 1] = aux
                desordenado = True

# Funcion para calcular la distancia total recorrida

def distancia_total_recorrida():
    km1 = int(input("Cuantos KM son hasta su destino?"))
    while km1 <= 0:
        print("Error la distancia no puede ser negativa.")
        km1 = int(input("Cuantos KM son hasta su destino?"))
    km2 = int(input("Cuantos KM son hasta su retorno?"))
    while km2 <= 0:
        print("Error la distancia no puede ser negativa")
        km2 = int(input("Cuantos KM son hasta su retorno?"))
    distancia_total = km1 + km2
    if distancia_total>0:
        return distancia_total



# Funcion para calcular el tiempo promedio

def tiempo_promedio(velocidad, distancia):
    dias = 0
    horas = (velocidad // distancia)
    if horas >= 24:
        divisor = horas//24 #34//24 = 1.416666666
        horas = horas-24*divisor # 34-33.84 = 0.16
        dias = dias+1*divisor
    return dias,horas

# Programa Principal

seleccione_camion = int(input("Coloce el ID de su camion, o coloque -1 para finalizar"))
lista_id = []
lista_km = []
lista_carga = []
lista_tiempo = []
a = 1
b = 0
distancia_total = 0
recorrido_acumulado = 0
while seleccione_camion > 0:
    if seleccione_camion != 0:
        lista_id.append(seleccione_camion)

    while seleccione_camion != -1:
        seleccione_camion = int(input("Coloque el ID de su camion, o coloque -1 para finalizar"))
        if seleccione_camion != -1:
            lista_id.append(seleccione_camion)

    for i in range(len(lista_id)):
        print("Camionero", lista_id[i], "...")
        distancia_total = distancia_total_recorrida()
        print("Camionero", lista_id[i], "...")
        carga = int(input("¿Cuanta carga lleva? Por favor ingresar en Toneladas."))
        while carga < 0:
            print("La carga no puede ser negativa.")
            carga=int(input("¿Cuanta carga lleva? Por favor ingresar en Toneladas"))
        print("Camionero", lista_id[i], "...")
        velocidad = int(input("Cual es la velocidad promedio?"))
        while velocidad <= 0:
            print("La velocidad no puede ser nula o negativa.")
            velocidad=int(input("Cual es la velocidad promedio."))
        lista_km.append(distancia_total)
        lista_carga.append(carga)
        lista_tiempo.append(tiempo_promedio(distancia_total,velocidad))
        a = a + 1

    burbujeo(lista_id, lista_carga,lista_km,lista_tiempo)

    separador(20)
    print("|","Identificacion", "|" ,"Carga", "|" ,"Recorrido",  "|"   ,"Tiempo promedio. (dias,horas)")
    print("-------------------------------------------------------------------------------------------")
    separador(1)

    while b != len(lista_id):
        if lista_km[b] >= 20000:
            print("|     ",lista_id[b],"    |    " ,lista_carga[b],"TN  |    ",lista_km[b],"KM       |"
                ,lista_tiempo[b], "| FUERA DE SERVICIO")
            separador(1)
        else:
            print("|     ",lista_id[b],"    |    " ,lista_carga[b],"TN  |    ",lista_km[b],"KM       |",lista_tiempo[b])
            separador(1)
        b = b+1


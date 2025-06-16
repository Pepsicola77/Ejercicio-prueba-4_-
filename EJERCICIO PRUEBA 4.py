import re
Stockconcepcion=500
StockPuentealto=1300
StockMuelleBaron=100
StockMuelleVergara=50

EntradasVendidasConcepcion=[]
EntradasVendidasPuentealto=[]
EntradasVendidasMuelleBaron=[]
EntradasVendidasMuelleVergara=[]

def comprar_entradaConcepcion():
    global Stockconcepcion
    if Stockconcepcion  <= 0:
        print("Lo sentimos, no hay stock diponible en Concepción")
        return
    nombre_comprador=str(input("Ingrese su nombre para realizar la compra:"))
    for nombre in EntradasVendidasConcepcion:
        if nombre["Nombre"]==nombre_comprador:
            print("Este nombre ya está registrado")
            return
    while True:   
            print("Debe de crear su código de confirmación")
            print("Este debe tener mínimo 6 caracteres, 1 mayúscula, 1 número y no puede tener espacios vacios")
            codigo_confirmacion=input("Ingrese su codigo a crear: ")
            if len(codigo_confirmacion)<=6 and re.search(r"[A-Za-z]", codigo_confirmacion) and re.search(r"\d",codigo_confirmacion) and re.search(r"\s",codigo_confirmacion) and not re.search("\s", codigo_confirmacion):
             print("Contraseña válidada")
             break
            else:
                print("Codigo no válido, porfavor intentelo otra vez")
    
    Datoscompraconcepcion={"Nombre": nombre_comprador, "Codigo de confirmación": codigo_confirmacion}
    EntradasVendidasConcepcion.append(Datoscompraconcepcion)
    print("Su compra se ha realizado con éxito")
    Stockconcepcion-=1

def comprar_entradaPuentealto():
    global StockPuentealto
    if StockPuentealto <=0:
        print("Lo sentimos, no hay stok disponible en Puente alto")
        return
    nombre_comprador2=str(input("Ingrese su nombre para realizar la compra: "))
    for nombre in EntradasVendidasPuentealto:
        if nombre["Nombre"]==nombre_comprador2:
            print("Este nombre ya está registrado")
            return
    
    while True:
     try:
      print("La cantidad de entradas máxima que usted puede comprar es de 3")
      cantidad_de_entradas=int(input("Ingrese la cantidad de entradas que usted comprará "))
      if cantidad_de_entradas > 3:
          print("No puede comprar más de entradas")
      else:
          break
     except ValueError:
         print("Ingrese un dato númerico!!!")
    
    DatoscompraPuentealto={"Nombre registrado": nombre_comprador2, "Cantidad de entradas": cantidad_de_entradas}
    EntradasVendidasPuentealto.append(DatoscompraPuentealto)
    StockPuentealto-=1
    
def comprar_entradaMuellebaron():
    global StockMuelleBaron
    if StockMuelleBaron <= 0:
        print("Lo sentimos no hay stock disponible en esta localidad.")
        return
    nombre_comprador3=str(input("Ingrese su nombre "))
    for nombre in EntradasVendidasMuelleBaron:
        if nombre["Nombre"]==nombre_comprador3:
            print("Este nombre ya está registrado")
            return
    tipoentrada=str("G")
    while True:   
            print("Debe de crear su código de confirmación")
            print("Este debe tener mínimo 6 caracteres, 1 mayúscula, 1 número y no puede tener espacios vacios")
            codigo_confirmacion=input("Ingrese su codigo a crear: ")
            if len(codigo_confirmacion)<=6 and re.search(r"[A-Za-z]", codigo_confirmacion) and re.search(r"\d",codigo_confirmacion) and re.search(r"\s",codigo_confirmacion) and not re.search("\s", codigo_confirmacion):
             print("Contraseña válidada")
             break
            else:
                print("Codigo no válido, porfavor intentelo otra vez")
    DatoscompradorBaron={"Nombre": nombre_comprador3, "Tipo entrada": tipoentrada}
    EntradasVendidasMuelleBaron.append(DatoscompradorBaron)
    print("Su compra ha sido realizada con exito")
    StockMuelleBaron-=1

def comprar_entradasMuelleVergara():
    global StockMuelleVergara
    if StockMuelleVergara <= 0:
        print("No hay stock disponible en esta localidad, lo sentimos.")
        return
    nombre_comprador4=str(input("Ingrese su nombre para comprar: "))
    for nombre in EntradasVendidasMuelleVergara:
        if nombre["Nombre"]==nombre_comprador4:
            print("Este nombre ya está registrado!!, intente con otro")
            return
    print("¿De que tipo entrada será su compra?")
    print("Sunset (SUN) o Night (NI)")
    tipo_de_entrada2=str(input("Ingrese su respuesta: ")).upper()
    if tipo_de_entrada2=="SUN":
        print("Su tipo de entrada será Sunset")
    elif tipo_de_entrada2=="NI":
        print("Su tipo de entrada será Night")
    else:
        print("Error, tipo de entrada no válida")
        return
    Datoscompravergara={"Nombre":nombre_comprador4, "Tipo de entrada": tipo_de_entrada2}
    EntradasVendidasMuelleVergara.append(Datoscompravergara)
    StockMuelleVergara-=1
    print("Su comprar ha sido realizada")

def main():
    while True:
        print("TOTEM AUTOSERVICIO GIRA LOS FORTIFICADOS ROCK AND CHILE IN CHILE")
        print("1.-Comprar entrada en Concepción")
        print("2.-Comprar entrada en Puente Alto")
        print("3.-Comprar entrada en Muelle Barón")
        print("4.-Comprar entrada en Muelle Vergara, Viña del mar")
        print("5.-Salir del Totem Autoservicio")

        opcion=input("Elija una opción: ")

        if opcion=="1":
            comprar_entradaConcepcion()
        elif opcion=="2":
            comprar_entradaPuentealto()
        elif opcion=="3":
            comprar_entradaMuellebaron()
        elif opcion=="4":
            comprar_entradasMuelleVergara()
        elif opcion=="5":
            print("Usted está saliendo del Totem Autoservicio, tenga un excelente día.")
            break
        else:
            print("Ingrese una opción válida!!!!")

main()




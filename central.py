from fabrica import crearPieza, agregarPieza, mostrarPedido

lista=[]

#Pedir datos por teclado
id=int(input("Digita el id: "))

#Llamar a la funcion que crea la pieza
pieza=crearPieza(id, "abcd001", "plato maravilloso", 50000, 100, 10, "1/4/2025")

#Llamar a la funcion que agrega la pieza a la lista
agregarPieza(lista, pieza)

#Llamar a la funcion que muestra la lista
mostrarPedido(lista)
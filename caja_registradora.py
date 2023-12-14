#Definiendo productos
precio = {
    "manzana" : 5,
    "leche" : 50,
    "carne" : 70,
    "pan" : 15,
    "huevos" : 60
    }

#Solicitando articulos
respuesta = input("Quieres agregar productos? si/no: ").lower()
if respuesta == "si":
    producto = input("Que producto llevaras? ").lower()
    precioProductoSeleccionado = (precio.get(producto))
    producto = producto.capitalize()
    cantidad = int(input("Cuantas llevaras? "))
    subtotal = (precioProductoSeleccionado) * cantidad
    iva = float(subtotal * 0.08)
    total = float(subtotal + iva)
    print ("-----------------")
    print("Producto", end=" ")
    print("Cantidad", end=" ")
    print("Precio")
    print(producto, end="      ")  
    print(cantidad, end="      ")
    print("$", precioProductoSeleccionado)
    print ("-----------------")
    print("Subtotal: $", subtotal)
    print ("-----------------")
    print("IVA 8%: $", iva)
    print ("-----------------")
    print("Total: $", total)
    print ("-----------------")
else :
    print("Gracias por su visita")
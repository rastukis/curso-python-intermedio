my_list = ["strings", 15, 15.6, True]

my_date = "2018-01-01 12:00:00 123456"

# Obtener Primeros elementos
print("Primeros elementos")
print(my_date[:4])

# Quitar primeros elementos
print(my_date[4:])

# Obtener los ultimos n-elementos
print(my_date[-6:])

# Eliminar los utlimos n-elementos
print(my_date[:-6])


my_list.append(6) # Agrega un valor al final de la lista
my_list.insert(1, "insert") # Agrega un valor en la posicion especificada
my_list.remove(15) # Elimina todos los valores que sean igual al argumento
my_list.pop() # Elimina el ultimo numero, regresa el valor eliminado

# my_list.sort() Ordena la lista, puede tener como parametro reverse = True


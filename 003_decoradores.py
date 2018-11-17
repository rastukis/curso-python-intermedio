def decorador(func):
    def nueva_funcion(*args, **kwargs):
        print("Vamos a ejecutar la funcion")
        func(*args, **kwargs)
        print("Se ejecuto la función")

    return nueva_funcion

@decorador
def saluda():
    print("Hola Mundo")

@decorador
def suma(num_uno, num_dos):
    print(num_uno + num_dos)

suma(12, 53)
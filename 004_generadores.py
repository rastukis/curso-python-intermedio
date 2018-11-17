def generadorPares(limite):
    num = 1

    while num < limite:
        yield num*2
        num += 1

num_pares = generadorPares(10)

"""
for i in num_pares:
    print(i)
"""

print(next(num_pares))

print("Aquí podría ir mas código")

print(next(num_pares))
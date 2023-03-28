# funcines lambda
# def suma(a, b):
#     return a + b
#
#
# lam_f = lambda numero1, numero2: (numero1 + numero2)
#
# print(suma(1, 2))
# print(lam_f("hola ", "mundo"))


# filters
def multiplo(numero):
    if numero % 5 == 0:
        return True
    return False
numeros = [2, 5, 10, 11, 12]

# print(list(filter(multiplo, numeros)))
#
# mul_lambda = lambda numero: (True if numero % 5 == 0 else False)
# print(list(filter(mul_lambda, numeros)))

# maps
print(list(map(lambda a: (a * 2), numeros)))

nombres = ["Luis", "Pedro", "Juan"]

print(list(map(lambda nombre: nombre + "@meli.com.co", nombres)))




# generator
from time import sleep


# def build_list(numero_elementos: int):
#     lista = []
#     for l in range(0, numero_elementos):
#         lista.append(l)
#     return lista
#
#
# def build_list_generator(numero_elementos: int):
#     while numero_elementos != 0:
#         yield numero_elementos
#         numero_elementos -= 1
#
#
# print(build_list(5))
# # print(list(build_list_generator(5)))
#
# gen_f = build_list_generator(50)  # generator
# # print(next(gen_f))
# # print(next(gen_f))
# # print(next(gen_f))
#
# for g in gen_f:
#     print(g)

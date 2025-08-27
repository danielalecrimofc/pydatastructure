import timeit
#Função 1
# Vai executar 11 passos se por exemplo eu colocar 10 como entrada
# O(n)
# A quantidade de passos depende do valor de entrada
def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma

print("Função 1:")
print(timeit.timeit("soma1(10)", globals=globals(), number=1))

# Função 2
# Vai executar 3 passos sempre independente do valor de entrada
# O(3)

def soma2(n):
    return (n * (n + 1)) / 2

print("Função 2:")
print(timeit.timeit("soma2(10)", globals=globals(), number=1))

import timeit
def lista1():
    lista = []
    for i in range(1000):
        lista += [i]
    return lista

print(timeit.timeit("lista1()", globals=globals(), number=1))

def lista2():
    return range(1000)

print(timeit.timeit("lista2()", globals=globals(), number=1))
#l = lista2()

#for i in l:
#    print(i)
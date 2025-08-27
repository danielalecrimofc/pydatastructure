#Constante - O(1)
lista = [1,2,3,4,5]

def constant(n):
    print(n[0])
    print(n[1])

constant(lista)

#Linear - O(n) / Depende do valor de n

def linear(n):
    for i in n:
        print(i)

linear(lista)

# Quadratic - O(n^2) - polynomial

def quadratic(n):
    for i in n:
        for j in n:
            print(i,j)
        print('-----')

quadratic(lista)

#Combination

# O(1) + O(5) + O(n) + O(n) + O(3)
# O(9) + O(2n) ou apenas O(n)
def combination(n):
    # O(1)
    print(n[0])

    # O(5)
    for i in range(5):
        print('test',1)

    # O(n)
    for i in n:
        print(i)
        
    # O(n)
    for i in n:
        print(i)

    # O(3)
    print('Python')
    print('Python')
    print('Python')

combination(lista)
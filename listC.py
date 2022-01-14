#list comprehension
x = [1, 2, 3, 4, 5]
y = []
for i in x:
    y.append(i**2) #adicionar cada valor ao quadrado
print(x)
print(y)
#valor a adicionar + laço + condição
a = [6, 7, 8, 9, 10]
b = [i**2 for i in a]
print (a)
print (b)
#só os número impares
z = [i for i in a if i%2 == 1]
print (z)


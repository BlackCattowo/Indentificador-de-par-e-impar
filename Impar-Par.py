n = int(input("Quantidade de números a serem analisados: "))

total = 0
par = 0
while n > 0:
    total += 1
    x = int(input())
    if x % 2 == 0:
        par += 1
    n -= 1

impar = total - par
print(par, "numeros são pares")
print(impar, "números são impares")
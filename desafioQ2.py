import math

def primo(n):

    primos = []
    if n >= 2:
        for i in range(2, n + 1):
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    break
            else:
                primos.append(i)
    return primos

def primo_recursivo(n):

    if n < 2:
        return []
    if n == 2:
        return [2]

    primos = primo_recursivo(n - 1)
    limite = int(math.sqrt(n))
    
    eh_primo = True
    for p in primos:
        if p > limite:
            break
        if n % p == 0:
            eh_primo = False
            break

    if eh_primo:
        primos.append(n)

    return primos

def main():
    while True:
        try:
            n = int(input("Digite um número inteiro positivo: "))
            if n <= 0:
                raise ValueError("O número deve ser um inteiro positivo.")
            break
        except ValueError as e:
            print("Erro:", e)

    print("P(%d) = %s" % (n, primo(n)))
    print("P(%d) = %s" % (n, primo_recursivo(n)))
main()

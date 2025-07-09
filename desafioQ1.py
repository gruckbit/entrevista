def fib(n):
    termo1, termo2 = 0, 1
    if n == 1:
        return termo1
    elif n == 2:
        return termo2
    elif n > 2:
        for i in range(2, n):
            termoN = termo1 + termo2
            termo1, termo2 = termo2, termoN
    return termo2

def fib_recursivo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_recursivo(n - 1) + fib_recursivo(n - 2)

def main():
    while True:
        try:
            n = int(input("Digite um número inteiro positivo: "))
            if n <= 0:
                raise ValueError("O número deve ser um inteiro positivo.")
            break
        except ValueError as e:
            print("Erro:", e)

    print("Fib(%d) = %d" % (n, fib(n)))
    print("Fib(%d) = %d" % (n, fib_recursivo(n)))

main()


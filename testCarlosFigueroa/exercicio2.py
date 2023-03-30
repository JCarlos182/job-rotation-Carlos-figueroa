def verifica_fibonacci(num):
    a = 0
    b = 1
    while b < num:
        c = a + b
        a = b
        b = c
    if b == num:
        print(num, "pertence à sequência de Fibonacci!")
    else:
        print(num, "não pertence à sequência de Fibonacci.")



def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 10  # Chcemy obliczyć 10 wyraz
wynik = fibonacci(n)
print(f"Wyraz ciągu Fibonacciego dla n = {n} to {wynik}")
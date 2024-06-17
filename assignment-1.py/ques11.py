def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence


num_terms = 10  # Change this number to adjust the number of Fibonacci terms to generate
fib_sequence = fibonacci(num_terms)
print(f"The Fibonacci sequence up to {num_terms} terms:")
print(fib_sequence)
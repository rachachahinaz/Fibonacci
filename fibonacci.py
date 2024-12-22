def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b

    return sequence

# Example usage:
num = int(input("Enter the number of terms for the Fibonacci sequence: "))
print(f"The first {num} numbers of the Fibonacci sequence are: {fibonacci_sequence(num)}")
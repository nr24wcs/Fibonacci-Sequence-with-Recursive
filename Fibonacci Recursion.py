def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_sequence_recursive(count):
    sequence = []
    for i in range(count):
        sequence.append(fibonacci_recursive(i))
    return sequence

try:
    num = int(input("Enter your number here: "))
    if num <= 0:
        print("please enter a postive number: " ) 
    else: 
        print("Fibonacci sequence is: ")
        print(fibonacci_sequence_recursive(num))
except ValueError:
    print("Please Try again with a valid number!")
# Simple Calculator in Python.

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Division by zero not allowed"

print("Addition:", add(10, 5))
print("Subtraction:", sub(10, 5))
print("Multiplication:", mul(10, 5))
print("Division:", div(10, 5))
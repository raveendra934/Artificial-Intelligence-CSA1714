

data = [
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 0],
    [0, 0, 0]
]

a = int(input("Enter first value (0 or 1): "))
b = int(input("Enter second value (0 or 1): "))

if a == 1:
    result = 1
else:
    result = 0

print("Predicted class:", result)

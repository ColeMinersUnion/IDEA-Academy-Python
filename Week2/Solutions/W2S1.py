
"""
For Loops
print a pyramid of starts thats n levels high
"""

input_height = int(input("Enter the height of the pyramid: "))
for i in range(1, input_height + 1):
    # Print leading spaces
    for j in range(input_height - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    # Move to the next line
    print()


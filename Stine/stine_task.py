"""
Stine - Exercise: Check Even or Odd

Goal:
- Complete the function so it returns True if the number is even.
- Return False if the number is odd.
"""


def is_even(number):
    # TODO: Return True for even numbers, otherwise False
    # Hint: use the modulo operator (%)
    if number % 2 == 0:
        return True
    else:
        return False


# Test case for Stine
test_number = 10
print("Expected: True")
print("Actual:", is_even(test_number))


def ansatt(name):
    if name == "Erik":
        return "GitComitt Kongen"
    elif name == "Stine":
        return "Aspiring GitComitt ninja"

print (ansatt("Erik"))
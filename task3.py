#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""

while True:
    a = float(input("Gimme a number: "))

    if a % 2 == 0:
        print("It is an even integer!")
        break

    print("It is not an even integer!")
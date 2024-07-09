
"""
HANDSHAKE CHALLENGE

You will need to:
- Write a function that takes an integer for the number of people and returns an integer with the number of handshakes
- Validate if a handshake can occur given X as an input
- Identify an error state and throw a custom exception
- Create a test file for the function and create a comprehensive test suite

"""


def no_of_handshakes(no_people):
    if no_people < 2:
        return 0
    return no_people * (no_people - 1) // 2
    pass

try:
    no_people = int(input("How many people would like to shake hands? "))
    if no_people < 2:
        print("A handshake requires at least 2 people.")
    else:
        print(f"The number of handshakes for {no_people} people is: {no_of_handshakes(no_people)}")
except ValueError:
    print("Invalid input, please enter an integer value.")

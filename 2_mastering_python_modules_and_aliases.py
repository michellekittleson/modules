'''
Task 1: Custom Module with Aliases

Create a custom module named 'text_utils.py' with functions for string manipulation (e.g., reversing a string, capitalizing). In your main script, import this module using an alias and utilize its functions.

Your main script should be able to use the functions from 'text_utils.py' via an alias, demonstrating an understanding of custom module creation and aliasing.

'''

import text_utils as tu

def main():
    while True:
        s = input("What is the string you would like to change? ")
        choice = input("\nWould you like to...\n1. Reverse the string, or...\n2. Capitalize the string?\n3. Exit\n")
        if choice == '1':
            tu.reverse_string(s)
        elif choice == '2':
            tu.capitalize_string(s)
        elif choice == '3':
            print("Exiting program. Have a great day!")
            break
        else:
            print("Please enter '1' or '2'.")

main()

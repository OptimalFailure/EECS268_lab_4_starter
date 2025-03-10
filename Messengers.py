"""
This file provides standardized functions for I/O to allow automatic 
checks for code correctness. Your GTA will still examine your code to
make sure it correctly uses recrsion and is appropriately documented.

You should NOT modify ANY code in this file.
"""

class Ex1Messenger:
    def request_base(self) -> str:
        """Request the base from the user with appropriate message. This function does NOT modify or validate the string"""
        return input("Enter a base: ")

    def request_power(self) -> str:
        """Request the power from the user with appropriate message. This function does NOT modify or validate the string"""
        return input("Enter a power: ")
    
    def print_answer(self, result:int) -> None:
        """Display the calculated answer in appropriate format"""
        print(f"Answer: {result}")
    
    def warn_exponent_out_of_range(self) -> None:
        """Print the appropriate warning for a negative exponent"""
        print("Sorry, your exponent must be zero or larger.")

    def warn_invalid_type(self) -> None:
        """Print the appropriate warning for a invalid base/exponent type"""
        print("Sorry, base and exponent must be ints.")
    

class Ex2Messenger:
    def request_sick_count(self) -> str:
        """Request the day from the user with appropriate message. This function does NOT modify or validate the string"""
        return input("OUTBREAK!\nWhat day do you want a sick count for?: ")
    
    def print_sick_count(self, count:int) -> None:
        """Display the calculated answer in appropriate format"""
        print(f"Total people with flu: {count}")

    def warn_invalid_day(self) -> None:
        """Print the appropriate warning for an invalid day"""
        print("Invalid day")
    

class Ex3Messenger:
    def request_mode_and_value(self) -> str:
        """Request the mode and value from the user with appropriate message. This function does NOT modify or validate the string"""
        return input("Enter mode and value: ") 
    
    def print_number(self, num:int) -> None:
        """Print a fibonacci number in the appropriate format"""
        print(num)
    
    def print_verification(self, num:int, isInSequence:bool) -> None:
        """Print whether or not a number is a fibonacci number, in the appropriate format"""
        res = "is" if isInSequence else "is not"
        print(f"{num} {res} in the sequence")

    def warn_invalid_flag(self) -> None:
        """Print the appropriate warning for invalid flag"""
        print("Invalid input. Flag must be -i or -v")

    def warn_invalid_num(self) -> None:
        """Print the appropriate warning for invalid number"""
        print("Invalid input. With -i flag, number must be an integer >= 0")


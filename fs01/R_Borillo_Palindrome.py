#Code written by: Raphael Jedidiah R. Borillo | BCS22 | 202230704 | S-ITCS214LA
#Date written: November 16, 2023

import time

# defines the main function of the program
def main():

# prints out the display interface of the program
    print("""
                                    PALINDROME CHECKER
============================================================================================================
||                                                                                                        ||
|| [1]. Run Palindrome Checker                                                                            ||
|| [2]. End Program                                                                                       ||
||                                                                                                        ||
============================================================================================================
""")

# gets user input
    op = int(input("Please input the NUMBER of your option here: \n-> "))
# while loop for menu iteration
    while True:
        if op == 1:
            # user input for palindrome
            print("=================================================")
            upalinput = input("Please input your word/phrase/sentence here: ")
            print("=================================================")
            # sets 'palindrome' to the Stack class and calls corresponding functions to analyze the input.
            palindrome = Stack(upalinput.lower())
            # prints user's original input
            print(f"Original Sentence: {upalinput}")
            time.sleep(0.5)
            # Stack class function calls
            palindrome.clean()
            palindrome.reverse()
            palindrome.display()
            time.sleep(0.5)
            print("Checking...")
            time.sleep(1.5)
            print(palindrome.check())
            # User input to repeat program
            userin = input("Check another palindrome? [Y/N] \n")
            if userin.lower() == "y":
                print("Returning to program...")
                time.sleep(1.5)
                main()
            elif userin.lower() == "n":
                # User input to confirm exit of program
                usercon = input("Exit program? [Y/N] \n")
                if usercon.lower() == "y":
                    print("Exiting program...")
                    time.sleep(3)
                    break
                elif usercon.lower() == "n":
                    print("Returning to program...")
                    time.sleep(1.5)
                    main()
            else:
                "Invalid input!"
        # User input to exit program
        elif op == 2:
            print("Exiting program...")
            time.sleep(3)
            break
        else:
            print("invalid input")
            main()

class Stack:
    # parameter definitions
    def __init__(self, palin):
        self.palin = palin
        self.revlist = []
        self.cleanlist = []
        self.top = -1

    # determines whether input is empty
    def empty(self):
        if self.top == -1:
            return f"There is no input."

    # reverses the cleaned input.
    def reverse(self):
        if not self.empty():
            while not self.empty():
                popped_element = self.cleanlist[self.top]
                self.top -= 1
                self.revlist.append(popped_element)
        else:
            return "Stack Underflow"

    # cleans the input (aka, removes all numbers, symbols, and spaces)
    def clean(self):
        valid_chars = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
        valid_num = '123456789'
        for x in self.palin:
            if x in valid_chars:
                self.top += 1
                self.cleanlist.append(x)
            elif x in valid_num:
                self.top += 1
                self.cleanlist.append(x)

    # checks to see if reversed input matches the cleaned input and displays result accordingly.
    def check(self):
        if self.cleanlist == self.revlist:
            return f"The input '{self.palin}' is a palindrome."
        elif self.cleanlist != self.revlist:
            return f"The input '{self.palin}' is not a palindrome."

    # displays the cleaned and reversed inputs.
    def display(self):
        time.sleep(0.7)
        print(f"Cleaned Sentence: {''.join(self.cleanlist)}")
        time.sleep(0.7)
        print(f"Reversed Sentence: {''.join(self.revlist)}")

# main code execution
print("Running program...")
time.sleep(2)
print("Hello! This is Palindrome Checker, a program that checks if your input is considered a palindrome!")
time.sleep(1)
main()

#Reflection:
'''
I think this code was pretty fun to create. It was definitely a challenge implementing it, 
since I'm not really used to working with stacks yet, so I didn't really know how to implement stacks
into the other functions I used.

However, after a few hours of work, I was finally able to understand the bugs in my code and
was able to debug properly. 

I plan to add on more to this code, however I am satisfied with the current version, as it works
properly. Although it can be further optimized, I don't think that my current skill set and the
time of the deadline will allow me to further modify the code without breaking it. 

I will, however, tinker with it
in my free time.
'''

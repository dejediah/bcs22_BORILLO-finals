def main():
    x = True
    print("""
                                    PALINDROME CHECKER
============================================================================================================
||                                                                                                        ||
|| [1]. Run Palindrome Checker                                                                            ||
|| [2]. End Program                                                                                       ||
||                                                                                                        ||
============================================================================================================
""")
    op = int(input("Please input the NUMBER of your option here: \n-> "))
    while x is True:
        if op == 1:
            print("=================================================")
            upalinput = input("Please input your word/phrase/sentence here: ")
            print("=================================================")
            palindrome = Stack(upalinput)
            print(f"Original Sentence: {upalinput}")
            palindrome.clean()
            palindrome.reverse()
            palindrome.display()
            print(palindrome.check())
            main()
        elif op == 2:
            print("Exiting program...")
            x = False
        else:
            print("invalid input")
            main()

class Stack:
    def __init__(self, palin):
        self.palin = palin
        self.revlist = []
        self.cleanlist = []
        self.top = -1

    def empty(self):
        if self.top == -1:
            return f"There is no input."

    def reverse(self):
        if not self.empty():
            while not self.empty():
                popped_element = self.cleanlist[self.top]
                self.top -= 1
                self.revlist.append(popped_element)
        else:
            return "Stack Underflow"

    def clean(self):
        for x in self.palin:
            if x.isalpha():
                self.top += 1
                self.cleanlist.append(x)

    def check(self):
        if self.cleanlist == self.revlist:
            return f"The input '{self.palin}' is a palindrome."
        elif self.cleanlist != self.revlist:
            return f"The input '{self.palin}' is not a palindrome."

    def display(self):
        print(f"Cleaned Sentence: {''.join(self.cleanlist)}")
        print(f"Reversed Sentence: {''.join(self.revlist)}")


main()

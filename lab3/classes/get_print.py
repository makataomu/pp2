class StringGetter():

    def __init__(self) -> None:
        self.string = ""
    
    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper()) 


string_getter = StringGetter()
string_getter.getString()
string_getter.printString()

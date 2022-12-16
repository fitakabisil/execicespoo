class StringFoo:
    def __init__(self):
        self.string = input("quel est l'objet?")

    def set_string(self, string):
        self.string = string

    def print_string(self):
        print(self.string.upper())


StringFoo().print_string()

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def difference(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        # TODO:- Add your code in the below function
        # check for divide by zero error, using assert statements
        # implement the division operation
        # adding different implementation
        try:
            return self.a / self.a
        except ZeroDivisionError:
            print("[ERROR] Can't divide by zero!")
            
    def square(self):
        return self.a * self.a
    
    def modulo(self):
        pass
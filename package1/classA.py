#2. Create a class with PROTECTED fields and methods. Access these fields and methods
#from any other class in the same package.
#Also, Access the PROTECTED fields and methods from child class located in a different
#package
#Access the PROTECTED fields and methods from any class in different package
class A:
    def __init__(self):
        self._protected_var = "I am PROTECTED variable"

    def _protected_method(self):
        print("I am PROTECTED method")

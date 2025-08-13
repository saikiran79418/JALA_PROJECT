from package1.classA import A

class B(A):  # Child class in different package
    def access_protected(self):
        print("From child class in different package:")
        print(self._protected_var)
        self._protected_method()
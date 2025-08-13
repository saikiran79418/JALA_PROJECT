from package1.classA import A
from package2.classB import B

print("--- Accessing from same package ---")
objA = A()
print(objA._protected_var)   # Works (same package)
objA._protected_method()

print("\n--- Accessing from child class in different package ---")
objB = B()
objB.access_protected()

print("\n--- Accessing from non-child class in different package ---")
objA2 = A()
print(objA2._protected_var)   # Works (but not recommended)
objA2._protected_method()

#output
#C:\protect\.venv\Scripts\python.exe C:\protect\main.py
#--- Accessing from same package ---
#I am PROTECTED variable
#I am PROTECTED method

#--- Accessing from child class in different package ---
#From child class in different package:
#I am PROTECTED variable
#I am PROTECTED method

#--- Accessing from non-child class in different package ---
#I am PROTECTED variable
#I am PROTECTED method

#Process finished with exit code 0

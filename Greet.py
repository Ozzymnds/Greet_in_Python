class MyClass:
    def __init__(self, name):
        # Constructor method that initializes the instance variable 'name'
        self.name = name

    def greet(self):
        # Method to print a greeting with the object's name
        print("Hello", self.name)

def main_function():
    # Create an instance of the MyClass class
    obj = MyClass(input("Your name: "))

    # Call the greet method of the instance
    obj.greet()

if __name__ == "__main__":
    # Call the main function when the script is executed directly
    main_function()

"""
In this example, we've defined a class named "MyClass" that has a special method __init__ (constructor) 
and another method named "greet". 
The __init__ method is automatically called when an object of the class is created and 
is used to initialize instance variables. The "greet" method simply prints a greeting with the object's name.
Then, we've defined a function named "main_function" that creates an instance of the "MyClass" class and 
calls its "greet" method.

Finally, we use the if __name__ == "__main__" block to ensure that the code inside that block 
only runs when the file is executed directly (not when it's imported as a module). 
In this case, we call the main function.
"""

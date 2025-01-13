glossary = {
    "Variable": "Variable is a reserved memory location to store values. In other words, a variable in a python program gives data to the computer for processing.",
    "List": "List is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.",
    "if statements": "if statement is a condition statement used to check a condition, and execute it if the condition holds true.",
    "Dictionary": "A dictionary in Python is a collection of key-value pairs. The dictionary keys must be unique.",
    "Loops": "Looping means repeating something over and over until a particular condition is satisfied.",
    "Parameters":"Parameters are variables that are defined in the function definition. They are used to receive and store arguments passed to a function at the call time.",
    "Tuple":"A tuple is an ordered and immutable collection written with round brackets. It can contain a mix of objects.",
    "Global":"Global keyword allows you to change a variable value outside of its current scope.",
    "del":"Python's del statement is used to delete variables and objects in the Python program.",
    "return":"In Python (and in many other programming languages), the purpose of the return statement is to send a value back to the part of the program that called the function."
}

for term, definition in glossary.items():
    print(term+": "+definition)
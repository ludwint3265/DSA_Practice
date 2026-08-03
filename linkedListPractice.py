'''
linked lists + OOP Python practice

Problem 1: Pokemon Class
Step 1: Copy the following code into your IDE.

Step 2: Add a line of code (outside of the class) to instantiate an instance of the class Pokemon and
store it in a variable named my_pokemon. The Pokemon instance created should have name "Pikachu" and its 
types should be ["Electric"].

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

'''
print("Question 1:\n")
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False


my_pokemon = Pokemon("Pikachu", ["Electric"])
print(my_pokemon.name, my_pokemon.types)
print("\n")

'''
Problem 2: Create Squirtle
Step 1: Add the print_pokemon definition below to your code on your IDE.

def print_pokemon(self):
   print({
      "name": self.name,   
      "types": self.types, 
      "is_caught": self.is_caught 
   })

Step 2: Instantiate an instance of the class Pokemon and store it in a variable named squirtle. The Pokemon instance created should have name "Squirtle" and its types should be ["Water"].

Step 3: Call the method print_pokemon() on your new Pokemon instance squirtle.

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False
'''

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
         print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
         })

print("Question 2:\n")
squirtle = Pokemon("Squirtle", ["Water"])
squirtle.print_pokemon()
print("\n")

'''
Problem 3: Is Caught
Using your code from Problem 2, update your squirtle Pokemon so that is_caught is updated to True. Use the print_pokemon() function to verify that squirtle's is_caught property was updated.

Expected Output:

{
    "name": "Squirtle",
    "types": ["Water"],
    "is_caught": True
}
'''

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
         print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
         })

print("Question 3:\n")
squirtle2 = Pokemon("Squirtle", ["Water"])
squirtle2.is_caught = True
squirtle2.print_pokemon()
print("\n")

'''
Problem 4: Catch Pokemon
Update the Pokemon class with a new method catch() that takes in no parameters except self.

The method should update the Pokemon's is_caught attribute to True and not return any value.

class Pokemon():
	...
	
	def catch(self):
		pass
Example Usage:

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.catch()
my_pokemon.print_pokemon()
Example Output:

{'name': 'rattata', 'types': ['Normal'], 'is_caught': False} # First print statement
{'name': 'rattata', 'types': ['Normal'], 'is_caught': True}  # Second print statement
'''

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
         print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
         })

    def catch(self):
        self.is_caught = True

print("Question 4:\n")
my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.catch()
my_pokemon.print_pokemon()
print("\n")

'''
Problem 5: Choose Pokemon
Update the Pokemon class with a new method choose() that takes in no parameters except self.

If the Pokemon is caught, the method should print the string "<Pokemon name> I choose you!".

Otherwise, it should print "<Pokemon name> is wild! Catch them if you can!".

class Pokemon():
	...
	
	def choose(self):
		pass
Example Usage:

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()
Example Output:

{'name': 'rattata', 'types': ['Normal'], 'is_caught': False}
rattata is wild! Catch them if you can!
rattata I choose you!
'''

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
         print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
         })

    def catch(self):
        self.is_caught = True

    def choose(self):
        if self.is_caught == True:
            print(f"{self.name} I choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")


print("Question 5:\n")
my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()
print("\n")


'''
Problem 6: Add Pokemon Type
Update the Pokemon class with a new method add_type() that takes in a string new_type as a parameter.

It should add new_type to the Pokemon's list of types.

class Pokemon():
	...
	
	def add_type(self, new_type):
		pass
Example Usage:

jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()
Example Output:

{'name': 'Jigglypuff', 'types': ['Normal'], 'is_caught': False}
{'name': 'Jigglypuff', 'types': ['Normal', 'Fairy'], 'is_caught': False}
'''


class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
         print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
         })

    def catch(self):
        self.is_caught = True

    def choose(self):
        if self.is_caught == True:
            print(f"{self.name} I choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")

    def add_type(self, new_type):
        if new_type is None or isinstance(new_type, str) == False:
            print("Could not add a None type / non-string object to types, please enter a string")
        else:
            self.types.append(new_type)

print("Question 6:\n")
jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()
print("\n")
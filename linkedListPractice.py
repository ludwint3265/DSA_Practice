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

'''
Problem 7

Outside the Pokemon class, write a new function get_by_type() that takes in a list of Pokemon instances my_pokemon and a string pokemon_type as parameters.

The function should return a list of all Pokemon instances from my_pokemon that have the type pokemon_type.

Hint: To test, loop over Pokemon in return list and print the Pokemon's name

class Pokemon():
	...
	
def get_by_type(my_pokemon, pokemon_type):
	pass
Example Usage:

# initializing pokemons
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")
print(normal_pokemon)
Example Output: [Jigglypuff, Meowth, Pidgeot]
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

def get_by_type(my_pokemon, pokemon_type):
    if my_pokemon is None or pokemon_type is None or len(my_pokemon) == 0 or isinstance(my_pokemon, list) == False:
        return []
    else:
        matching_pokemon = []
        for pokemon in my_pokemon:
            for type in pokemon.types:
                if type == pokemon_type:
                    matching_pokemon.append(pokemon.name)

        return matching_pokemon

print("Question 7:\n")
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")
print(normal_pokemon)
print("\n")

'''
Problem 8:
Some Pokemon can evolve into other species of Pokemon.
In the updated Pokemon class below, each instance of Pokemon has an attribute evolution. 
The attribute will either be the default value of None or another Pokemon instance.

Write a function get_evolutionary_line() that takes in a 
Pokemon object starter_pokemon as a parameter.

The function should return a list of itself and the Pokemon that the
starter_pokemon can evolve into.

class Pokemon():
	def  __init__(self, name, types, evolution = None):
		self.name = name
		self.types = types
		self.is_caught = False
		self.evolution = evolution
 
def get_evolutionary_line(starter_pokemon):
	pass
Example Usage:

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)
Example Output:

[`Charmander`, `Charmeleon`, `Charizard`]
[`Charmeleon`, `Charizard`]
['Charizard']
'''

print("Question 8:\n")
class Pokemon():
	def __init__(self, name, types, evolution = None):
		self.name = name
		self.types = types
		self.is_caught = False
		self.evolution = evolution

def get_evolutionary_line(starter_pokemon):
    if starter_pokemon is None:
        return None
    else:
        pokemon_list = []
        pokemon_list.append(starter_pokemon.name)
        if starter_pokemon.evolution == None:
            return pokemon_list
        else:
            pokemon_list.append(starter_pokemon.evolution.name)
            if starter_pokemon.evolution.evolution is not None:
                pokemon_list.append(starter_pokemon.evolution.evolution.name)
                return pokemon_list
            return pokemon_list

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)
print("\n")

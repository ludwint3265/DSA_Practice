# Python practice for functions, lists, and dictionaries

# all in - taking in list of integers a and b, return True if every element in list a is in b, and False otherwise.

def all_in(a, b):
   my_set = set(b)
   for i in range(len(a)):
      if a[i] not in my_set:
         return False
   return True

"""
lst_1 = [1, 2]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1))
"""

# create_dictionary - taking in a list of keys and a list of values, return a dictionary where each item in keys is paired with its index-corresponding item in values. Assume keys ans values are the same length.
def create_dictionary(keys, values):
   new_dict = {}
   for i in range(len(keys)):
      new_dict[keys[i]] = values[i]

   return new_dict

"""
keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']
print(create_dictionary(keys, values))
"""


# write a function print_pair that take a dictionary and a key 'target' as parameters. the function looks for the target and when found, it prints the key and its associated value as "Key: <key>" follow by "Value: <value>". If target is not in dictionary, print "That pair does not exist!"

def print_pair(dictionary, target):
   if dictionary.get(target) == None:
      print("That pair does not exist!")
   else:
      print(f"Key: {target}, Value: {dictionary[target]}")

"""
dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")
"""

# keys vs. values: write a function keys_v_values() that takes in a dictionary whose keys and values are both ints. Using at least one loop, the function should find the sum of all keys in the dictionary and the sum of all values.
# If the sum of keys > sum of values, function should return the string "keys"
# If the sum of values > sum of keys, function should return the string "values"
# If sum of keys = sum of values, function should return the string "balanced"

def keys_v_values(dictionary):
   if len(dictionary) == 0:
      return "balanced"

   key_sum, value_sum, key_list = 0, 0, list(dictionary.keys())
   for i in range(len(key_list)):
      key_sum += key_list[i]
      value_sum += dictionary[key_list[i]]

   if key_sum > value_sum:
      return "keys"
   elif value_sum > key_sum:
      return "values"
   else:
      return "balanced"

"""
dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
print(list(dictionary1.keys()))

greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)
"""

# write a function restock_inventory() that updates an inventory dictionary based on a restock list. it accepts 2 parameters:
# current_inventory: dictionary where each key-value pair represents an item and its current stock in the inventory
# restock_list: a dictionary where each key-value pair represents an item and the quantity to be added to the inventory
# if an item in restock_list is not present in current_inventory, it should be added. the function should return the updated dictionary current_dictionary.

def restock_inventory(current_inventory, restock_list):
   for key in restock_list:
      if current_inventory.get(key) == None:
         current_inventory[key] = restock_list[key]
      else:
         current_inventory[key] += restock_list[key]

   return current_inventory

"""
current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}

print(restock_inventory(current_inventory, restock_list))
"""

# calculate GPA - write a function calculate_gpa() that calculates the GPA for a student based on their course grades and returns "gpa" as a float. the function
# takes in a dictionary report_card as a parameter where each key-value pair represents a course and the grade received in that coure respectively. The grades are 
# represented as strings ("A", "B", "C", "D", "F") and each grade corresponds to a certain number of grade points:
# A=4, B=3, C=2, D=1, F=0. a GPA is calculated by finding the average of all grade points.

def calculate_gpa(report_card):
   gpa, total, classes = float(0), 0, 0

   for key in report_card:
      classes += 1
      if report_card[key] == "A":
         total += 4
      elif report_card[key] == "B":
         total += 3
      elif report_card[key] == "C":
         total += 2
      elif report_card[key] == "D":
         total += 1
      else:
         pass

   gpa = total / classes
   return gpa

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))
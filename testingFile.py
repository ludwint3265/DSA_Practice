import math
import string
from techniques import twoPointer as tp
from tp import check_if_palindrome, sorted_array_2_sum, combine_sorted_arrays

def main():
   myInt = int('7f', 16) # evaluates to integer 127
   print(myInt)
   myList = list('hello')
   print(myList)

   myString = 'Don\'t worry'
   print(myString)
   
   # Two pointers testing
   # palindrome checking
   print("racecar is a palindrome:", check_if_palindrome("racecar"))
   print("fergus is a palindrome:", check_if_palindrome("fergus"))

   # sorted array 2 sum
   print("2 sum in sorted array [1,2,4,6,8,9,14,15] for target 13:", sorted_array_2_sum([1,2,4,6,8,9,14,15], 13))
   print("2 sum in sorted array [1,2,3,6,8,9,14,16] for target 13:", sorted_array_2_sum([1,2,3,6,8,9,14,16], 13))

   # combining sorted array
   print("Combining sorted arrays [1,3,5,7] and [2,4,6,8]:", combine_sorted_arrays([1,3,5,7],[2,4,6,8]))
   return 0
   

if __name__ == "__main__":
   main()

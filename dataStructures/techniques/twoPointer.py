import string

 # 2 pointers : method 1 where we start from the ends of the string/array and go towards middle
   # Time complexity: O(N), Space complexity: O(1)
def check_if_palindrome(s:str) -> bool:
      left = 0
      right = len(s)-1

      while left<right:
         if s[left] != s[right]:
            return False
         left += 1
         right -= 1
      return True
   
print("racecar is a palindrome:", check_if_palindrome("racecar".lower()))
print("fergus is a palindrome:", check_if_palindrome("fergus".lower()))

   # 2 pointers : another method 1 example, sorted array 2 sum
   # Time complexity: O(N), Space complexity: O(1)
def sorted_array_2_sum(arr:list[int], target:int) -> bool:
      left = 0
      right = len(arr)-1

      while left < right:
         current = arr[left] + arr[right]
         if current > target:
            right -= 1
         elif current < target:
            left += 1
         else:
            return True
      return False
   
print("2 sum in sorted array [1,2,4,6,8,9,14,15] for target 13:", sorted_array_2_sum([1,2,4,6,8,9,14,15], 13))
print("2 sum in sorted array [1,2,3,6,8,9,14,16] for target 13:", sorted_array_2_sum([1,2,3,6,8,9,14,16], 13))


   # 2 pointers : merging 2 sorted arrays
   # Time complexity: O(N+M), Space complexity: O(N+M)
def combine_sorted_arrays(a1:list[int],a2:list[int]) -> list[int]:
      p1 = p2 = 0
      ans = []
      
      # intial condition where both arrays are not exhuasted, compares and adds the lowest value to the answer list
      while p1 < len(a1) and p2 < len(a2):
         if a1[p1] < a2[p2]:
            ans.append(a1[p1])
            p1+=1
         elif a2[p2] < a1[p1]:
            ans.append(a2[p2])
            p2+=1
         else:
            ans.append(a1[p1])
            ans.append(a2[p2])
            p1+=1
            p2+=1

      # adding remaining elements from either array if one is exhausted before the other
      while p1 < len(a1):
         ans.append(a1[p1])
         p1+=1
      
      while p2<len(a2):
         ans.append(a2[p2])
         p2+=1
      
      return ans
   
print("Combining sorted arrays [1,3,5,7] and [2,4,6,8]:", combine_sorted_arrays([1,3,5,7],[2,4,6,8]))
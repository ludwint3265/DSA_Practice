import string

def isAnagram(self, s: str, t: str) -> bool:
        #if the lengths of the strings are different, they cannot be anagrams
        if len(s) != len(t):
            return False
        else:
            seen = {}

            #adding each character at its respective index to their own hash maps
            #done to compare frequency for each character
            for char in s:
                if char not in seen:
                    seen[char]=1
                else:
                    seen[char]+=1
            
            seenT = {}
            for charT in t:
                if charT not in seenT:
                    seenT[charT]=1
                else:
                    seenT[charT]+=1
            
            #Python dict comparison checks for :
            #total dict length + exact key-value matches (all keys present, with same exact values for each one)
            #no need to manually check all values and their amounts
            if seen != seenT:
                return False
        return True

def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {} # map value:index

        for i, num in enumerate(nums):

            # trying to find if we have already seen the value
            curr = target - num
            if curr in seen:

                # if the current value is already in seen, then it's accounted for, thus we have both values that add to target
                return [seen[curr], i]

            # if curr isn't seen, it's added to the seen dict
            seen[num] = i
        return
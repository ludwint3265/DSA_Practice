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

from collections import defaultdict
def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

    res = defaultdict(list)
# Creates a dictionary where each key maps to a list.
# When a key is accessed for the first time, defaultdict calls list()
# to create a new empty list as the value.

    for s in strs:
        count = [0] * 26
    # Initializes a fixed-size list of 26 zeros.
    # Each index represents the frequency of a letter from 'a' to 'z'.

        for c in s:
            count[ord(c) - ord('a')] += 1
        # ord(c) gives the integer code of the character.
        # Subtracting ord('a') maps:
        # 'a' -> 0, 'b' -> 1, ..., 'z' -> 25
        # This allows each character to increment its corresponding index
        # in the frequency array.

        res[tuple(count)].append(s)
    # Converts the frequency list into a tuple so it can be used as a dictionary key.
    # Tuples are immutable and hashable, unlike lists.
    # All anagrams produce the same frequency tuple, so they map to the same key.

    return list(res.values())
# Returns only the grouped anagram lists, discarding the keys.
# The result matches the required List[List[str]] output format.

def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
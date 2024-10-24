def isIsomorphic(s: str, t: str) -> bool:
        map = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            # Check if the mapping exists for s -> t
            if char_s in map:
                # If the mapping exists but is inconsistent
                if map[char_s] != char_t:
                    return False
            else:
                # If char_t is already used in another mapping, return False
                if char_t in map.values():
                    return False
                # Create the mapping s -> t
                map[char_s] = char_t

        return True

''''
Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'. 
'''

s = "egg"
t = "add"
print(isIsomorphic(s,t))
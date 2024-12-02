'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 

Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.

'''

# Approach 1: Frequency Count and Sorting
from collections import Counter,defaultdict

def frequencySort( s: str) -> str:
        # 1. Count the frequency of each character in the string
        char_frequency = Counter(s)
        
        # 2. Sort the characters based on their frequency in descending order
        sorted_chars = sorted(char_frequency.items(), key=lambda item: -item[1])
        
        # 3. Build the frequency-sorted string by repeating characters
        frequency_sorted_string = "".join(chars * frequency for chars, frequency in sorted_chars)
        
        # 4. Return the resulting string
        return frequency_sorted_string

#Approach 2: Bucket Sort

def frequencySort( s: str) -> str:
    count = Counter(s)
    buckets = defaultdict(list)
    for char, cnt in count.items():
        buckets[cnt].append(char)
    res = []
    for i in range(len(s), 0, -1):
        for c in buckets[i]:
            res.append(c * i)
    return "".join(res)


s = "tree"

print(frequencySort(s))
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i][: len(prefix)] != prefix:
                print("strs[i][: len(prefix)]",strs[i][: len(prefix)])
                # print("strs[i]", strs[i])
                prefix = prefix[:-1]
                print("prefix",prefix)
                # print("prefix[:-1]",prefix[:-1])
                if not prefix:
                    return ""
        return prefix
#time complexity = O(n), where worst case we need to check total number characters of all string

        # Method2: Iterate character by character (column by column)
        # for i in range(len(strs[0])):
        #     # Get the current character from the first string
        #     current_char = strs[0][i]
            
        #     # Compare this character with the corresponding character in other strings
        #     for string in strs[1:]:
        #         # If we've reached the end of one of the strings, or characters don't match
        #         if i >= len(string) or string[i] != current_char:
        #             return strs[0][:i]  # Return the prefix up to this point
        
        # # If no mismatch found, return the entire first string
        # return strs[0]


strs = ["flower","flow","flight"]

Solution().longestCommonPrefix(strs)


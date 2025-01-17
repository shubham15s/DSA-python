# extpected Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict
def group_inpt(lst):
    grouped = defaultdict(list)
    for word in lst:
        key = "".join(sorted(word))
        grouped[key].append(word)
    return list(grouped.values())
        
Input = ["eat","tea","tan","ate","nat","bat"]
print(group_inpt(Input))
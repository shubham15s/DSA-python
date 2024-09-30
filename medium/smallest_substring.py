# Write a program to find the Length of the smallest sub-string consisting of maximum distinct characters.

# Input : "AABBBCBB"

# Output : 5

# Input : "AABBBCBBAC"

# Output : 3


def len_of_smallest_str(s: str) -> int:
    distinct_char = len(set(s))
    left = 0
    right = 0
    current_char_count = {}
    min_length = float("inf")
    char_dist_count = 0

    while right < len(s):
        # print("calling")
        char = s[right]
        if char in current_char_count:
            current_char_count[char] += 1
            print(char)

        else:
            current_char_count[char] = 1
            char_dist_count += 1

        while char_dist_count == distinct_char:
            print("char dist count", char_dist_count)
            min_length = min(min_length, right - left + 1)
            left_char = s[left]
            current_char_count[left_char] -= 1
            print(current_char_count)

            if current_char_count[left_char] == 0:
                del current_char_count[left_char]
                char_dist_count -= 1
            left += 1
        right += 1
    return min_length if min_length != float("inf") else 0




char = "AABBBCBB"

print("lenght-----> ", len_of_smallest_str(char))




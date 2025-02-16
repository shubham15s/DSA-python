"""
The goal is to compress a string by replacing consecutive repeated characters with the character followed by its count.
"""

def compress_string(s):
    if not s:
        return ""

    compressed = []  # Use a list for efficient concatenation
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  
            count += 1  # Increase count if the same char repeats
        else:
            compressed.append(s[i - 1] + str(count))  # Store previous char + count
            count = 1  # Reset count for new char

    # Append the last character and its count
    compressed.append(s[-1] + str(count))

    return "".join(compressed)  # Convert list to string in O(n)

s = "aaabbccccdd"
compressed_str = compress_string(s)
print(f"Compressed String: {compressed_str}")

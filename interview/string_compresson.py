def compress_string(s):
    if not s:
        return ""
    
    compressed = []
    count = 1  

    # Iterate through the string
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  
            count += 1
        else:
            compressed.append(s[i - 1])
            compressed.append(str(count))
            count = 1 

    compressed.append(s[-1])  
    compressed.append(str(count)) 

    compressed_string = ''.join(compressed)
    return compressed_string if len(compressed_string) < len(s) else s

# Example usage
test_strings = [
    "aaabbbcc",   # Compressed: a3b3c2
    "abcd",       # Compressed: abcd (no compression)
    "aabbccdd",   # Compressed: a2b2c2d2
    "a",          # Compressed: a (no compression)
    "",           # Compressed: (empty string)
    "zzzzyyyyxx", # Compressed: z4y4x2
]

for s in test_strings:
    compressed = compress_string(s)
    print(f"Original: {s} | Compressed: {compressed}")

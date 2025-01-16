def swap_alternate_bits(num):
    # Convert the number to a 16-bit binary string
    binary = format(num, '016b')
    print(f"Original 16-bit binary: {binary}")

    # Convert binary string to a list of characters for swapping
    binary_list = list(binary)
    print(binary_list)

    # Swap every alternate bit
    for i in range(0, len(binary_list) - 1, 2):
        binary_list[i], binary_list[i + 1] = binary_list[i + 1], binary_list[i]

    # Convert the swapped list back to a binary string
    swapped_binary = ''.join(binary_list)
    print(f"Swapped binary: {swapped_binary}")

    # Convert the swapped binary string back to an integer
    swapped_integer = int(swapped_binary, 2)
    return swapped_integer

# Example usage
number = 5  # Input number
result = swap_alternate_bits(number)
print(f"Result after swapping alternate bits: {result}")

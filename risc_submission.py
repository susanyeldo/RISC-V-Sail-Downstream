
def process_list(input_list):
    # Check if the length of the input list is a multiple of 10
    if len(input_list) % 10 != 0:
        raise ValueError("Error: The length of the list must be a multiple of 10.")

    # Remove items at positions which are a multiple of 2 or 3
    processed_list = [item for i, item in enumerate(input_list) if (i + 1) % 2 != 0 and (i + 1) % 3 != 0]
    return processed_list



def run_tests():
    # Test case 1: Valid input
    input_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    try:
        result1 = process_list(input_list1)
        print("Test case 1 passed. Result:", result1)
    except ValueError as e:
        print("Test case 1 failed. Error:", e)

    # Test case 2: Invalid input (not a multiple of 10)
    input_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    try:
        result2 = process_list(input_list2)
        print("Test case 2 failed. Result:", result2)
    except ValueError as e:
        print("Test case 2 passed. Error:", e)

    # Test case 3: Valid input with all items removed
    input_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    try:
        result3 = process_list(input_list3)
        print("Test case 3 passed. Result:", result3)
    except ValueError as e:
        print("Test case 3 failed. Error:", e)



if __name__ == "__main__":
    run_tests()
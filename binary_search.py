def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Adjust the search interval to the right half
        else:
            right = mid - 1  # Adjust the search interval to the left half

    return -1  # Element not found in the array

# Get user input for the sorted array
input_str = input("Enter a sorted array of numbers (comma-separated): ")
arr = [int(x) for x in input_str.split(",")]

# Get user input for the target element
target = int(input("Enter the element to search for: "))

result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")

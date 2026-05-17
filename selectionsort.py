# Selection Sort using Greedy Method

n = int(input("Enter number of elements: "))

arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

# Selection Sort
for i in range(n - 1):

    min_index = i

    # Find minimum element
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap elements
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted array:")
for i in arr:
    print(i, end=" ")

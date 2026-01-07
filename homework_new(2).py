import numpy as np

# Given array
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print("Original Array:\n", arr)

# 1. Indexing: third row, first column
print("\n1. Element at third row, first column:", arr[2, 0])

# 2. Slicing: second column
print("\n2. Second column:", arr[:, 1])

# 3. Data type of array elements
print("\n3. Data type of elements:", arr.dtype)

# 4. Copy: modify first element
arr_copy = arr.copy()
arr_copy[0, 0] = 999
print("\n4. Copy modified:\n", arr_copy)
print("Original array after copy modification:\n", arr)

# 5. View: modify first element
arr_view = arr.view()
arr_view[0, 0] = 555
print("\n5. View modified:\n", arr_view)
print("Original array after view modification:\n", arr)

# 6. Shape of array
print("\n6. Shape of array:", arr.shape)

# 7. Loop through elements with position
print("\n7. Elements with their positions:")
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        print(f"Element at row {i}, column {j} = {arr[i, j]}")

# 8. Join arrays vertically and horizontally
new_arr = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

vertical_join = np.vstack((arr, new_arr))
horizontal_join = np.hstack((arr, new_arr))

print("\n8. Vertical Join:\n", vertical_join)
print("Horizontal Join:\n", horizontal_join)

# 9. Split array into 3 arrays by columns
split_arrays = np.hsplit(arr, 3)
print("\n9. Split arrays by columns:")
for part in split_arrays:
    print(part)

# 10. Search for position of value 60
position_60 = np.where(arr == 60)
print("\n10. Position of value 60:", position_60)

# 11. Sort each row
sorted_rows = np.sort(arr, axis=1)
print("\n11. Each row sorted:\n", sorted_rows)

# 12. Filter elements greater than 50
filtered = arr[arr > 50]
print("\n12. Elements greater than 50:", filtered)

# 13. Random 2x3 array
random_array = np.random.randint(1, 101, size=(2, 3))
print("\n13. Random 2x3 array:\n", random_array)

# 14. Use NumPy ufunc
added_array = np.add(arr, 10)
sqrt_array = np.sqrt(arr)

print("\n14. Add 10 to each element:\n", added_array)
print("Square root of array:\n", sqrt_array)

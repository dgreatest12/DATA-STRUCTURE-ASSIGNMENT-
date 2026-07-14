# 1_arrays.py — Arrays: store, read, update, traverse, find max, insert
# Time complexity: read/update O(1), traverse/max O(n), insert O(n)

def read_value(arr, index):
    return arr[index]

def update_value(arr, index, value):
    arr[index] = value

def traverse_and_print(arr):
    for i, val in enumerate(arr):
        print(f"  index {i}: {val}")

def find_max(arr):
    max_val = arr[0]
    for val in arr:
        if val > max_val:
            max_val = val
    return max_val

def insert_at_index(arr, index, value):
    """Insert value at given index by shifting elements right (no built-in insert)."""
    arr.append(None)  # grow by one slot
    # shift elements one position to the right
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]
    arr[index] = value

# ── Demo ─────────────────────────────────────────────────
marks = [72, 85, 91, 60, 78]

print("=== Arrays Demo ===")
print(f"\nOriginal marks: {marks}")

print(f"\nRead value at index 2: {read_value(marks, 2)}")

update_value(marks, 4, 95)
print(f"After updating index 4 to 95: {marks}")

print("\nTraversing all values:")
traverse_and_print(marks)

print(f"\nMaximum value: {find_max(marks)}")

print(f"\nArray before insert (size {len(marks)}): {marks}")
insert_at_index(marks, 2, 88)
print(f"Array after inserting 88 at index 2: {marks}")

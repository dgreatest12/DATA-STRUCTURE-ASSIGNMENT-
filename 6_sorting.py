# 6_sorting.py — Bubble Sort and Insertion Sort
# Time complexity: both O(n²) worst case, Insertion Sort O(n) best case

def bubble_sort(arr):
    """Repeatedly swap adjacent elements that are out of order."""
    a = arr[:]
    n = len(a)
    print("  Bubble Sort — array state after each pass:")
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        print(f"    Pass {i + 1}: {a}")
        if not swapped:
            print("    (no swaps — early exit)")
            break
    return a


def insertion_sort(arr):
    """Pick each element and insert it into its correct position."""
    a = arr[:]
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# ── Demo ─────────────────────────────────────────────────
original = [64, 34, 25, 12, 22, 11, 90]

print("=== Sorting Demo ===")
print(f"\nOriginal array: {original}\n")

sorted_bubble = bubble_sort(original)
print(f"\n  Final sorted result: {sorted_bubble}")

print(f"\nInsertion Sort on: {original}")
sorted_insertion = insertion_sort(original)
print(f"  Sorted result: {sorted_insertion}")

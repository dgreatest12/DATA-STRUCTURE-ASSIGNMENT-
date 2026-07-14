# 5_searching.py — Linear Search and Binary Search
# Time complexity: linear O(n), binary O(log n)

def linear_search(arr, target):
    """Search left to right, counting every comparison made."""
    comparisons = 0
    for i, val in enumerate(arr):
        comparisons += 1
        if val == target:
            return i, comparisons
    return -1, comparisons


def binary_search(arr, target):
    """Divide-and-conquer on a sorted array, counting comparisons."""
    low, high = 0, len(arr) - 1
    comparisons = 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons


# ── Demo ─────────────────────────────────────────────────
data = sorted([15, 3, 42, 8, 27, 56, 11, 33, 19, 47,
               62, 5, 38, 24, 71, 13, 50, 29, 44, 7])

target = 47

print("=== Searching Demo ===")
print(f"\nSorted list of 20 items:\n  {data}")
print(f"\nSearching for: {target}\n")

idx, comps = linear_search(data, target)
print(f"Linear Search  → found at index {idx} | comparisons made: {comps}")

idx, comps = binary_search(data, target)
print(f"Binary Search  → found at index {idx} | comparisons made: {comps}")

print("\n--- Searching for a missing value (100) ---")
idx, comps = linear_search(data, 100)
print(f"Linear Search  → not found | comparisons made: {comps}")
idx, comps = binary_search(data, 100)
print(f"Binary Search  → not found | comparisons made: {comps}")

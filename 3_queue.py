# 3_queue.py — Queue from scratch (enqueue, dequeue, peek)
# Time complexity: enqueue O(1), dequeue O(n) with list, peek O(1)

class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data.pop(0)  # remove from front

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def __str__(self):
        return f"Queue (front →) {self._data}"


# ── Demo ─────────────────────────────────────────────────
print("=== Queue Demo ===\n")
q = Queue()

print("Enqueue: Alice")
q.enqueue("Alice")
print(q)

print("Enqueue: Bob")
q.enqueue("Bob")
print(q)

print("Enqueue: Carol")
q.enqueue("Carol")
print(q)

print(f"\nPeek (front): {q.peek()}")

print(f"\nDequeue: {q.dequeue()}")
print(q)

print(f"\nDequeue: {q.dequeue()}")
print(q)

print(f"\nEnqueue: Dave")
q.enqueue("Dave")
print(q)

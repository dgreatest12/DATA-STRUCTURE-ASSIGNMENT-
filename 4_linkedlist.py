# 4_linkedlist.py — Singly Linked List
# Time complexity: insert_head O(1), insert_tail O(n), delete O(n), traverse O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_by_value(self, value):
        if self.head is None:
            print(f"  List is empty, nothing to delete.")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
        print(f"  Value {value} not found in list.")

    def traverse(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        print("  " + " → ".join(result) + " → None")


# ── Demo ─────────────────────────────────────────────────
print("=== Singly Linked List Demo ===\n")
ll = LinkedList()

print("Insert at tail: 10, 20, 30")
ll.insert_at_tail(10)
ll.insert_at_tail(20)
ll.insert_at_tail(30)
ll.traverse()

print("\nInsert at head: 5")
ll.insert_at_head(5)
ll.traverse()

print("\nDelete node with value 20")
ll.delete_by_value(20)
ll.traverse()

print("\nDelete node with value 5 (head)")
ll.delete_by_value(5)
ll.traverse()

print("\nAttempt to delete value 99 (not in list)")
ll.delete_by_value(99)

# 2_stack.py — Stack from scratch + Balanced Brackets Checker
# Time complexity: push/pop/peek O(1), balanced_brackets O(n)

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __str__(self):
        return f"Stack{self._data} <-- top"


def balanced_brackets(expression):
    """Returns True if all brackets in the expression are balanced."""
    stack = Stack()
    matching = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty() or stack.pop() != matching[char]:
                return False
    return stack.is_empty()


# ── Demo ─────────────────────────────────────────────────
print("=== Stack Demo ===")
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(f"After pushing 10, 20, 30: {s}")
print(f"Peek: {s.peek()}")
print(f"Pop: {s.pop()}")
print(f"Stack after pop: {s}")

print("\n=== Balanced Brackets Checker ===")
tests = ["([]{})", "([)]", "{[()]}", "((())", ""]
for expr in tests:
    result = "✅ Balanced" if balanced_brackets(expr) else "❌ Not balanced"
    print(f"  '{expr}' → {result}")

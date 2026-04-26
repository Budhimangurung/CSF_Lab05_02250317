
# Task 1: Stack Implementation
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)


print("=" * 45)
print("TASK 1: Stack Implementation")
print("=" * 45)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Stack after pushing elements:")
s.display()
print("Top element:", s.peek())
print("Popped element:", s.pop())
print("Stack after popping:")
s.display()

# Task 2: Balanced Parentheses Checker
def is_balanced(expression):
    stack = Stack()
    matching = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty() or stack.peek() != matching[char]:
                return "Not Balanced"
            stack.pop()

    return "Balanced" if stack.is_empty() else "Not Balanced"


print("\n" + "=" * 45)
print("TASK 2: Balanced Parentheses Checker")
print("=" * 45)

expressions = ["(a+b)*(c+d)", "(a+b)*(c+d", "{[a+b]*(c+d)}", "{[a+b]*(c+d}"]
for expr in expressions:
    print(f"Input:  {expr}")
    print(f"Output: {is_balanced(expr)}\n")
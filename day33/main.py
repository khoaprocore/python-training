class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty!")

    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty!")
        
    def size(self):
        return len(self.items)
    
    def display(self):
        if not self.is_empty():
            print(' - '.join(map(str, self.items)))
        else:
            raise IndexError("Stack is empty!")
    

# LIFO - Last In First Out
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

stack.display()

print(stack.pop()) # 3
print(stack.pop()) # 2

print(stack.peek()) # 1

print(stack.is_empty()) # False
print(stack.size()) # 1

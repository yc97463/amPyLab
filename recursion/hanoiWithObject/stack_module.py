class Stack:
    def __init__(self, name):
        self.items = []
        self.name = name

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("stack is empty")

# LIFO (Last In First Out)
class Stack:
    def __init__(self):
        self.items = []
    
    # Push Method appends item at the last of the stack
    def push (self, item):
        self.items.append(item)

    # Pop Method removes item from the last of the stack
    def pop (self):
        self.items.pop()
    
    # isMepty method returns the values of stack is empty or not
    def isEmpty (self):
        length = len(self.items)
        if length == 0:
            return True
        return False
    
# Test Cases
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(5)
    s.push(19)

    while not s.isEmpty():
        print(s.items)
        s.pop()
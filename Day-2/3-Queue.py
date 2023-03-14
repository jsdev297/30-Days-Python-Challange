class Queue:
    def __init__(self, max_size) -> None:
        self.__items = [0] * max_size
        self.__max_size = max_size
        self.size = 0
        self.head = 0
        self.tail = 0

    def enqueue (self, item):
        if self.__isFull():
            print("Queue is full")
            return
        self.__items[self.tail] = item
        self.tail = (self.tail+1) % self.__max_size
        self.size += 1

    def dequeue (self):
        item = self.__items[self.head]
        self.head = (self.head+1) % self.__max_size
        self.size -= 1
        return item

    def __isFull (self):
        if self.__max_size == self.size:
            return True
        return False
    
    def isEmpty (self):
        if self.size == 0:
            return True
        return False
    
if __name__ == "__main__":
    q = Queue(5)
    q.enqueue("Fatin")
    q.enqueue("Ishraq")
    q.enqueue("Prapya")

    while not q.isEmpty():
        person = q.dequeue()
        print(person)
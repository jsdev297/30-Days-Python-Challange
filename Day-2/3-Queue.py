class Queue:
    def __init__(self, size) -> None:
        self.__items = [0] * size
        self.__max_size = size
        self.head, self.tail, self.size = 0, 0, 0

    def enqueue (self, item):
        if self.__isFull() == True:
            print("Queue is full")
            return
        print("Inserting Item")
        self.__items[self.tail] = item
        self.tail = (self.tail + 1) % self.__max_size
        self.size += 1
        print(self.tail)

    def dequeue (self):
        pass

    def __isFull (self):
        if self.size == self.__max_size: return True
        return False
    
    def printQueue (self):
        print(self.__items)
    
if __name__ == "__main__":
    q = Queue(5)
    q.enqueue("Fatin")
    q.enqueue("Ishraq")
    q.enqueue("Prapya")
    q.enqueue("Carnia")
    q.enqueue("Abu Bakkar")
    q.printQueue()
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, x) -> None:
        self.head = Node(x)
        self.tail = self.head

    def add_head(self, x):
        temp = Node(x)
        temp.next = self.head
        self.head.pre = temp
        self.head = temp

    def add_tail(self, x):
        temp = Node(x)
        temp.pre = self.tail
        self.tail.next = temp
        self.tail = temp

    def add_at(self, k, x):
        p = self.head
        for i in range(k-1):
            p = p.next
        temp = Node(x)
        temp.pre = p
        temp.next = p.next
        p.next.pre = temp
        p.next = temp

    def print_list(self):
        p = self.head
        while p is not None:
            print(p.data, end=' ')
            p = p.next


n = int(input())
l = DoublyLinkedList(1)
for i in range(2, n+1):
    l.add_head(i)
    l.add_tail(i)
l.print_list()

n = int(input())
x = int(input())
l = DoublyLinkedList(x)
for i in range(1, n):
    x = int(input())
    l.add_tail(x)

k = int(input())
x = int(input())

if k == 0:
    l.add_head(x)
elif k == n:
    l.add_tail(x)
else:
    l.add_at(k, x)
l.print_list()


class LinkedList:

    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node

            for e in nodes:
                node.next = Node(data=e)
                node = node.next

    def __repr__(self):
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(current.data)
            current = current.next
        nodes.append('None')
        return ' -> '.join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous = self.head
        for node in self:
            if node.data == target_node_data:
                previous.next = node.next
                return
            previous = node
        raise Exception("Node with data '%s' not found" % target_node_data)

    def __getitem__(self, position):
        # c = 0
        # for x in self:
        #     if c == position:
        #         return x
        #     c += 1

        if position < 0:
            raise Exception(f"Node with position {position} not found!")

        cur_node = self.head

        while cur_node is not None and position > 0:
            position -= 1
            cur_node = cur_node.next

        return cur_node
    
    def reverse_node(self):
        cur_node = self.head
        prev = None

        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = next_node

        self.head = prev

        
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
    

"""
Create a Queue() object inheriting this article’s linked list with enqueue() and dequeue() methods.
"""
class Queue(LinkedList):
    def enqueue(self, item):
        self.add_last(Node(item))

    def dequeue(self):
        if self.head is None:
            raise Exception("List is empty!")
        
        value = self.head.data
        self.head = self.head.next
        return value


queue = Queue()

queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')

for node in queue:
    print(node)

print(queue.dequeue()) # 'a'
print(queue.dequeue()) # 'b'
print(queue.dequeue()) # 'c'
print(queue.dequeue()) # Exception

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return ", ".join(values)


mylist = LinkedList()
mylist.add(6)
mylist.add(1)
mylist.insert(2, 1)
mylist.insert(4, 2)
mylist.insert(2, 2)
mylist.insert(8, 5)

print(mylist)

node1 = mylist.head
node2 = node1.next
node3 = node2.next
node4 = node3.next
node5 = node4.next
node6 = node5.next

mylist.head = node6
node6.next = node2
node5.next = node1

result = []
current = mylist.head
for _ in range(6):
    result.append(str(current.data))
    current = current.next

print(", ".join(result))
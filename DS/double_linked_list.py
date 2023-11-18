class DoubleLinkedListNode:
    def __init__(self, data=None, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        newNode = DoubleLinkedListNode(data=data, next=self.head)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.previous = newNode
            self.head = newNode

    def insert_at_end(self, data):
        newNode = DoubleLinkedListNode(data=data, previous=self.tail)
        if not self.tail:
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def insert_values(self, values):
        for value in values:
            self.insert_at_end(value)

    def print(self):
        elements_string = ''
        tmp = self.head

        while tmp:
            elements_string += str(tmp.data)
            if tmp.next is not None:
                elements_string += ' <=> '

            tmp = tmp.next

        print(elements_string)

    def length(self):
        if self.head:
            counter = 0
            tmp = self.head
            while tmp:
                counter += 1
                tmp = tmp.next

            return counter

        else:
            return 0

    def max(self):
        if self.head:
            maximum = self.head.data
            tmp = self.head
            while tmp:
                if tmp.data > maximum:
                    maximum = tmp.data
                tmp = tmp.next

            return maximum

    def min(self):
        if self.head:
            minimum = self.head.data
            tmp = self.head
            while tmp:
                if tmp.data < minimum:
                    minimum = tmp.data
                tmp = tmp.next

            return minimum

    def insert_at_index(self, index, data):
        length = self.length()
        if index > length:
            print(f"Can't insert at index {index} while the list's length is {length}")

        elif index < 0:
            print("Index must be a positive integer !")

        elif index == 0:
            self.insert_at_beginning(data=data)

        elif index == length:
            self.insert_at_end(data=data)

        else:
            if index <= length / 2:
                counter = 0
                tmp = self.head

                while counter < index - 1:
                    counter += 1
                    tmp = tmp.next

                newNode = DoubleLinkedListNode(data=data, previous=tmp, next=tmp.next)
                tmp.next.previous = newNode
                tmp.next = newNode

            else:
                counter = length
                tmp = self.tail

                while counter > index + 1:
                    counter -= 1
                    tmp = tmp.previous

                newNode = DoubleLinkedListNode(data=data, previous=tmp.previous, next=tmp)
                tmp.previous.next = newNode
                tmp.previous = newNode

    def remove_at_index(self, index):
        length = self.length()
        if index > length:
            print(f"Can't remove at index {index} while the list's length is {length}")

        elif index < 0:
            print("Index must be a positive integer !")

        else:
            if index <= length / 2:
                counter = 0
                tmp = self.head

                while counter < index:
                    counter += 1
                    tmp = tmp.next

                if tmp.next:
                    tmp.previous.next = tmp.next
                    tmp.next.previous = tmp.previous
                else:
                    tmp.next = None

            else:
                counter = length - 1
                tmp = self.tail

                while counter > index:
                    counter -= 1
                    tmp = tmp.previous

                if tmp.previous:
                    tmp.previous.next = tmp.next
                    tmp.next.previous = tmp.previous
                else:
                    tmp.previous = None

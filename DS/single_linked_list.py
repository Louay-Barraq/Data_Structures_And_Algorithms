class SingleLinkedListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new = SingleLinkedListNode(data=data, next=self.head)
        self.head = new

    def insert_at_end(self, data):
        new = SingleLinkedListNode(data=data)

        if self.head is None:
            self.head = new

        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next

            tmp.next = new

    def print(self):
        elements_string = ''
        tmp = self.head

        while tmp is not None:
            elements_string += str(tmp.data)
            if tmp.next is not None:
                elements_string += ' => '

            tmp = tmp.next

        print(elements_string)

    def max(self):
        if self.head:
            tmp = self.head
            maximum = tmp.data

            while tmp is not None:
                if tmp.data > maximum:
                    maximum = tmp.data
                tmp = tmp.next

            return maximum

    def min(self):
        if self.head:
            tmp = self.head
            minimum = tmp.data

            while tmp is not None:
                if tmp.data < minimum:
                    minimum = tmp.data
                tmp = tmp.next

            return minimum

    def insert_values(self, values):
        for value in values:
            self.insert_at_end(value)

    def length(self) -> int:
        counter = 0
        itr = self.head
        while itr is not None:
            counter += 1
            itr = itr.next

        return counter

    def insert_at_index(self, index, data):
        if index > self.length():
            print(f"Can't answer at index {index}, when the list's length is {self.length()} !")
            return

        elif index < 0:
            print("index must be a positive integer !")
            return

        elif index == 0:
            self.insert_at_beginning(data=data)

        else:
            counter = 0
            tmp = self.head

            while counter < index - 1:
                tmp = tmp.next
                counter += 1

            tmp.next = SingleLinkedListNode(data=data, next=tmp.next)

    def remove_at_index(self, index):
        if index > self.length():
            print(f"Can't answer at index {index}, when the list's length is {self.length()} !")
            return

        elif index < 0:
            print("index must be a positive integer !")
            return

        else:
            counter = 0
            tmp = self.head

            while counter < index - 1:
                tmp = tmp.next
                counter += 1

            tmp.next = tmp.next.next

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurrence of data_after value in linked list
        if self.head is not None:
            tmp = self.head
            while tmp:
                if tmp.data == data_after:
                    # Insert data_to_insert after data_after node
                    tmp.next = SingleLinkedListNode(data=data_to_insert, next=tmp.next)
                    break
                tmp = tmp.next

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is not None:
            tmp = self.head
            while tmp.next is not None:
                if tmp.next.data == data:
                    tmp.next = tmp.next.next
                    break
                tmp = tmp.next

from single_linked_list import SingleLinkedList
from double_linked_list import DoubleLinkedList
from hash_table import HashTable
from stack import Stack
from queue import Queue
from tree import TreeNode
from binary_search_tree import BinarySearchTreeNode

def single_linked_list_test():
    # Initializing the linked list
    s_linked_list = SingleLinkedList()

    # Inserting elements
    values = [1, 2, 3, 4, 7]
    s_linked_list.insert_values(values)
    s_linked_list.insert_at_index(0, 100)
    s_linked_list.insert_at_index(4, 20)
    s_linked_list.print()

    # Deleting elements
    s_linked_list.remove_at_index(2)
    s_linked_list.remove_at_index(4)
    s_linked_list.remove_at_index(3)
    s_linked_list.print()

    s_linked_list.insert_after_value(100, 37)
    s_linked_list.print()

    s_linked_list.remove_by_value(1)
    s_linked_list.print()

    # Getting list infos
    print("Length:", s_linked_list.length())
    print("Max Value:", s_linked_list.max())
    print("Min Value:", s_linked_list.min())


def double_linked_list_test():
    d_linked_list = DoubleLinkedList()

    # Inserting elements
    values = [1, 2, 3, -5, 4, 7]
    d_linked_list.insert_values(values)
    d_linked_list.print()

    d_linked_list.insert_at_index(3, 10)
    d_linked_list.insert_at_index(7, 77)
    d_linked_list.print()

    d_linked_list.remove_at_index(2)
    d_linked_list.remove_at_index(5)
    d_linked_list.print()

    # Getting list infos
    print(f"Length: {d_linked_list.length()}")
    print(f"Max: {d_linked_list.max()}")
    print(f"Min: {d_linked_list.min()}")


def hash_table_test():
    hash_table = HashTable()

    hash_table["Louay"] = 7
    hash_table["Wala"] = 18

    hash_table.print()

    del hash_table["Wala"]

    hash_table.print()


def stack_test():
    stack = Stack()

    values = [1, 2, 3, 4, 5]
    stack.push_values(values=values)
    stack.print()
    print(f"Top: {stack.top()}")
    stack.pop()
    stack.print()

    print(f"Max: {stack.max()}")
    print(f"Min: {stack.min()}")


def queue_test():
    queue = Queue()

    values = [1, 2, 3, 4, -5, 37]
    queue.push_values(values)
    queue.print()
    print(f"Top: {queue.top()}")

    queue.pop()
    queue.print()

    print(f"Max: {queue.max()}")
    print(f"Min: {queue.min()}")


def tree_test():
    family = TreeNode("Famille")
    parents = TreeNode("Parents")
    father = TreeNode("Father")
    mother = TreeNode("Mother")
    children = TreeNode("Children")
    daughter = TreeNode("Daughter")
    son = TreeNode("Son")

    # Connect Children
    children.add_child(son)
    children.add_child(daughter)
    # Connect Parents
    parents.add_child(father)
    parents.add_child(mother)
    # Connect the whole family
    family.add_child(parents)
    family.add_child(children)

    family.print_tree()


def binary_search_tree_test():
    values = [3, 7, 1, 4, 6, 8]
    tree = BinarySearchTreeNode(5)

    tree.add_children(values)
    print(tree.in_order_traversal())

    tree.delete(6)
    tree.delete(8)
    print(tree.in_order_traversal())

    print(f"Max: {tree.maximum()}")
    print(f"Min: {tree.minimum()}")


if __name__ == '__main__':
    # single_linked_list_test()
    # double_linked_list_test()
    # hash_table_test()
    # stack_test()
    # queue_test()
    # tree_test()
    binary_search_tree_test()

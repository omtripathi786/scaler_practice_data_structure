class Node:
    """
    The basic building block of a linked list. Each node
    contains data and a reference (or link) to the next node in
    the sequence.
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, head):
        self.head = head

    def append(self, new_node):
        """
        Append the element at the last of linked list.
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    @staticmethod
    def print_ll(A):
        """
        print the whole linked list......
        """
        current = A
        while current:
            print(current.value, end='-->')
            current = current.next
        print('None')

    @staticmethod
    def print_cyclic_ll(A):
        """
        Print a cyclic linked list.
        Stop printing when a loop is encountered.
        """
        current = A
        nodes = set()
        while current:
            if current in nodes:
                print('Loop starts  |  and End at-->', current.value)
                break
            print(current.value, end='-->')
            nodes.add(current)
            current = current.next
        else:
            print('None')

    def get_value(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        count = 1
        while current:
            if count == position:
                return current.value
            current = current.next
            count += 1
        else:
            return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        if position == 1:
            new_element.next = self.head
        count = 1
        while count <= position - 2 and current.next:
            count += 1
            current = current.next
        new_element.next = current.next
        current.next = new_element

    def delete_with_index(self, position):
        """delete the node from linked list with its
         position given and here it will 1 based index."""
        current = self.head
        prev = None
        if position == 1:
            self.head = current.next
        count = 1
        while current:
            if count == position:
                next_node = current.next
                if prev is None:
                    self.head = next_node
                else:
                    prev.next = next_node
                break
            count += 1
            prev = current
            current = current.next

    @staticmethod
    def reverse_ll(hl):
        prev = None
        current = hl
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    @staticmethod
    def find_middle_element(A):
        slow = fast = A
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value


def create_ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    linked_list = LinkedList(head)
    for i in arr[1:]:
        node = Node(i)
        linked_list.append(node)
    return linked_list


def create_cyclic_ll(arr, loop_index):
    """
    Create a cyclic linked list from an array of values.
    The last node in the list will point to the node at loop_index.
    """
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    linked_list = LinkedList(head)
    nodes = [head]
    for i in arr[1:]:
        node = Node(i)
        linked_list.append(node)
        nodes.append(node)
    # Create the loop
    nodes[-1].next = nodes[loop_index]
    return linked_list


if __name__ == '__main__':
    # Test cases
    # Set up some Elements
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    # create linked list object with head node
    ll = LinkedList(n1)
    ll.append(n2)
    ll.append(n3)
    ll.append(n4)
    ll.append(n5)
    ll.append(n6)
    # print linked list to visualize the data
    ll.print_ll(n1)
    print(ll.get_value(5))
    # Test the insert function
    n10 = Node(10)
    ll.insert(n10, 3)
    ll.print_ll(n1)
    # Test deletion
    ll.delete_with_index(3)
    ll.print_ll(n1)
    A = ll.reverse_ll(n1)
    ll.print_ll(A)
    ll.append(n7)
    print(ll.find_middle_element(A))

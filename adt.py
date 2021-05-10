class LLNode:
    def __init__(self, key, next_node=None):
        self.key = key
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def pushFront(self, key) -> None:
        """Add a node at the front of the linked list

        Args:
            key (any): Value of the node to be added
        """
        node = LLNode(key, self.head)
        self.head = node
        if self.tail == None:
            self.tail = node
        self.len += 1

    def pushBack(self, key) -> None:
        """Add a node at the end of the linked list

        Args:
            key (any): Value of the node to be added
        """
        node = LLNode(key)
        if self.isEmpty():  # if empty
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.len += 1

    def popFront(self):
        if self.isEmpty():  # if empty
            print("Cannot pop since it's an EMPTY LIST")
            return -1
        if self.head == self.tail:  # if only one node
            tmp_node = self.head
            tmp_key = tmp_node.key
            # Make head and tail as None since its an empty list
            self.head = None
            self.tail = None
            # Delete first node
            del tmp_node
            return tmp_key
        else:
            # tmp_node points to first node
            tmp_node = self.head
            tmp_key = tmp_node.key
            # Make head point to second node
            self.head = self.head.next
            # Delete tmp_node which points to first node
            del tmp_node
            return tmp_key
        self.len -= 1

    def popBack(self):
        # if empty or if only one element
        if self.isEmpty() or self.head == self.tail:
            self.popFront()
        else:
            mov_node = self.head
            # move to last but first position
            while mov_node.next.next:
                mov_node = mov_node.next
            # make last node as tmp_node
            tmp_node = mov_node.next
            # point last but first node's next to None
            mov_node.next = None
            # make last but first node as tail
            self.tail = mov_node
            # delete last node
            del tmp_node
            self.len -= 1

    def addAfter(self, find_key, key):
        if self.isEmpty():
            print("Cannot insert the key since the list is EMPTY")
        else:
            mov_head = self.head
            while (mov_head) and (mov_head.key != find_key):
                mov_head = mov_head.next
            if mov_head == None:
                print("Specified Key is not present in the list")
            else:
                node = LLNode(key, mov_head.next)
                mov_head.next = node
                if self.tail == mov_head:
                    self.tail = node
                self.len += 1

    def addBefore(self, find_key, key):
        if self.isEmpty():
            print("Cannot insert the key since the list is EMPTY")
        if self.head.key == find_key:
            self.pushFront()
        else:
            mov_head = self.head
            while (mov_head.next) and (mov_head.next.key != find_key):
                mov_head = mov_head.next
            if mov_head.next == None:
                print("Specified Key is not present in the list")
            else:
                node = LLNode(key, mov_head.next)
                mov_head.next = node
                self.len += 1

    def addAfterNode(self, node: LLNode, key) -> int:
        """Add a node of value key after the given linked list node 'node'. If given node is the last node, modify the tail pointer. If the given node is None, raise an Exception

        Args:
            node (LLNode): Linked List node used as position to insert a new node
            key (any): Value for the newly created node

        Returns:
            int: Status
                1 : Inserted at the middle of the linked list
                2 : Inserted at the end of the linked list, so tail is modified
        """
        new_node = LLNode(key, node.next)
        node.next = new_node
        self.len += 1
        if new_node.next == None:
            self.tail = new_node
            return 2
        return 1

    def addAtIndex(self, index: int, key) -> int:
        """Add a node of value key before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.

        Args:
            index (int): Position of the key after insertion
            key (any): Key to be inserted at the given index

        Returns:
            int: Status
                 1 : insertion successful
                -1 : negative index
                -2 : index greater than length+1
        """
        if index < 0:
            return -1
        elif index == 0:
            self.pushFront(key)
        else:
            mov_ind = 0
            mov_head = self.head
            # goto index-1 position
            while mov_head and mov_ind != index - 1:
                mov_head = mov_head.next
                mov_ind += 1
            if mov_head == None:  # index greater than length+1
                return -2
            # insert after index-1 position so that the newly inserted node will be at given index
            self.addAfterNode(mov_head, key)
        return 1

    def deleteAtIndex(self, index: int):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0:
            return -1
        elif self.isEmpty():
            print("Cannot delete anything from an EMPTY LIST")
        elif index == 0:
            return self.popFront()
        else:
            mov_head = self.head
            prev_node = mov_head
            mov_ind = 0
            while mov_head and mov_ind != index:
                prev_node = mov_head
                mov_head = mov_head.next
                mov_ind += 1
            if mov_head == None:
                print("Delete op failed: Index out of range")
            else:
                prev_node.next = mov_head.next
                del mov_head
                if prev_node.next == None:
                    self.tail = prev_node

    def find(self, key):
        mov_head = self.head
        while mov_head and mov_head.key != key:
            mov_head = mov_head.next
        return mov_head if mov_head else None

    def delete(self, key):
        if self.isEmpty():
            print("Cannot delete anything from an EMPTY LIST")
        elif self.head.key == key:
            self.popFront()
        else:
            mov_head = self.head
            prev_node = mov_head
            while mov_head and mov_head.key != key:
                prev_node = mov_head
                mov_head = mov_head.next
            if mov_head == None:
                print("Delete op failed: Specified key is not present in the list")
            else:
                prev_node.next = mov_head.next
                del mov_head
                self.len -= 1
                if prev_node.next == None:
                    self.tail = prev_node

    def getFront(self):
        return self.head

    def getBack(self):
        return self.tail

    def get(self, index):
        if index < 0:
            return -1
        mov_ind = 0
        mov_head = self.head
        while mov_head and mov_ind != index:
            mov_head = mov_head.next
            mov_ind += 1
        if mov_head == None:
            return -1
        else:
            return mov_head.key

    def isEmpty(self) -> bool:
        """Returns a boolean value by checking the head of the linked list

        Returns:
            bool: Status
                True:   If the list is empty, hence head will point to None.
                False:  If the list is not empty.
        """
        return self.head == None

    def display(self):
        if self.isEmpty():
            print("Cannot display since its an EMPTY LIST")
            return
        tmp_node = self.head
        while tmp_node.next:
            print(tmp_node.key, end=" -> ")
            tmp_node = tmp_node.next
        print(tmp_node.key)
        print(tmp_node.key == self.tail.key, self.tail.key)


class DLLNode:
    def __init__(self, key, prev_node=None, next_node=None):
        self.key = key
        self.next = next_node
        self.prev = prev_node

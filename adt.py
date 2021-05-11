class LLNode:
    def __init__(self, key, next_node=None):
        self.key = key
        self.next = next_node

    def update_len(self, n: int) -> None:
        """! Deprecated !
        Update the length of the calling linked list

        Args:
            n (int): integer to be added o the length, can be both negative and positive

        Reference:
            https://stackoverflow.com/questions/17065086/how-to-get-the-caller-class-name-inside-a-function-of-another-class-in-python
        """
        try:
            inspect_stack = inspect.stack()
            # reference to the calling class from the internal stack and update the length of that linked list
            inspect_stack[2][0].f_locals["self"].len += n
        except:
            # if class of calling function is not linked list
            ...


class LinkedList:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.len = 0
        if iterable:
            for element in iterable:
                self.pushBack(element)

    def pushFront(self, key) -> None:
        """Add a node at the front of the linked list

        Args:
            key (any): Value of the node to be added

        Constraints:
            Time: O(1)
            Space: O(1)
        """
        node = LLNode(key, self.head)
        self.head = node
        if self.tail == None:  # if list was previously empty
            self.tail = node
        self.len += 1

    def pushBack(self, key) -> None:
        """Add a node at the end of the linked list

        Args:
            key (any): Value of the node to be added

        Constraints:
            Time: O(1)
            Space: O(1)
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
        """Delete the front node of the linked list and returns the value of it.

        Returns:
            any: Returns the value of the deleted node
            -1 : If the list was empty

        Constraints:
            Time: O(1)
            Space: O(1)
        """
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
            self.len -= 1
            return tmp_key
        else:
            # tmp_node points to first node
            tmp_node = self.head
            tmp_key = tmp_node.key
            # Make head point to second node
            self.head = self.head.next
            # Delete tmp_node which points to first node
            del tmp_node
            self.len -= 1
            return tmp_key

    def popBack(self):
        """Deletes the last node (if exists) and returns the value of it.

        Returns:
            any: Returns the value of the deleted node
            -1 : If the list was empty

        Constraints:
            Time: O(1)
            Space: O(1)
        """

        # if empty or if only one element
        if self.isEmpty() or self.head == self.tail:
            return self.popFront()
        else:
            mov_node = self.head
            # move to last but first position
            while mov_node.next.next:
                mov_node = mov_node.next
            # make last node as tmp_node
            tmp_node = mov_node.next
            tmp_val = tmp_node.key
            # point last but first node's next to None
            mov_node.next = None
            # make last but first node as tail
            self.tail = mov_node
            # delete last node
            del tmp_node
            self.len -= 1
            return tmp_val

    def addAfter(self, find_key, key) -> int:
        """Adds an node with specified key after the node with find_key. If multiple node has the value find_key, first find_key in the list will get the priority.

        Args:
            find_key (any): Value to find in the linked list
            key (any): Value to be inserted after find_key

        Returns:
            int: Status
                -1: List is empty
                -2: Specified Key is not present in the list
                 1: Successful insertion

        Constraints:
            Time: O(n)
            Space: O(1)
        """
        if self.isEmpty():
            # print("Cannot insert the key since the list is EMPTY")
            return -1
        else:
            mov_head = self.head
            while (mov_head) and (mov_head.key != find_key):
                mov_head = mov_head.next
            if mov_head == None:
                # print("Specified Key is not present in the list")
                return -2
            else:
                self.addAfterNode(mov_head, key)
                return 1

    def addBefore(self, find_key, key) -> int:
        """Adds an node with specified key before the node with find_key. If multiple node has the value find_key, first find_key in the list will get the priority.

        Args:
            find_key (any): Value to find in the linked list
            key (any): Value to be inserted before find_key

        Returns:
            int: Status
                -1: List is empty
                -2: Specified Key is not present in the list
                 1: Successful insertion

        Constraints:
            Time: O(n)
            Space: O(1)
        """
        if self.isEmpty():
            # print("Cannot insert the key since the list is EMPTY")
            return -1
        if self.head.key == find_key:
            self.pushFront(key)
        else:
            mov_head = self.head
            while (mov_head.next) and (mov_head.next.key != find_key):
                mov_head = mov_head.next
            if mov_head.next == None:
                # print("Specified Key is not present in the list")
                return -2
            else:
                self.addAfterNode(mov_head, key)
                return 1

    def addAfterNode(self, node: LLNode, key) -> int:
        """Add a node of value key after the given linked list node 'node'. If given node is the last node, modify the tail pointer. If the given node is None, raise an Exception

        Args:
            node (LLNode): Linked List node used as position to insert a new node
            key (any): Value for the newly created node

        Returns:
            int: Status
                1 : Inserted at the middle of the linked list
                2 : Inserted at the end of the linked list, so tail is modified

        Constraints:
            Time: O(1)
            Space: O(1)
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

        Constraints:
            Time: O(n)
            Space: O(1)
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

        Args:
            index (int): Position to be deleted

        Returns:
            any : Value of the deleted node if its deleted
                -1 : negative index
                -2 : index greater than length+1
                -3 : empty list

        Constraints:
            Time: O(n)
            Space: O(1)
        """
        if index < 0:
            return -1
        elif self.isEmpty():
            print("Cannot delete anything from an EMPTY LIST")
            return -3
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
                self.len -= 1
                if prev_node.next == None:
                    self.tail = prev_node

    def find(self, key):
        """Find the given key in the list

        Args:
            key (any): Key to be found

        Returns:
            node: If key is present
            None: If key is not present

        Constraints:
            Time: O(n)
            Space: O(1)
        """
        mov_head = self.head
        while mov_head and mov_head.key != key:
            mov_head = mov_head.next
        return mov_head if mov_head else None

    def delete(self, key):
        """
        Delete the node with the given value in the linked list, if the index is valid. If multiple key's found, delete the node with the first key.

        Args:
            index (int): Position to be deleted

        Returns:
            any : Value of the deleted node if its deleted
                -1 : negative index
                -2 : index greater than length+1
                -3 : empty list

        Constraints:
            Time: O(n)
            Space: O(1)
        """
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

        Constraints:
            Time: O(1)
            Space: O(1)
        """
        return self.head == None

    def length(self) -> int:
        """Returns the length of the linked list

        Returns:
            int: Length of the linked list

        Constraints:
            Time: O(1) # because we store the len variable and update everytime we modify the list
            Space: O(1)
        """
        return self.len

    def display(self):
        if self.isEmpty():
            print("Cannot display since its an EMPTY LIST")
            return
        tmp_node = self.head
        while tmp_node.next:
            print(tmp_node.key, end=" -> ")
            tmp_node = tmp_node.next
        print(tmp_node.key)
        if tmp_node.key != self.tail.key:
            print("Improper tail at:", self.tail.key)


class LinkedlistBinOp:
    @staticmethod
    def isCyclic1(ll: LinkedList) -> bool:
        """Linked List Cycle: Check whether the given linked list is cyclic. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

        Returns:
            bool: Status
                True:   If the linked list has the cycle
                False:  If the linked list is not cyclic

        Constraints:
            Time: O(n)
            Space: O(1)
        """
        rabbit = ll.head  # fast pointer
        tortoise = ll.head  # slow pointer
        while rabbit and rabbit.next:
            rabbit = rabbit.next.next  # move two steps front
            tortoise = tortoise.next  # move one step front
            if rabbit == tortoise:  # if both meet, there is a cycle
                return True
        return False

    @staticmethod
    def isCyclic2(ll: LinkedList) -> LLNode:
        """Linked List Cycle II: Given a linked list, return the node where the cycle begins. If there is no cycle, return None. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

        Returns:
            LLNode: Returns the node which is the beginning of the cycle
            None  : If the linked list has no cycle

        Constraints:
            Time: O(n)
            Space: O(1)
        """
        rabbit = ll.head  # fast pointer
        tortoise = ll.head  # slow pointer
        while rabbit and rabbit.next:
            rabbit = rabbit.next.next  # move two steps front
            tortoise = tortoise.next  # move one step front
            if rabbit == tortoise:  # if both meet, there is a cycle
                break
        else:  # If rabbit == None or rabbit.next == None
            return None
        tortoise2 = ll.head
        while tortoise != tortoise2:
            tortoise2 = tortoise2.next  # move one step front
            tortoise = tortoise.next  # move one step front
        return tortoise

    @staticmethod
    def getIntersectionNode(ll1: LinkedList, ll2: LinkedList) -> LLNode:
        """Intersection of Two Linked Lists: Given two singly linked-lists ll1 and ll2, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return None.

        Args:
            ll1 (LinkedList): First linked list
            ll2 (LinkedList): Second linked list

        Returns:
            LLNode: Node of intersection (if exists)
            None  : If there is no intersection
        """
        lenA, lenB = ll1.len, ll2.len
        tmpA, tmpB = ll1.head, ll2.head
        if lenA < lenB:
            impr = lenB - lenA
            while impr:
                tmpB = tmpB.next
                impr -= 1
        elif lenA > lenB:
            impr = lenA - lenB
            while impr:
                tmpA = tmpA.next
                impr -= 1
        # now that both pointers points to the corresponding position from the end
        # ie. length from tmpA to the end of tmpA = length from tmpB to the end of tmpB
        while tmpA:
            if tmpA == tmpB:  # if both are the same, then its the intersection node
                return tmpA
            tmpA = tmpA.next
            tmpB = tmpB.next
        # if both reach the end of the list, then there is no intersection
        return None

    @staticmethod
    def removeNthFromEnd(ll: LinkedList, n: int):
        """Remove Nth Node From End of List: Given a linked list, remove the nth node from the end of the list.

        Args:
            ll (LinkedList): Linked list to be used
            n (int): index from the last (1 corresponds to the last element, 2 -> last but first and so on...)

        Constraints:
            Time: O(n)
            Space: O(1)
        """
        #! Not tested
        length = ll.len
        del_ind = length - n
        ll.deleteAtIndex(del_ind)

    @staticmethod
    def reverse(ll: LinkedList):
        if ll.head == None:  # empty list
            return None
        if ll.head.next == None:  # single node list
            return ll.head  # no changes
        tmp1, tmp2, tmp3 = ll.head, None, None
        ll.tail = ll.head
        while tmp1:
            tmp3 = tmp2
            tmp2 = tmp1
            tmp1 = tmp1.next
            tmp2.next = tmp3
        ll.head = tmp2


class DLLNode:
    def __init__(self, key, prev_node=None, next_node=None):
        self.key = key
        self.next = next_node
        self.prev = prev_node

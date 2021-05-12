from copy import deepcopy


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
    def __init__(self, iterable=[]):
        self.head = None
        self.tail = None
        self.len = 0
        self.extend(iterable)

    def extend(self, iterable) -> None:
        """Add all the keys specified in the given iterable to the end of the existing linked list

        Args:
            iterable (any): Must be an python iterable which consists of keys to be added

        Constraints:
            Time: O(m) # m= length(iterable)
            Space: O(1)
        """
        for key in iterable:
            self.pushBack(key)

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
            Time: O(n)
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
                tmp_val = mov_head.key
                del mov_head
                self.len -= 1
                if prev_node.next == None:
                    self.tail = prev_node
                return tmp_val

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


class LinkedlistOp:
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
    def removeNthFromEnd(ll: LinkedList, n: int) -> None:
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
    def reverse(ll: LinkedList) -> None:
        """Given a singly linked list, reverse the list by modifying given linked list itself.

        Args:
            ll (LinkedList): Linked List to be reversed

        Returns:
            None: Returns None

        Constraints:
            Time: O(n)
            Space: O(1)
        """
        if ll.head == None or ll.head.next == None:  # empty list or single node list
            ...  # no changes
        else:
            tmp1, tmp2, tmp3 = ll.head, None, None
            ll.tail = ll.head
            while tmp1:
                tmp3 = tmp2
                tmp2 = tmp1
                tmp1 = tmp1.next
                tmp2.next = tmp3
            ll.head = tmp2

    @staticmethod
    def removeElements(ll: LinkedList, val: int) -> None:
        """Remove Linked List Elements: Given a linked list and an integer val, remove all the nodes of the linked list that has LLNode.key == val.

        Args:
            ll (LinkedList): Linked list to be modified
            val (int): nodes with the given value will be deleted

        Constraints:
            Time: O(n)
            Space: O(1)
        """
        if ll.head == None:
            ...
        elif ll.head.next == None:  # len(LinkedList) = 1
            if ll.head.key == val:
                ll.popFront()
        else:
            # We skip checking of head node for now, that is why we start mov_head as head.next
            mov_head, prev = ll.head.next, ll.head
            while mov_head:
                if mov_head.key == val:
                    prev.next = mov_head.next
                    del_tmp = mov_head
                    mov_head = mov_head.next
                    del del_tmp
                    if mov_head == None:  # If the deleted node was last node,
                        ll.tail = prev  # then make prev node as the new tail
                else:
                    # Move forward only if the mov_head.val != val, because we we delete a node then
                    # we will be moving mov_head one step further and we need to check the current mov_head too
                    prev = mov_head
                    mov_head = mov_head.next
            # Since we skipped checking the head node, we check it now
            if ll.head.key == val:
                ll.popFront()

    @staticmethod
    def oddEvenList(ll: LinkedList) -> None:
        """Odd Even Linked List: Given a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices.

        Args:
            ll (LinkedList): Linked List to be modified

        Constraints:
            Time: O(n)
            Space: O(1)
        """
        if ll.head == None or ll.head.next == None or ll.head.next.next == None:
            ...
        else:
            # Create 4 new pointers, 2 for even linked list and 2 for odd linked list
            # Make 1st node as head of odd list, 2nd node as head of even list
            odd_head, odd_tail = ll.head, ll.head
            even_head, even_tail = ll.head.next, ll.head.next
            # Iteration begins with the third node
            mov_head = ll.head.next.next
            # Now heads of both odd and even linked list points to None
            odd_head.next = None
            even_head.next = None
            discriminator = 1  # index used to differentiate odd and even numbers
            while mov_head:
                if discriminator % 2 == 0:
                    even_tail.next = mov_head
                    even_tail = mov_head
                else:
                    odd_tail.next = mov_head
                    odd_tail = mov_head
                # Create new tmp_mov_head to make the newly added node's next as None
                tmp_mov_head = mov_head
                mov_head = mov_head.next
                tmp_mov_head.next = None
                discriminator += 1
            odd_tail.next = even_head
            ll.head = odd_head
            ll.tail = even_tail

    @staticmethod
    def isPalindrome(ll: LinkedList) -> bool:
        """Palindrome Linked List: Given  a singly linked list, return true if it is a palindrome.

        Args:
            ll (LinkedList): Linked list to be checked

        Returns:
            bool: Result
                True  : If given linked list is a palindrome
                False : If given linked list is not a palindrome

        Constraints:
            Time:  O(2n)
            Space: O(1)
        """
        # added to prevent modification of Linked List passed as argument (original)
        ll = deepcopy(ll)
        if ll.head == None or ll.head.next == None:
            return True
        cut_ind = ll.len // 2
        mov_ind, tmp = 0, ll.head
        while mov_ind != cut_ind - 1:
            tmp = tmp.next
            mov_ind += 1
        # making new linked list with new_head as its head
        new_head = tmp.next
        tmp.next = None
        # reverse the second half linked list
        tmp1, tmp2, tmp3 = new_head, None, None
        while tmp1:
            tmp3 = tmp2
            tmp2 = tmp1
            tmp1 = tmp1.next
            tmp2.next = tmp3
        new_head = tmp2
        # now the we have two linked list
        mov_head, mov_new_head = ll.head, new_head
        while mov_head and mov_new_head:
            if mov_new_head.val != mov_head.val:
                return False
            mov_head = mov_head.next
            mov_new_head = mov_new_head.next
        return True

    # @staticmethod
    def mergeTwoSortedLists(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
        """Merge Two Sorted Lists: Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

        Args:
            ll1 (LinkedList): First Linked List
            ll2 (LinkedList): Second Linked List

        Returns:
            LinkedList: Merged Linked List

        Constraints:
            Time:  O(n)
            Space: O(1)
        """
        if ll1.head == None:  # If 1st list is empty then return 2nd list as it is
            return ll2
        elif ll2.head == None:  # If 2nd list is empty then return 1st list as it is
            return ll1
        # To make sure that the function doesn't affect original linked list
        ll1, ll2 = deepcopy(ll1), deepcopy(ll2)
        # Create a new linked list, only LinkedList object is created.
        ll3 = LinkedList()
        # We gotta initially point head of newly created list to worthy node
        if ll1.head.key < ll2.head.key:
            ll3.head = ll1.head
            ll1.head = ll1.head.next
        else:
            ll3.head = ll2.head
            ll2.head = ll2.head.next
        # Check for the smallest value in node and append it to the newly created list
        tmp3 = ll3.head
        while ll1.head and ll2.head:
            if ll1.head.key < ll2.head.key:
                tmp3.next = ll1.head
                ll1.head = ll1.head.next
            else:
                tmp3.next = ll2.head
                ll2.head = ll2.head.next
            tmp3 = tmp3.next
            ll3.tail = tmp3
        # If ll2.head got to the end, then append nodes of ll1 as it is
        while ll1.head:
            tmp3.next = ll1.head
            ll1.head = ll1.head.next
            tmp3 = tmp3.next
            ll3.tail = tmp3
        # If ll1.head got to the end, then append nodes of ll2 as it is
        while ll2.head:
            tmp3.next = ll2.head
            ll2.head = ll2.head.next
            tmp3 = tmp3.next
            ll3.tail = tmp3
        ll1.tail, ll2.tail = None, None
        # Return newly created merged linked list
        return ll3

    def addTwoNumbers(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
        """Add Two Numbers: Given two linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. Assume the two numbers do not contain any leading zero, except the number 0 itself.

        Args:
            ll1 (LinkedList): First Linked List
            ll2 (LinkedList): Second Linked List

        Returns:
            LinkedList: Sum of two linked list as a newly created linked list

        Constraints:
            Time:  O(n)
            Space: O(n) # linked list with sum (max: n+1 nodes)
        """
        if ll1.head == None:  # If 1st list is empty then return 2nd list as it is
            return ll2
        elif ll2.head == None:  # If 2nd list is empty then return 1st list as it is
            return ll1
        # Create a new linked list, only LinkedList object is created.
        ll3 = LinkedList()
        # We gotta initially point head of newly created list
        adder = ll1.head.key + ll2.head.key
        zum, carry = adder % 10, adder // 10
        ll3.pushFront(zum)
        tmp3 = ll3.head
        tmp1, tmp2 = ll1.head.next, ll2.head.next
        # Create a new node with the sum of two nodes and append it
        while tmp1 and tmp2:
            adder = tmp1.key + tmp2.key + carry
            zum, carry = adder % 10, adder // 10
            tmp3.next = LLNode(zum)
            tmp1, tmp2, tmp3 = tmp1.next, tmp2.next, tmp3.next
            ll3.tail = tmp3
        # If ll2.head got to the end, then append nodes of ll1 as it is
        while tmp1:
            adder = tmp1.key + carry
            zum, carry = adder % 10, adder // 10
            tmp3.next = LLNode(zum)
            tmp1, tmp3 = tmp1.next, tmp3.next
            ll3.tail = tmp3
        # If ll1.head got to the end, then append nodes of ll2 as it is
        while tmp2:
            adder = tmp2.key + carry
            zum, carry = adder % 10, adder // 10
            tmp3.next = LLNode(zum)
            tmp2, tmp3 = tmp2.next, tmp3.next
            ll3.tail = tmp3
        # Return newly created merged linked list
        if carry:
            ll3.pushBack(1)
        return ll3


class DLLNode:
    def __init__(self, key, prev_node=None, next_node=None):
        self.key = key
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self, iterable=[]):
        self.head = None
        self.tail = None
        self.len = 0
        self.extend(iterable)

    def extend(self, iterable) -> None:
        """Add all the keys specified in the given iterable to the end of the existing linked list

        Args:
            iterable (any): Must be an python iterable which consists of keys to be added

        Constraints:
            Time: O(m) # m= length(iterable)
            Space: O(1)
        """
        for key in iterable:
            self.pushBack(key)

    def pushFront(self, key) -> None:
        """Add a node at the front of the doubly linked list

        Args:
            key (any): Value of the node to be added

        Constraints:
            Time: O(1)
            Space: O(1)
        """
        node = DLLNode(key, None, self.head)
        if self.head:  # if list was not previously empty
            self.head.prev = node
        self.head = node
        if self.tail == None:  # if list was previously empty
            self.tail = node
        self.len += 1

    def pushBack(self, key) -> None:
        """Add a node at the end of the doubly linked list

        Args:
            key (any): Value of the node to be added

        Constraints:
            Time: O(1)
            Space: O(1)
        """
        node = DLLNode(key)
        if self.isEmpty():  # if empty
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.len += 1

    def popFront(self):
        """Delete the front node of the doubly linked list and returns the value of it.

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
            # Make prev of 2nd node point to None
            self.head.next.prev = None
            # Make head point to 2nd node
            self.head = self.head.next
            # Delete tmp_node which points to first node
            del tmp_node
            self.len -= 1
            return tmp_key

    def popBack(self):
        """Deletes the last node (if exists) of doubly linked list and returns the value of it.

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
            # make last node as tmp_node
            tmp_node = self.tail
            tmp_val = tmp_node.key
            # point last but first node's next to None
            self.tail.prev.next = None
            # make last but first node as tail
            self.tail = self.tail.prev
            # delete last node
            del tmp_node
            self.len -= 1
            return tmp_val

    def addAfter(self, find_key, key) -> int:
        """Adds a node with specified key after the node with find_key. If multiple node has the value find_key, first find_key in the list will get the priority.

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
        """Adds a node with specified key before the node with find_key. If multiple node has the value find_key, first find_key in the list will get the priority.

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

    def addAfterNode(self, node: DLLNode, key) -> int:
        """Add a node of value key after the given linked list node 'node'. If given node is the last node, modify the tail pointer. If the given node is None, raise an Exception

        Args:
            node (DLLNode): Linked List node used as position to insert a new node
            key (any): Value for the newly created node

        Returns:
            int: Status
                1 : Inserted at the middle of the linked list
                2 : Inserted at the end of the linked list, so tail is modified

        Constraints:
            Time: O(1)
            Space: O(1)
        """
        new_node = DLLNode(key, node, node.next)
        if node.next:  # if given node is not the last node
            node.next.prev = new_node
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
            # print("Cannot delete anything from an EMPTY LIST")
            return -3
        elif index == 0:
            return self.popFront()
        else:
            mov_head = self.head
            mov_ind = 0
            while mov_head and mov_ind != index:
                mov_head = mov_head.next
                mov_ind += 1
            if mov_head == None:
                # print("Delete op failed: Index out of range")
                return -2
            else:
                prev_node = mov_head.prev
                mov_head.prev.next = mov_head.next
                if mov_head.next:
                    mov_head.next.prev = mov_head.prev
                tmp_val = mov_head.key
                del mov_head
                self.len -= 1
                if prev_node.next == None:
                    self.tail = prev_node
                return tmp_val

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
            # print("Cannot delete anything from an EMPTY LIST")
            return -1
        elif self.head.key == key:
            return self.popFront()
        else:
            mov_head = self.head
            while mov_head and mov_head.key != key:
                mov_head = mov_head.next
            if mov_head == None:
                # print("Delete op failed: Specified key is not present in the list")
                return -2
            else:
                prev_node = mov_head.prev
                mov_head.prev.next = mov_head.next
                if mov_head.next:
                    mov_head.next.prev = mov_head.prev
                tmp_val = mov_head.key
                del mov_head
                self.len -= 1
                if prev_node.next == None:
                    self.tail = prev_node
                return tmp_val

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
            return -2
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
            print(tmp_node.key, end=" <-> ")
            tmp_node = tmp_node.next
        print(tmp_node.key)
        if tmp_node.key != self.tail.key:
            print("Improper tail at:", self.tail.key)

    def displayReverse(self):
        if self.isEmpty():
            print("Cannot display since its an EMPTY LIST")
            return
        tmp_node = self.tail
        while tmp_node.prev:
            print(tmp_node.key, end=" <-> ")
            tmp_node = tmp_node.prev
        print(tmp_node.key)
        if tmp_node.key != self.head.key:
            print("Improper head at:", self.head.key)

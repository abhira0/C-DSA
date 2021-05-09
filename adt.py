class LLNode:
    def __init__(self, key, next_node=None):
        self.key = key
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pushFront(self, key):
        node = LLNode(key, self.head)
        self.head = node
        if self.tail == None:
            self.tail = node

    def pushBack(self, key):
        node = LLNode(key)
        if self.head == None:  # if empty
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def popFront(self):
        if self.head == None:  # if empty
            print("Cannot pop since it's an EMPTY LIST")
        elif self.head == self.tail:  # if only one node
            tmp_node = self.head
            # Make head and tail as None since its an empty list
            self.head = None
            self.tail = None
            # Delete first node
            del tmp_node
        else:
            # tmp_node points to first node
            tmp_node = self.head
            # Make head point to second node
            self.head = self.head.next
            # Delete tmp_node which points to first node
            del tmp_node

    def popBack(self):
        # if empty or if only one element
        if self.head == None or self.head == self.tail:
            self.popFront()
        else:
            mov_node = self.head
            # move to last but 1th position
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

    def addAfter(self, find_key, key):
        if self.head == None:
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

    def addBefore(self, find_key, key):
        if self.head == None:
            print("Cannot insert the key since the list is EMPTY")
        if self.head.key == find_key:
            node = LLNode(key, self.head)
            self.head = node
        else:
            mov_head = self.head
            while (mov_head.next) and (mov_head.next.key != find_key):
                mov_head = mov_head.next
            if mov_head.next == None:
                print("Specified Key is not present in the list")
            else:
                node = LLNode(key, mov_head.next)
                mov_head.next = node

    def find(self, key):
        mov_head = self.head
        while mov_head and mov_head.key != key:
            mov_head = mov_head.next
        return mov_head if mov_head else None

    def delete(self, key):
        if self.head == None:
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
                if prev_node.next == None:
                    self.tail = prev_node

    def getFront(self):
        return self.head

    def getBack(self):
        return self.tail

    def isEmpty(self):
        return self.head == None

    def display(self):
        if self.head == None:
            print("Cannot display since its an EMPTY LIST")
            return
        tmp_node = self.head
        while tmp_node.next:
            print(tmp_node.key, end=" -> ")
            tmp_node = tmp_node.next
        print(tmp_node.key)
        print(tmp_node.key == self.tail.key, self.tail.key)

    def max(self):
        if self.head == None:
            print("EMPTY LIST")
            return
        maxi = self.head.key
        mov_head = self.head
        while mov_head:
            maxi = max(maxi, mov_head.key)
            mov_head = mov_head.next
        return maxi

    def min(self):
        if self.head == None:
            print("EMPTY LIST")
            return
        mini = self.head.key
        mov_head = self.head
        while mov_head:
            mini = min(mini, mov_head.key)
            mov_head = mov_head.next
        return mini

    def sum(self):
        if self.head == None:
            print("EMPTY LIST")
            return
        summer = self.head.key
        mov_head = self.head
        while mov_head:
            summer += mov_head.key
            mov_head = mov_head.next
        return summer

    def product(self):
        if self.head == None:
            print("EMPTY LIST")
            return
        prod = self.head.key
        mov_head = self.head
        while mov_head:
            prod *= mov_head.key
            mov_head = mov_head.next
        return prod


class DLLNode:
    def __init__(self, key, prev_node=None, next_node=None):
        self.key = key
        self.next = next_node
        self.prev = prev_node

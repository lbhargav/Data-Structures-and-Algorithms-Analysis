#####################################################################
'''
 # Implements a Linkedlist and Linkedlist algorithms.
 # @author Bhargav Lenka
'''
#####################################################################

class Node:
    # initilizng node class
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    nodeCount = 0
    def __init__(self):
        self.head = None
        self.nodeCount = 0

    def size(self):
        return self.nodeCount

    def insertBefore(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            self.head = newNode
            self.head.next = temp
            del temp
        self.nodeCount += 1

    def insertEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while True:
                if current.next is None:
                    break
                current = current.next
            current.next = newNode
        self.nodeCount += 1

    def insertBetween(self, idx, data, size):
        newNode = Node(data)
        if (idx > size or self.head == None or idx == 0):
            print(" index out of bounds")
            exit
            # raise Exception('Index out of bounds')
        else:
            current = self.head
            position = 0
            while True:
                if (position == idx):
                    prev.next = newNode
                    newNode.next = current
                    break
                prev = current
                current = current.next
                position +=1
            self.nodeCount += 1


    def removeFirst(self):
        if self.head is None:
            print("Empty List")
        self.head = self.head.next
        self.nodeCount -= 1

    def removeLast(self):
        if self.head is None:
            print("Empty List")
        current = self.head
        while True:
            if current.next is None:
                current = prev
                current.next = None
                break
            prev = current
            current = current.next
        self.nodeCount -= 1


    def removeBetween(self, idx, size):
        if (idx >= size or self.head == None or idx == 0):
            print(" index out of bounds")
            # raise Exception('Index out of bounds')
        else:
            current = self.head
            position = 0
            while True:
                if (position == idx):
                    prev.next = current.next
                    break
                prev = current
                current = current.next
                position += 1
            self.nodeCount -= 1


    def setValue(self, idx, newData, size):
        if (idx > size or self.head == None):
            print(" index out of bounds")
        else:
            current = self.head
            position = 0
            while True:
                if (position == idx):
                    current.data = newData
                    break
                current = current.next
                position += 1
            return current.data

    def getValue(self, idx, size):
        if (idx > size or self.head == None):
            print(" index out of bounds")
        else:
            current = self.head
            position = 0
            while True:
                if (position == idx):
                    value = current.data
                    print()
                    print("value at index", idx, "is ",value)
                    break
                current = current.next
                position += 1
            return value

    # Function to swap Nodes a  and b in linked list by changing links
    def swap(self, idx1, idx2, size):
        if (idx1 > size or idx2 > size or self.head == None):
            print(" index out of bounds")
            return
        # Nothing to do if idx1 and idx2 are same
        if idx1 == idx2:
            return
        # finding idx1 and keeping track of idx1 prev
        prev1 = None
        current1 = self.head
        position = 0
        while (idx1 > position):
            prev1 = current1
            current1 = current1.next
            position += 1
        prev2 = None
        current2 = self.head
        position = 0
        while (idx2 > position):
            prev2 = current2
            current2 = current2.next
            position += 1
        if prev1 != None:
            prev1.next = current2
        else:
            self.head = current2
        if prev2 != None:
            prev2.next = current1
        else:
            self.head = current1
        # inter changing the links
        temp = current1.next
        current1.next = current2.next
        current2.next = temp

    # swap by interchanging the data, expensive
    '''
    def swap(self, idx1, idx2, size):
        if (dx1 > size or idx2 > size or self.head == None):
            print(" index out of bounds")
        else:
            idx1Value = self.getValue(idx1, size)
            idx2Value = self.getValue(idx2, size)
            self.setValue(idx1, idx2Value, size)
            self.setValue(idx2, idx1Value, size)
    '''


    # foward shift and backward sift
    def shift(self, shifts, direction):
        # if list is empty operation fails
        if self.head == None:
            print("operation failed")
            return
        # if one node is presenet do nothing
        elif self.head.next == None:
            return
        # forward direction, when direction = -1
        elif (direction == +1):
            for i in range(0, shifts):
                current = self.head
                while True:
                    if current.next is None:
                        break
                    prev = current
                    current = current.next
                temp = self.head
                self.head = current
                self.head.next = temp
                prev.next = None

        #  backward direction, when direction = -1
        elif(direction == -1):
            for i in range(0, shifts):
                current = self.head
                while True:
                    if current.next is None:
                        break
                    current = current.next
                temp = self.head
                self.head = self.head.next
                current.next = temp
                temp.next = None
        elif direction != +1 or direction != -1:
            print("invalid direction")
            return

    def erase(self, idx, size):
        if (idx > size or self.head == None):
            print(" index out of bounds")
        else:
            current = self.head
            position = 1
            while True:
                if (position == idx):
                    break
                current = current.next
                position += 1
            current.next = None

    def insertList(self, list, idx, size):
        if (idx > size or self.head == None):
            print(" index out of bounds")
        else:
            current1 = self.head
            position = 0
            while True:
                if (position == idx):
                    break
                # prev1 = current1
                current1 = current1.next
                position += 1
            temp = current1.next
            current1.next = list
            list.next = temp

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # iterative
        if l1 == None: return l2
        if l2 == None: return l1
        if l1 == None and l2 == None: return None
        l3 = ListNode(0)
        curr = l3
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return l3.next

        # recursion
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) > 1:
            m = len(lists) // 2
            l1 = self.mergeKLists(lists[:m])
            l2 = self.mergeKLists(lists[m:])
            return self.mergeTwoLists(l1, l2)

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # iterative
        if head is None:
            return None
        prev = None
        curr = head
        while not curr is None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head =  prev
        return head

        # recursion
        if head is None:
            return head
        if head.next is None:
            return head
        p = ListNode(head)
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        if head.next is None:
            return False
        slow = head
        fast = head.next
        while not slow is fast:
            if fast is None or fast.next is None:
                return False
            else:
                slow = slow.next
                fast = fast.next.next
        return True

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        p = headA
        q = headB
        while True:
            if p == q:
                return p
            if p:
                p = p.next
            else:
                p = headB
            if q:
                q = q.next
            else:
                q = headA

    def printList(self):
        if self.head is None:
            print(" Empty Linked List")
            return
        print()
        print("Head -->", end = " ")
        current = self.head
        while True:
            if current is None:
                break
            print(current.data, "-->", end = " ")
            current = current.next
            # self.count += self.count
        print("None")
        print()
        # print(self.count)

def main():
    # firstNode = Node("1")
    linkedList = LinkedList()
    linkedList.insertBefore("2")
    linkedList.insertBefore("1")
    linkedList.insertEnd("3")
    linkedList.printList()
    print("nodeCount:", linkedList.size())
    linkedList.insertBetween(3, 4, linkedList.size())
    linkedList.printList()
    print("nodeCount:", linkedList.size())
    linkedList.removeFirst()
    linkedList.printList()
    print("nodeCount:", linkedList.size())
    linkedList.removeLast()
    linkedList.printList()
    print("nodeCount:", linkedList.size())
    linkedList.removeBetween(3, linkedList.size())
    linkedList.printList()
    print("nodeCount:", linkedList.size())

    linkedList.setValue(2, 4, linkedList.size())
    linkedList.printList()
    print("nodeCount:", linkedList.size())
    linkedList.getValue(2, linkedList.size())
    print("-----------")
    linkedList.swap(1,0 , linkedList.size())
    linkedList.printList()
    print(" forward shift")
    # +1 for forward direction
    # -1 for backward direction
    linkedList.shift(2, +1)
    linkedList.printList()

    print(" backward shift")
    linkedList.shift(4, -1)
    linkedList.printList()
    print("erase")
    linkedList.erase(1,linkedList.size())
    linkedList.printList()
    count = linkedList.size()
    print("Number of Nodes in the LinedList:", count)

    print("---------------")
    list = LinkedList()
    list.insertBefore("10")
    list.insertBefore("9")
    list.insertBefore("8")
    list.printList()
    print("nodeCount:", list.size())
    linkedList.insertList(list, 1, linkedList.size())
    list.printList()
    print("nodeCount:", list.size())

if __name__ == '__main__':
    main()






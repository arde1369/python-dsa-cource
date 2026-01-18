class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # WRITE MERGE METHOD HERE #
    #                         #
    #                         #
    #                         #
    #                         #
    ###########################
    def merge(self,ll):
        dn = Node(0)
        current = dn
        itr1 = self.head
        itr2 = ll.head
        while itr1 and itr2:
            if itr1.value < itr2.value:
                current.next = itr1
                itr1 = itr1.next
            else:
                current.next = itr2
                itr2 = itr2.next
            current = current.next
        while itr1:
            current.next = itr1
            itr1 =itr1.next
            current = current.next
        while itr2:
            current.next = itr2
            itr2 =itr2.next
            current = current.next
        current.next = None
        self.head = dn.next


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""
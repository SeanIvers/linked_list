# Initial structure of node class and linked list class

class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None # Not sure what Node's neighbor is upon creation

class SList:
    def __init__(self,):
        self.head = None

    # def addToFront(self, val):
    #     new_node = SLNode(val)
    #     if self.head != None:
    #         new_node.next = self.head
    #     self.head = new_node
    #     return self

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head # save the current head in a variable
        new_node.next = current_head # SET the new node's next TO the list's current head
        self.head = new_node # SET the list's head TO the node we created in the last step
        return self # chaining
    
    # def printList(self):
    #     itr = self.head
    #     while itr != None:
    #         print(itr.value)
    #         itr = itr.next
    #     return self

    def print_values(self):
        runner = self.head # a pointer to the list's first node
        while (runner != None): # iterating while runner is a node and not None
            print(runner.value) # print the current node's value
            runner = runner.next # set the runner to it's neighbor
        return self # chaining

    # def addToEnd(self, val):
    #     if self.head == None:
    #         self.add_to_front(val)
    #         return self
    #     itr = self.head
    #     new_node = SLNode(val)
    #     while itr.next != None:
    #         itr = itr.next
    #     itr.next = new_node
    #     return self

    def add_to_back(self, val):
        if self.head == None: # if the list is empty
            self.add_to_front(val) # run the add_to_front method
            return self # end function
        new_node = SLNode(val) # create a new instance of our Node class with the given value
        runner = self.head # set an iterator to start at the front of the list
        while (runner.next != None): # iterator until the iterator doesn't have a neighbor
            runner = runner.next # increment the runner to the next node in the list
        runner.next = new_node # increment the runner to the next node in the list
        return self

    # remove the first node and return its value
    def remove_from_front(self):
        self.head = self.head.next
        return self

    # remove the last node and return its value
    def remove_from_back(self):
        if self.head == None:
            return self
        current_node = self.head
        prev_node = self.head
        while current_node.next != None:
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = None
        return self

    # remove the first node with the given value
        # consider:
        # the node with the given value is the first node
        # the node with the given value is in the middle of the list
        # the node with the given value is the last node
    def remove_val(self, val):
        if self.head == None:
            return self
        elif self.head.value == val:
            self.head = self.head.next
            return self
        prev_node = self.head
        current_node = self.head.next
        while current_node != None:
            if current_node.value == val:
                prev_node.next = current_node.next
                return self
            elif current_node.next == None:
                return self
            prev_node = current_node
            current_node = current_node.next

    # insert a node with value val as the nth node in the list
        # consider:
        # n is 0
        # n is the length of the list
        # n is between 0 and the length of the list
    def insert_at(self, val, n):
        if self.head != None:
            if n == 0:
                self.add_to_front(val)
                return self
            prev_node = self.head
            current_node = self.head.next
            counter = 0
            new_node = SLNode(val)
            while current_node != None:
                if counter == n - 1:
                    new_node.next = current_node
                    prev_node.next = new_node
                    return self
                prev_node = current_node
                current_node = current_node.next
                counter += 1
            self.add_to_back(val)
            return self
        return self


my_list = SList()
my_list2 = SList()

my_list.add_to_front(3).add_to_front(2).add_to_front(1).add_to_front(0)
# my_list.add_to_back(4).remove_from_front().remove_from_back().print_values()
# my_list.remove_val(3).print_values()
# my_list2.remove_val(8)

my_list.insert_at(-1, 4).print_values()
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):  
        self.head = None
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        current = self.head
        if current is not None:
            if current.val == node:
                self.head = current.next
                current = None
                return 
        while(current.next):
            if current.val == node:
                break
            prev = current
            current = current.next
        if current == None:
            return
        prev.next = current.next
        current = None
        # node.val = node.next.val
        # node.next = node.next.next
    def append(self, new_data): 
  
        # 1. Create a new node 
        # 2. Put in the data 
        # 3. Set next as None 
        new_node = ListNode(new_data) 
  
        # 4. If the Linked List is empty, then make the 
        #    new node as head 
        if self.head is None: 
            self.head = new_node 
            return
  
        # 5. Else traverse till the last node 
        last = self.head 
        while (last.next): 
            last = last.next
  
        # 6. Change the next of last node 
        last.next =  new_node 

s = Solution()
s.append(4) 
s.append(5)
s.append(1)
s.append(9)

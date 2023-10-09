
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CustomLinkedList:
    def __init__(self, arr) -> None:
        if not arr:
            self.head = None
            return
        
        self.head = Node(arr[0])
        current = self.head
        for data in arr[1:]:
            current.next = Node(data)
            current = current.next

    def insert(self, root, item):
        if root is None:
            return Node(item)
        
        current = root
        while current.next:
            current = current.next
        
        current.next = Node(item)
        return root
    
    def reverselist(self, head):
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev
    
    def print_as_list(self, head):
        linked_list_as_list = []
        current = head
        while current:
            linked_list_as_list.append(current.data)
            current = current.next

        print(linked_list_as_list)
        return linked_list_as_list

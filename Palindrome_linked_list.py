#Palindrome_linked_list.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)

def add(data):
    node = head
    while node.next: #  while next address is not exist
        node = node.next
    node.next = ListNode(data)

add(2)
add(2)
add(1)

def isPalindrome(head):
    q =[]

    if not head:
        return True

    node = head

    # change list
    while node is not None:
        q.append(node.val)
        node = node.next
    print(q)


    # test palindrome
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True
print(isPalindrome((head)))
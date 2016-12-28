"""
Linked Lists: Pg. 94 - 2.1

Remove Dups:  Write code to remove duplicates from an unsorted LinkedList
    **Follow up: How would you solve if a temp buffer is not allowed

Tests:
    node_a = Node('data', None)
    node_b = Node('alex', node_c)
    node_c = Node('alex', node_d)
    node_d = Node('hello', None)

    Pass in a LL:
    None : None
    node_a : node_a
    node_c : node_c -> node_d
    node_b : node_b -> node_d

Outloud:  Ok, so first thing is to clarify if this is a singly or doubly Linked
List (ASSUMPTION: Single) Also to be explicit -> we are removing duplicates of
data if they are pointers to the same space in memory not just if they are the
same value
    For Example: node_x -> "alex", node_z -> "alex" at differnt memory
    locations so we would keep both.  However if:
    node_a -> "alex" <- node_b both point to the same spot in memory remove
    node_b

*Should ask if the given input can be modified or not
"""

from DataStructures import LinkedList, Node

def remove_dups(LL):
    seen_data = set()
    if len(LL) < 2:
        return LL
    p1 = LL.head
    p2 = p1.next
    seen_data.add(id(p1.data))
    while p2 is not None:
        if id(p2.data) in seen_data:
            p2 = p2.next
        else:
            p1.next = p2
            p1 = p2
            p2 = p1.next
            seen_data.add(id(p1.data))
    LL.tail = p1
    return LL


node_a = Node('data')
node_b = Node('alex')
node_c = Node('alex')
node_d = Node('hello')

node_b.next = node_c
node_c.next = node_d

linked_list = LinkedList()
linked_list.head = node_b
remove_dups(linked_list)
print node_b.next.data

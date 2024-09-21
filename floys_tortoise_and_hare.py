# also known as fast and slow pointers. 

# NOTE:usually you have a fast and slow pointer.
# the fast pointer shifts by 2
# the slow pointer shifts by 1.
# fast pointer is 2x as fast as the slow. 

# we keep doing it until ONE of the pointers 
# reaches the end of the list. Which will 
# technically BE THE FAST pointer.

# lets say we want to find the middle... 
# FAST REACHES END, SLOW IS HALF, SO AT MIDDLE.

# algorithm also works on null values.
# if the head is null, the loop doesnt even
# execute.
def middleOfList(head):
    slow = head
    fast = head 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# NOTE: now lets think about it... what if we have a cycle?
# We can actually determine if a LinkedList has a cycle using this technique.
def cycleDetectionLinkedList(head) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # if they intersect, we know there is a cycle.
        # the reason? the fast pointer should always be ahead.
        # a cycle or loop basically means that are slow was able
        # to catch uo, that is the only case.
        # IT IS GUARANTEED THEY WILL INTERSECT. 
        if slow == fast:
            return True
    return False

# what if you are asked for the head of the cycle? 
# that wont be their intersection point.

def getHeadOfCycle(head):
    slow = head 
    fast = head 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            # cycle detected
            break
        
        if not fast or not fast.next: 
            return None

        # start at the original head
        slow2 = head 
        # in this second phase, they are guaranteed 
        # to meet at the head of the cycle.
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next 
        return slow
    
# so lets think... why does this work?
# 2 * slow = fast
# 2 * (P + C - X) = P + C + C - X
# doing some basic algebra... 
# P - X = 0
# P = X 

# this math guarantees that we will 
# meet at the head. :)
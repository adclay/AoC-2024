from Puzzle_Input import *

""" -----------------------------------------------------------------------------------------------|
|                                              Part 1                                              |
|----------------------------------------------------------------------------------------------- """

class LinkedList:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
    def add(self, val):
        self.next = LinkedList(val, self.next)
        return self.next
        
    def print(self):
        node = self
        while node != None:
            print(node.val, end = " ")
            node = node.next
        print()

# Initialize linked list
head = LinkedList(stones[0])
node = head
for i in range(1, len(stones)):
    node = node.add(stones[i])

# Apply rules
number_of_stones = len(stones)
for i in range(25):
    node = head
    while node != None:
        # Rule 1
        if node.val == 0:
            node.val = 1
            node = node.next
            continue
        
        # Rule 2
        val, digits = node.val, 0
        while val > 0:
            digits += 1
            val //= 10
        if digits % 2 == 0:
            left, right = node.val // (10 ** (digits // 2)), node.val % (10 ** (digits // 2))
            node.val = left
            node = node.add(right)
            node = node.next
            number_of_stones += 1
            continue
        
        # Rule 3
        node.val *= 2024
        node = node.next
print("Answer to part 1 =", number_of_stones)

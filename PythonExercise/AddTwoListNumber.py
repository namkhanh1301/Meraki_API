class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
    def AddTwoListNumber(self):
        def toInt(node):
            return node.val + 10 * toInt(node.next) if node else 0
        def toList(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = toList(n / 10)
            return node
        
        return toList(toInt(self.l1)) + toList(toInt(self.l2))

print (Solution([1,2,3],[4,5,6]).AddTwoListNumber())
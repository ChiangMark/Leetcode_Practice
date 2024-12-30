class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
                
            tail = tail.next
            
        tail.next = l1 if l1 else l2    
        return dummy.next
        
        
        
def print_list(node):
    """打印鏈表"""
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")
        
if __name__ == "__main__":
    solution = Solution()
    
    # 創建測試用例
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    
    merged_list = solution.mergeTwoLists(list1, list2)
    
    print("Merged List:")
    print_list(merged_list)  # 輸出: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
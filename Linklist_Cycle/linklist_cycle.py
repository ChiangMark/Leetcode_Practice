# 時間複雜度：O(n) 其中n是鏈表的節點數。最壞情況下，我們需要遍歷整個鏈表。
# 空間複雜度：O(1) 只使用了常數的額外空間。

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def hasCycle(head: ListNode) -> bool:
        fast, slow = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
            
        return False
  
    def create_cycle_linked_list():
        # 建立節點
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        
        # 連結節點
        node1.next = node2
        node2.next = node3
        node3.next = node4
        
        # 建立循環：讓最後一個節點指向第二個節點
        node4.next = node2
        
        return node1  # 返回頭節點
    
if __name__ == "__main__":
    # 建立循環鏈結串列
    cycle_list = Solution.create_cycle_linked_list()

    # 驗證是否有循環
    print("是否有循環:", Solution.hasCycle(cycle_list))
    
    
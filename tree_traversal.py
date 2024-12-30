from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def preorder_traversal(root): #root > left > right
    if root is None:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)
    
def inorder_traversal(root): #left > root > right
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

def postorder_traversal(root): # left > right > root
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]
    
def level_order_traversal(root):
    if root is None:
        return []

    queue = deque([root])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

if __name__ == "__main__":
    # 建立一棵簡單的二叉樹
    root = TreeNode(1)                              
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    ###
    #      1
    #    2   3
    #  4   5  
    
    
    # 測試各種遍歷方法
    print("前序遍歷:", preorder_traversal(root))
    print("中序遍歷:", inorder_traversal(root))
    print("後序遍歷:", postorder_traversal(root))
    print("層序遍歷:", level_order_traversal(root))
    
    
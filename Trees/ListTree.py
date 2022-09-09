from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(lst):
    tree_len = len(lst)
    
    validated_lst = lst
    root = TreeNode(lst[0])
    
    deq = deque([root])
    idx = 1
    
    while deq and idx < tree_len:
        node = deq.popleft()
        if str(validated_lst[idx]):
            left_child = validated_lst[idx]
            if left_child:
                node.left = TreeNode(left_child)
                deq.append(node.left)
        
        if not idx+1 == tree_len and validated_lst[idx+1]:
            right_child = validated_lst[idx+1]
            if right_child:
                node.right = TreeNode(right_child)
                deq.append(node.right)
        
        idx += 2
        
    return root
if __name__ == "__main__":
    pass
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, description: List[List[int]]) -> Optional[TreeNode]:
        root=None
        a=set()
        for i in description:
            a.add(i[1])

        for i in description:
            if i[0] not in a:
                root=TreeNode(i[0])
                break

        hash_map={}

        for i in description:
            if i[0] not in hash_map:
                    if i[2]==0:
                        hash_map[i[0]]=[-1,i[1]]
                    else:
                        hash_map[i[0]]=[i[1],-1]
            else:
                if i[2]==0:
                    hash_map[i[0]][1]=i[1]
                else:
                    hash_map[i[0]][0]=i[1]
        st = [root]
        
        while st:
            curr_node = st.pop()
            
            if curr_node.val in hash_map:
                left_val, right_val = hash_map[curr_node.val]
                
                if right_val != -1:
                    curr_node.right = TreeNode(right_val)
                    st.append(curr_node.right)
                    
                if left_val != -1:
                    curr_node.left = TreeNode(left_val)
                    st.append(curr_node.left)
                    
        return root


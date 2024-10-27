'''
Coding Ninja :> https://www.naukri.com/code360/problems/tree-traversal_981269?leftPanelTabValue=PROBLEM

Problem statement
You have been given a Binary Tree of 'N'

nodes, where the nodes have integer values.



Your task is to return the ln-Order, Pre-Order, and Post-Order traversals of the given binary tree.



For example :
For the given binary tree:

The Inorder traversal will be [5, 3, 2, 1, 7, 4, 6].
The Preorder traversal will be [1, 3, 5, 2, 4, 7, 6].
The Postorder traversal will be [5, 2, 3, 7, 6, 4, 1].
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
1 2 3 -1 -1 -1  6 -1 -1
Sample Output 1 :
2 1 3 6 
1 2 3 6 
2 6 3 1
Explanation of Sample Output 1 :
 The given binary tree is shown below:

Inorder traversal of given tree = [2, 1, 3, 6]
Preorder traversal of given tree = [1, 2, 3, 6]
Postorder traversal of given tree = [2, 6, 3, 1]
Sample Input 2 :
1 2 4 5 3 -1 -1 -1 -1 -1 -1
Sample Output 2 :
5 2 3 1 4 
1 2 5 3 4 
5 3 2 4 1
Explanation of Sample Output 2 :
The given binary tree is shown below:

Inorder traversal of given tree = [5, 2, 3, 1, 4]
Preorder traversal of given tree = [1, 2, 5, 3, 4]
Postorder traversal of given tree = [5, 3, 2, 4, 1]
Constraints :
1 <= 'N' <= 10^5
0 <= 'data' <= 10^5     

where 'N' is the number of nodes and 'data' denotes the node value of the binary tree nodes.

Time limit: 1 sec
'''


# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    # Write your code here.
    preOrderRes=[]
    inOrderRes=[]
    postOrderRes=[]

    preOrder(root,preOrderRes)
    inOrder(root,inOrderRes)
    postOrder(root,postOrderRes)


    return [inOrderRes,preOrderRes, postOrderRes]

def preOrder(rootNode,result) :
    
    
    if not rootNode :
        return 
    
    result.append(rootNode.data)
    preOrder(rootNode.left,result)
    preOrder(rootNode.right,result)
    
    
    

def inOrder(rootNode,result) :
    
    if not rootNode :
        return 
    
    inOrder(rootNode.left,result)
    result.append(rootNode.data)
    inOrder(rootNode.right,result)
    

def postOrder(rootNode,result) :
    
    
    if not rootNode :
        return 
    
    postOrder(rootNode.left,result)
    postOrder(rootNode.right,result)
    result.append(rootNode.data)

    
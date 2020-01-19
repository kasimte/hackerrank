# https://www.hackerrank.com/challenges/30-binary-trees/problem
import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):

        # initialize an empty array
        queue = []
        # add the root, if applicable
        if root != None: queue.append(root)

        # repeat this process while we have something
        # in the queue
        while queue:
            # pop off the first node and print it
            node = queue.pop()
            print(node.data, end=" ")

            # then insert the left and right nodes, 
            # in that order. these will go after
            # whatever is already on the queue
            if node.left: queue.insert(0, node.left)
            if node.right: queue.insert(0, node.right)

        
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

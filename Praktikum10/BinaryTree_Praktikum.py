class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def inorderTransversal(self, root):
        res = []
        if root:
            res = self.inorderTransversal(root.left)
            res.append(root.data)
            res = res + self.inorderTransversal(root.right)
        return res

    def preorderTransversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTransversal(root.left)
            res = res + self.preorderTransversal(root.right)
        return res

    def postorderTransversal(self, root):
        res = []
        if root:
            res = self.postorderTransversal(root.left)
            res = res + self.postorderTransversal(root.right)
            res.append(root.data) 
        return res

arr = [97, 77, 117, 67, 87, 107, 127, 82]
nim = Node(arr[0])
for i in arr[1:]:
    nim.insert(i)

print(f"{"{:8}".format("nama")}: Haidar Lathif Abqary Setia Harja")
print(f"{"{:8}".format("NIM")}: J0403251097")
print("="*61)
print(f"{"{:25}".format("in-order Transversal")}:{nim.inorderTransversal(nim)}")
print(f"{"{:25}".format("pre-order Transversal")}:{nim.preorderTransversal(nim)}")
print(f"{"{:25}".format("post-order Transversal")}:{nim.postorderTransversal(nim)}")
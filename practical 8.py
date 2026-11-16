
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    # 1. Insert a new node
    def insert(self, root, data):

        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        else:
            print("Duplicate value is not allowed!")

        return root

    # 2. Find longest path (Height)
    def longest_path(self, root):

        if root is None:
            return 0

        left_height = self.longest_path(root.left)
        right_height = self.longest_path(root.right)

        return 1 + max(left_height, right_height)

    # 3. Find minimum value
    def find_minimum(self, root):

        if root is None:
            return None

        while root.left is not None:
            root = root.left

        return root.data

    # 4. Mirror the tree
    def mirror(self, root):

        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.mirror(root.left)
        self.mirror(root.right)

        return root

    # 5. Search a value
    def search(self, root, key):

        if root is None:
            return False

        if root.data == key:
            return True

        elif key < root.data:
            return self.search(root.left, key)

        else:
            return self.search(root.right, key)

    # Inorder Traversal
    def inorder(self, root):

        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


# Main Program
tree = BST()

while True:

    print("\n\n====== BINARY SEARCH TREE ======")
    print("1. Insert Node")
    print("2. Find Longest Path")
    print("3. Find Minimum Value")
    print("4. Mirror Tree")
    print("5. Search Value")
    print("6. Display Inorder Traversal")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        data = int(input("Enter value to insert: "))
        tree.root = tree.insert(tree.root, data)
        print("Node inserted successfully!")

    elif choice == 2:

        height = tree.longest_path(tree.root)
        print("Number of nodes in longest path:", height)

    elif choice == 3:

        minimum = tree.find_minimum(tree.root)

        if minimum is None:
            print("Tree is empty!")
        else:
            print("Minimum value in BST:", minimum)

    elif choice == 4:

        if tree.root is None:
            print("Tree is empty!")
        else:
            tree.mirror(tree.root)
            print("Tree mirrored successfully!")

    elif choice == 5:

        key = int(input("Enter value to search: "))

        if tree.search(tree.root, key):
            print("Value found in BST!")
        else:
            print("Value not found in BST!")

    elif choice == 6:

        if tree.root is None:
            print("Tree is empty!")
        else:
            print("Inorder Traversal:")
            tree.inorder(tree.root)

    elif choice == 7:

        print("Program terminated successfully!")
        break

    else:
        print("Invalid choice! Please enter a valid option.")

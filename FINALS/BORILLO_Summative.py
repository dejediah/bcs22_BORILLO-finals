# SUMMATIVE FINALS | Borillo, Raphael Jedidiah R. | 202230704
# Coded on 12/14/2023


# creates a class treenode that denotes each node of the tree
class treenode:

    def __init__(self, level):
        self.level = level
        self.left = None
        self.right = None

# defines a leftmost to rightmost vertical traversal function
def LRVerticalOrder(root, dist, lrmap):
    # checks for a root input, if no root, skips this function
    if root is None:
        return

    # appends the current node and its level to the map, except if the node's level is equal to zero
    try:
        lrmap[dist].append(root.level)
    except:
        lrmap[dist] = [root.level]

    # recursively calls function for left and right nodes
    # if the node is on the left of the root, subtracts one from its distance from the root
    # if the node is on the right of the root, adds one to its distance from the root
    LRVerticalOrder(root.left, dist - 1, lrmap)
    LRVerticalOrder(root.right, dist + 1, lrmap)


# defines a rightmost to leftmost vertical traversal function
def RLVerticalOrder(root, dist, rlmap):
    if root is None:
        return
    try:
        rlmap[dist].append(root.level)
    except:
        rlmap[dist] = [root.level]

    # recursively calls function for left and right nodes
    # if the node is on the left of the root, adds one to its distance from the root
    # if the node is on the right of the root, subtracts from to its distance from the root
    RLVerticalOrder(root.left, dist + 1, rlmap)
    RLVerticalOrder(root.right, dist - 1, rlmap)

# prints the value gathered from the LRVerticalOrder function
def printLR(root):
    lrmap = {}
    lrfin = []
    dist = 0
    LRVerticalOrder(root, dist, lrmap)

    print("Left to right vertical order traversal is:")
    for index, value in enumerate(sorted(lrmap)):
        for i in lrmap[value]:
            lrfin.append(i)
    print(str(lrfin))

# prints the value gathered from the RLVerticalOrder function
def printRL(root):
    rlmap = {}
    rlfin = []
    dist = 0
    RLVerticalOrder(root, dist, rlmap)

    print("Right to left vertical order traversal is:")
    for index, value in enumerate(sorted(rlmap)):
        for i in rlmap[value]:
            rlfin.append(i)
    print(str(rlfin))

# reverses the order of the RLVerticalOrder function prints the value gathered, in order to simulate a bottom to top,
# rightmost to leftmost traversal
def reverseRL(root):
    revmap = {}
    revfin = []
    dist = 0
    LRVerticalOrder(root, dist, revmap)

    print("Right to left reverse vertical order traversal is:")
    for index, value in enumerate(sorted(revmap)):
        for i in revmap[value]:
            revfin.append(i)

    print(str(revfin[::-1]))


# defines a function that gathers all print functions into one function
def finalprint(root):
    print()
    printRL(root)
    print("\n")
    printLR(root)
    print("\n")
    reverseRL(root)


# defines the main running function
def main():
    # defines the tree and its children based on the Node class
    root = treenode(1)
    root.left = treenode(2)
    root.right = treenode(3)
    root.left.left = treenode(4)
    root.left.right = treenode(5)
    root.right.left = treenode(6)
    root.right.right = treenode(7)
    root.right.left.right = treenode(8)
    root.right.right.right = treenode(9)

    # prints the introductory tree and statement
    print("""         1
       /   \ 
      /     \   
     2       3
    / \     / \ 
   4   5   6   7
              / \               
             8   9""")

    # gathers user's input for chosen node
    print("Based on the tree above, input the root node that you want in order to find the vertical traversal of its tree. (input number from 0-9)")
    node = int(input("Input: "))

    # case-statements for inputs
    if node == 1:
        finalprint(root)
    elif node == 2:
        finalprint(root.left)
    elif node == 3:
        finalprint(root.right)
    elif node == 4:
        finalprint(root.left.left)
    elif node == 5:
        finalprint(root.left.right)
    elif node == 6:
        finalprint(root.right.left)
    elif node == 7:
        finalprint(root.right.right)
    elif node == 8:
        finalprint(root.right.left.right)
    elif node == 9:
        finalprint(root.right.right.right)

    # input for program loop
    userin = input("\nRun again? (yes/no) \n> ")

    # program loop checker
    if userin.lower() == "yes":
        main()
    else:
        pass

main()

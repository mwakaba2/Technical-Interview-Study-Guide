from nose.tools import assert_equal

def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print(l)

setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))

# Self Check Section 1 ####
x = BinaryTree('a')
insertLeft(x,'b')
insertRight(x,'c')
insertRight(getRightChild(x),'d')
insertLeft(getRightChild(getRightChild(x)),'e')
print(x)


# Self Check Section 2 ####
# build a tree with the following list representation: ['a', ['b', [], ['d', [], []]], ['c', ['e', [], []], ['f', [], []]]
def buildTree():
    tree = BinaryTree('a')
    insertLeft(tree, 'b')
    insertRight(tree, 'c')
    insertRight(getLeftChild(tree), 'd')
    insertLeft(getRightChild(tree), 'e')
    insertRight(getRightChild(tree), 'f') 
    print(tree) 
    return tree  

ttree = buildTree()
assert_equal(getRootVal(getRightChild(ttree)),'c')
assert_equal(getRootVal(getRightChild(getLeftChild(ttree))),'d')
assert_equal(getRootVal(getRightChild(getRightChild(ttree))),'f')
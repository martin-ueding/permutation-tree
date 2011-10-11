paths = [
    [1, 4, 7], [1, 4, 8], [1, 4, 9], [1, 5, 7], [1, 5, 8], [1, 5, 9], [1, 6, 7], [1, 6, 8], [1, 6, 9], [2, 4, 7], [2, 4, 8], [2, 4, 9], [2, 5, 7], [2, 5, 8], [2, 5, 9], [2, 6, 7], [2, 6, 8], [2, 6, 9], [3, 4, 7], [3, 4, 8], [3, 4, 9], [3, 5, 7], [3, 5, 8], [3, 5, 9], [3, 6, 7], [3, 6, 8], [3, 6, 9]
]

class Tree(object):
    def __init__(self, node=0):
        self.node = node
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def toList(self):
        if len(self.children) > 0:
            return "\n".join(["%i -> %i;" % (self.node, x.node)+"\n"+x.toList() for x in self.children])
        else:
            return ""

tree = Tree()

# iterate through the lists
for path in paths:
    subtree = tree

    for value in path:
        # check whether the current value already exists at this position in the tree
        found = False
        for child in subtree.children:
            if value == child.node:
                subtree = child
                found = True
                break

        # attach the leaf to the current position in the tree if needed
        if not found:
            newchild = Tree(node=value)
            subtree.addChild(newchild)
            subtree = newchild

        # use the found or created leaf as a position for the next value in the path-list

print "digraph G {"
print tree.toList()
print "}"


# Binary Trees

## Terms
**Levels** - Each layer in tree is level.

    Children have a higher level than their parents

    Number of connections from lowest leaf to root + 1


**Leaves / External Nodes** - Nodes with no children

**Parent / Internal Node** - Nodes with at least one child

**Node Height** - Number of edges between it and furthest leaf in tree

    Leaves have a height of 0

    Inverse of Node Depth

**Tree Height** - Height of root node

**Node Depth** - Number of edges from the node to the root

    Root has a depth of 0

    Inverse of Node Height

## Binary Search Trees

All operations, insertion, deletion, and lookup take O(h) time.

Where h is the height of the tree.

However when a binary search tree is balanced, the height is equal to log(n)

Where n is the number of nodes in the tree.

### AVL Trees

For a node to be considered balanced, the heights of their left and right children should not differ by more than 1

`Height(node) = 1 + max(Height(node.left), Height(node.right))`

Algorithm for finding if node is balanced

`Node.isBalanced = abs(node.left.height - node.right.height) <= 1`

#### Rotations


```
Balanced Tree

             Y      <- 3 Balanced: abs(2-2) <= 1
           /   \
          X     Z   <- 2 Balanced: abs(1-1) <= 1
         / \   / \
        *   * *   * <- 1 Balanced: abs(0-0) <= 1
```


##### Left Rotation on Unbalanced Node


```

                X        <- 4  Unbalanced: abs(1-3) > 1
               / \
       1 ->   *   Y      <- 3  Balanced: abs(1-2) <= 1
                 / \
       1 ->     *   Z    <- 2  Balanced: abs(1-1) <= 1
                   / \
       1 ->       *   *  <- 1
```


Use when right child height - left child height > 1

Right Child gets moved up to current node's place

* Unbalanced node's parent pointer gets pointed to right child
* Right child's left pointer gets pointed to unbalanced node
* Right child's left child becomes unbalanced node's right child

##### Right Rotation on Unbalanced Node

```

    Unbalanced: abs(3-1) > 1  4 ->        Z
                                         / \
    Balanced: abs(3-1) > 1    3 ->      Y   *  <- 1
                                       / \
    Balanced: abs(3-1) > 1    2 ->    X   *    <- 1
                                     / \
                              1 ->  *   *      <- 1
```

Use when left child height - right child height > 1

Left Child gets moved up to current node's place

* Unbalanced node's parent pointer gets pointed to right child
* Left child's right pointer gets pointed to unbalanced node
* Left child's right child gets pointed to unbalanced node's left child


#### Insertions

#### Left Left
```
          Z
         / \
        Y   *
       / \
      X   *
     / \
    *   *

Perform Right Rotation on Z Node

          X
        /   \
       Y     Z
      / \   / \
     *  *  *   *

```
#### Left Right
```
          Z
         / \
        Y   *
       / \
      *   X
         / \
        *   *
 Perform Left Rotation on Y Node

          Z
         / \
        X   *
       / \
      Y   *
     / \
    *   *
 Perform Right Rotation on Z

          X
        /   \
       Y     Z
      / \   / \
     *  *  *   *

```
#### Right Right
```
          Z
         / \
        *   Y
           / \
          *   X
             / \
            *   *

Perform Left Rotation on Z Node

          X
        /   \
       Y     Z
      / \   / \
     *  *  *   *

```
#### Right Left
```
          Z
         / \
        *    Y
            / \
           X   *
          / \
         *   *
 Perform Right Rotation on Y Node

          Z
         / \
        *   X
           / \
          *   Y
             / \
            *   *
 Perform Left Rotation on Z

          X
        /   \
       Y     Z
      / \   / \
     *  *  *   *

```

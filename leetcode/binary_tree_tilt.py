def findTilt(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    leftTilt = 0
    rightTilt = 0
    if root.left:
        leftTilt = findTilt(root.left)
    if root.right:
        rightTilt = findTilt(root.right)
    return abs(leftTilt - rightTilt)
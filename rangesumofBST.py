class solution: 
  def rangesumofBST (self, root, L, R):
    if not root:
      return 0;
    if R < root.val:
     return self.ranfesumofBST(root.left, L, R)
    elif L > root.val:
      return self.rangesumofBST(root.right, L, R)
    else:
      return self.rangesumofBST(root.val + rangesumofBST(left.root, L,R) + rangesumofBST(rght.root, L, R)
              

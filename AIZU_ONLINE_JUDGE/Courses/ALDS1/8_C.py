from typing import Optional
from sys import stdin

input = stdin.readline

# Nodeクラスは以下のように定義されているとします
class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class BST:
  def __init__(self):
    # 初めはノードがないのでNoneを入れておく
    self.root = None

  # 探索
  def search(self, x: int) -> Optional[Node]:
    node = self.root
    while node:
      if node.val == x:
        return node
      elif x < node.val:
        node = node.left
      else: # x > node.val
        node = node.right

    # 見つからなったためNoneを返す
    return None

  # 挿入
  def insert(self, x: int) -> Optional[Node]:
    new_node = Node(x)
    # まだ１つもノードないのでnew_nodeをrootにする
    if not self.root:
       self.root = new_node
       return new_node

    # 新しいノードの親となるノードを探す
    parent = None
    node = self.root
    while node:
      # そもそも値xのノードが存在していたためそれを返す
      if node.val == x:
        return node
      elif x < node.val:
        parent = node
        node = node.left
      else: # x > node.val
        parent = node
        node = node.right

    if x < parent.val:
      parent.left = new_node
    else: # x > node.val
      parent.right = new_node

    return new_node

  # 探索のコードを少し変える
  # 見つけたノード、その親ノード、親ノードの左右どちらについているか　を返しようにする
  # 親ノードの左についていた場合をtrueとする
  def searchForRemove(self, x: int) -> tuple[Optional[Node], Optional[Node], bool]:
    parent = None
    isLeft = False
    node = self.root
    while node:
      if node.val == x:
        return node, parent, isLeft
      elif x < node.val:
        parent = node
        isLeft = True
        node = node.left
      else: # x > node.val
        parent = node
        isLeft = False
        node = node.right

    # 見つからなった
    return None, None, False

  # 削除のパターン３用のヘルパー関数
  # あるノード以下で最も左に位置するノードとその親ノードを探索する
  def getLeftestNode(self, node: Optional[Node]) -> tuple[Optional[Node], Optional[Node]]:
    if not node:
      return None, None

    parent = None
    leftestNode = node
    while leftestNode.left:
      parent = leftestNode
      leftestNode = leftestNode.left

    return leftestNode, parent

  # 削除
  def remove(self, x):
    node, parent, isLeft = BST.searchForRemove(self, x)
    # そもそも削除対象が存在しなかった
    if not node:
      return

    # パターン１　子ノードがない
    if (not node.left) and (not node.right):
      # 親がない、つまりrootを削除する
      # この場合rootにも子がないので、そもそもこの二分探索木のノード数は1以下
      # よってrootをNoneで置き換える
      if not parent:
        self.root = None
        return

      # ノードを削除、つまりNoneと置き換える
      if isLeft:
        parent.left = None
      else:
        parent.right = None

    # パターン２　左右のどちらかに子ノードを持つ
    elif (not node.left) or (not node.right):
      child = node.left or node.right
      # 親がない、つまりrootを削除する
      # この場合子ノードがそのままrootになる
      if not parent:
        self.root = child
        return

      # ノードを削除し、子ノードと置き換える
      if isLeft:
        parent.left = child
      else:
        parent.right = child

    # パターン３　左右どちらにも子ノードを持つ
    else:
      left, right = node.left, node.right

      # rightLeftestNodeはnodeの右の部分木のうち最も左にあるノード
      # そもそもright != None なので、rightLeftestNodeは必ず存在する
      rightLeftestNode, rightLeftestNodeParent = BST.getLeftestNode(self, right)
      if not rightLeftestNodeParent:
        # rightLeftestNodeParentが存在しないということは、
        # rightLeftestNode == rightで、この場合親のrightLeftestNodeParentはnodeとなる
        rightLeftestNodeParent = node

      # 上の図の例でいうと62の左に58をつける操作
      # rightLeftestNodeは高々１つの子を持血、持つ場合は右のみ
      rightLeftestNodeParent.left = rightLeftestNode.right

      # nodeのleftとrightをleftRightestNodeにつける
      # 注意すべきはrightLeftestNodeがrightのとき
      # このときはleftのみをつなげる（当たり前だがrightをつなげると自己参照になってしまう）
      if rightLeftestNode == right:
        rightLeftestNode.left = left
      else:
        rightLeftestNode.left, rightLeftestNode.right = left, right

      # 親がない、つまりrootを削除する
      # この場合rightLeftestNodeがそのままrootになる
      if not parent:
        self.root = rightLeftestNode
        return

      if isLeft:
        parent.left = rightLeftestNode
      else:
        parent.right = rightLeftestNode

    return


def preOrder(root):
  pre_order_output = []
  def dfs(node: Node):
    if not node:
      return

    pre_order_output.append(node.val)
    dfs(node.left)
    dfs(node.right)

  dfs(root)
  return pre_order_output

def inOrder(root):
  in_order_output = []
  def dfs(node: Node):
    if not node:
      return

    dfs(node.left)
    in_order_output.append(node.val)
    dfs(node.right)

  dfs(root)
  return in_order_output

def print_order(order):
  print(" " + " ".join([str(num) for num in order]))

N = int(input().rstrip())
bst = BST()
while N:
  query = list(map(str, input().rstrip().rsplit()))
  if query[0] == "find":
    if bst.search(int(query[1])):
      print("yes")
    else:
      print("no")
  elif query[0] == "insert":
    bst.insert(int(query[1]))
  elif query[0] == "delete":
    bst.remove(int(query[1]))
  elif query[0] == "print":
    print_order(inOrder(bst.root))
    print_order(preOrder(bst.root))

  N -= 1

class Node:
  def __init__(self, height, key, x):
    self.height = height # そのノードを根とする部分木の高さ
    self.key = key       # そのノードのキー
    self.val = x         # そのノードの値
    self.left = None     # 左部分木
    self.right = None    # 右部分木

# 部分木 t の高さを返す
def height(t): return 0 if t is None else t.height

# 左右の部分木の高さの差を返す。左が高いと正、右が高いと負
def bias(t): return height(t.left) - height(t.right)

# 左右の部分木の高さから、その木の高さを計算して修正する
def modifyHeight(t): t.height = 1 + max(height(t.left), height(t.right))

def rotateL(v): # ２分探索木 v の左回転。回転した木を返す
  u = v.right; t2 = u.left
  u.left = v; v.right = t2
  modifyHeight(u.left)
  modifyHeight(u)
  return u

def rotateR(u): # ２分探索木 u の右回転。回転した木を返す
  v = u.left; t2 = v.right
  v.right = u; u.left = t2
  modifyHeight(v.right)
  modifyHeight(v)
  return v

def rotateLR(t): # ２分探索木 t の二重回転(左回転 -> 右回転)。回転した木を返す
  t.left = rotate(t.left)
  return rotateR(t)

def rotateRL(t): # ２分探索木 t の二重回転(右回転 -> 左回転)。回転した木を返す
  t.right = rotateR(t.right)
  return rotateL(t)


class AVL:
  def __init__(self):
    self.root = None     # AVL木の根。Node 型
    self.change = False  # 修正が必要かを示すフラグ(True:必要, False:不要)
    self.lmax_key = None # 左部分木のキーの最大値
    self.lmax_val = None # lmax に対応する値

    # 挿入時の修正(balanceLi:左部分木への挿入, balanceRi:右部分木への挿入)
    def balanceLi(self, t): return self.balanceL(t)
    def balanceRi(self, t): return self.balanceR(t)

    # 削除時の修正(balanceLd:左部分木での削除, balanceRd:右部分木での削除)
    def balanceLd(self, t): return self.balanceR(t)
    def balanceRd(self, t): return self.balanceL(t)

    # 部分木 t のバランスを回復して戻り値で返す
    # 左部分木への挿入に伴うAVL木の修正
    # 右部分木での削除に伴うAVL木の修正
    def balanceL(self, t):
      if not self.change: return t
      h = height(t)
      if bias(t) == 2:
        if bias(t.lst) >= 0:
          t = rotateR(t)
        else:
          t = rotateLR(t)
      else: modifyHeight(t)
      self.change = (h != height(t))
      return t

    # 部分木 t のバランスを回復して戻り値で返す
    # 右部分木への挿入に伴うAVL木の修正
    # 左部分木での削除に伴うAVL木の修正
    def balanceR(self, t):
      if not self.change: return t
      h = height(t)
      if bias(t) == -2:
        if bias(t.right) <= 0:
          t = rotateL(t)
        else:
          t = rotateRL(t)
      else: modifyHeight(t)
      self.change = (h != height(t))
      return t

    # エントリー(key, x のペア)を挿入する
    def insert(self, key, x): self.root = self.insert_sub(self.root, key, x)

    def insert_sub(self, t, key, x):
      if t is None:
        self.change = True
        return Node(1, key, x)
      elif key < t.key:
        t.left = self.insert_sub(t.left, key, x)
        return self.balanceLi(t)
      elif key > t.key:
        t.right = self.insert_sub(t.right, key, x)
        return self.balanceRi(t)
      else:
        self.change = False
        t.val = x
        return t

    # key で指すエントリー(ノード)を削除する
    def delete(self, key): self.root = self.delete_sub(self.root, key)

    def delete_sub(self, t, key):
      if t is None:
        self.change = False
        return None
      elif key < t.key:
        t.left = self.delete_sub(t.left, key)
        return self.balanceLd(t)
      elif key > t.key:
        t.right = self.delete_sub(t.right, key)
        return self.balanceRd(t)
      else:
        if t.left is None:
          self.change == True
          return t.right # 右部分木を昇格させる
        else:
          t.left = self.delete_max(t.left) # 左部分木の最大値を削除する
          t.key = self.lmax_key # 左部分木の削除した最大値で置き換える
          t.val = self.lmax_val
          return self.balancedLd(t)

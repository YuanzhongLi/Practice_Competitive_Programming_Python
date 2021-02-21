### 1. permutations
itertoolsのpermutationsを使用
```
from itertools import permutations
```
[link](./permutations.py)

### 2. gcd
mathのgcdを使用
```
from math import gcd
```

### 3. ascii
```
ord('a')
# result
# 97

chr(97)
# result
# 'a'
```
### 4. list操作
```
# pop back
li.pop(-1)
```

#### 4-1. sort
```
# use cmp_to_key
from functools import cmp_to_key
points.sort(key=cmp_to_key(lambda a, b: (a[0]**2 + a[1]**2) - (b[0]**2 + b[1]**2)))

# only use lambda
points.sort(key=lambda a: a[0]**2+a[1]**2)

# part sort (reverse)        
ary[2:8] = sorted(ary[2:8])
```

#### 4-2. reversed(array) return iterator!
```
A = [1,2,3]
A_rev = list(reversed(A))
# A_rev = [3, 2, 1]
```

#### 4-3. compare関数
functoolsのcmp_to_keyを使用
```
from functools import cmp_to_key
```
[link](./compare_function.py)

#### 4-4. 文字列操作
基本的にはlist(deque)に変換した方がよい

#### 4-5. 文字列判定
```
文字列が十進数字か判定: str.isdecimal()
文字列が数字か判定: str.isdigit()
文字列が数を表す文字か判定: str.isnumeric()
文字列が英字か判定: str.isalpha()
文字列が英数字か判定: str.isalnum()
文字列がASCII文字か判定: str.isascii()
```

### 5. object 操作
#### 5-1. object.get(key, default)でkeyの存在判定
```
d = {}
d['a'] = 1
print(d['a'])
# 1
print(d.get('b', None))
# None
```

#### 5-2. OrderedDict # double linked list + hashmap
```
from collections import OrderedDict
od = OrderdDict()
# key-valueのペアを末尾に移動 (O(1))
od.move_to_end(key)
# key-valueのペアを先頭に移動 (O(1))
od.move_to_end(key, False)
```

#### 5-3. deque 注意
can not use slice!
```
deque[2:8] is Error!
```

### 5-4. 配列の参照範囲
```
a = [[1, 2], [3, 4]]
for ele in a:
  ele = [2, 4]
print(a)
# result [[1, 2], [3, 4]]
# eleに[2, 4]という配列を再代入

a = [[1, 2], [3, 4]]
for ele in a:
  ele[0] *= 2
  ele[1] *= 2
print(a)
# result [[2, 4], [3, 4]]
# eleというpointerの[0]と[1]の値を更新
```

### 6. グローバル変数
通常のスコープ
```
a = 2
def func(x):
    global a
    a = 10
    return x+a
```

関数内関数
```
# nonlocalを使用
def outer():
    var = 'Initial Var'
    def inner():
        nonlocal var
        var = 'New Var'
        return(var)

# globalを使用  
def outer():
    global var
    var = 'Initial Var'

    def inner():
        global var
        var = 'New Var'
        return(var)  
```

### 7.bisect
bisect_left: lower_bound 
bisect_right: upper_bound
```
from bisect import bisect_left
# A: array
bisect_left(A, value)
```

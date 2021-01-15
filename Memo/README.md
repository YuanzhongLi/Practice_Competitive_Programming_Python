### compare関数
functoolsのcmp_to_keyを使用
```
from functools import cmp_to_key
```
[link](./compare_function.py)

### permutations
itertoolsのpermutationsを使用
```
from itertools import permutations
```
[link](./permutations.py)

### gcd
mathのgcdを使用
```
from math import gcd
```

### ascii
```
ord('a')
# result
# 97

chr(97)
# result
# 'a'
```
### list操作
```
# pop back
li.pop(-1)
```

#### 文字列操作
基本的にはlistに変換した方がよい

### object 操作
#### object.get(key, default)でkeyの存在判定
```
d = {}
d['a'] = 1
print(d['a'])
# 1
print(d.get('b', None))
# None
```

#### OrderedDict # double linked list + hashmap
```
from collections import OrderedDict
od = OrderdDict()
# key-valueのペアを末尾に移動 (O(1))
od.move_to_end(key)
# key-valueのペアを先頭に移動 (O(1))
od.move_to_end(key, False)
```

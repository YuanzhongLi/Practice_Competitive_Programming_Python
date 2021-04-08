class A:
  def __init__(self, a, b=None):
    self.a = a
    self.b = b

  def __pr__(self):
    return str(a) + " " + str(B)

class B:
  def __init__(self, val):
    self.val = val

  def __pr__(self):
    return "B"

  def f(self, ele):
    ele.b =  self

a = A(1)
b = B(20)
b.f(a)
print(a)
print(a.b.val)

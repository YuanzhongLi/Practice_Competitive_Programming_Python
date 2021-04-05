### easy
def f(x):
  if x % 15 == 0:
      return "FizzBuzz"
  elif x % 5 == 0:
      return "Buzz"
  elif x % 3 == 0:
      return "Fizz"
  else:
      return str(x)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
      ret = []
      for i in range(1, n+1):
          ret.append(f(i))
      return ret

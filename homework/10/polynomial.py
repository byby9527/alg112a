import random

def neighbor(f, x, h):
  x += random.uniform(-h, h)
  return f(x), x

def hillClimbing(f, x, h = 0.01, maxIter = 10000):
  x = x
  print("初始值：", x)
  while True:
    fnow = f(x)
    fneighbor, newx = neighbor(f, x, h)
    print("x=", x, "f(x)=", fnow)

    if fneighbor < fnow:
      x = newx
      print("更新值：", x)
    else:
      if maxIter <= 0:
        print("無實數解")
        return
      maxIter -= 1
  return x

def f(x):
  return x**3 - 1

x = hillClimbing(f, 0)

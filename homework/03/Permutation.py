def perm(n):
  p = [i for i in range(n)]

  perm_a(p, 0)

def perm_a(p, i):
  if i == n:
    print(p)
    return

  for j in range(i, n):
    # 將元素交換到目前位置
    p[i], p[j] = p[j], p[i]
    # 繼續遞迴
    perm_a(p, i + 1)
    
    # 將元素交換回來
    p[i], p[j] = p[j], p[i]

n = int(input("請輸入元素個數："))
perm(n)

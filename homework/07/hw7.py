from micrograd.engine import Value
# 初始化變數
a = Value(2.0)
b = Value(1.0)
c = Value(3.0)

# 訓練迴圈
for _ in range(1000):  # 迭代次數
    # 定義目標函數
    f = a**2 + b**2 + c**2

    # 印出當前變數值和目標函數值
    print("a=", a.data, "b=", b.data, "c=", c.data, "f=", f.data)

    # 反向傳播計算梯度
    f.backward()

    # 檢查是否收斂
    if a.grad < 0.001 and b.grad < 0.001 and c.grad < 0.001:
        break

    # 使用梯度下降更新參數
    a -= a.grad * 0.01
    b -= b.grad * 0.01
    c -= c.grad * 0.01
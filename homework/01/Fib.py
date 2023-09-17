def fibonacci(n):
    a, b = 0, 1  # 初始化前兩個費波那契數字
    if n <= 1:
        return n
    for i in range(2, n + 1):
        next_fib = a + b  # 計算下一個費波那契數字
        a, b = b, next_fib  # 更新 a 和 b，將 b 賦值為下一個費波那契數字

    return b
try:
    n = int(input("請輸入數字: "))
    
    if n < 0:
        print("請輸入大於等於 0 的數字。")
    else:
        result = fibonacci(n)
        print(f"第 {n} 個費波那契數字是: {result}")

except ValueError:
    print("請輸入有效的整數。")

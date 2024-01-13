import random
import copy

def neighbor(f, p, h):
    # 在每個元素上添加隨機值來生成鄰近解
    for i in range(len(p)):
        p[i] += random.uniform(-h, h)
    # 新解的目標函數值
    return f(p), p

def hillClimbing(f, p, h=0.01, maxIter=10000):
    # 用來追蹤連續失敗迭代的計數器
    failCount = 0

    # 迭代直到達到最大迭代次數
    while failCount < maxIter:
        # 當前解的目標函數值
        fnow = f(p)

        # 生成鄰近解並評估其目標函數值
        fneighbor, newp = neighbor(f, copy.copy(p), h)

        # 檢查鄰近解是否優於當前解
        if fneighbor > fnow:
            p = newp
            print('p=', p, 'f(p)=', fneighbor)
            failCount = 0  # 在發現改進時重置 failCount
        else:
            failCount += 1  # 當未發現改進時增加 failCount

    # 返回最終解及其目標函數值
    return p, fnow

def f(p):
    return -1 * (p[0]**2 + p[1]**2 + p[2]**2)

result = hillClimbing(f, [2, 1, 3])
print("最終結果:", result)




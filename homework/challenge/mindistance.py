def min_edit_distance_recursive(str1, str2, memo=None):
    if memo is None:
        memo = {}

    # 如果其中一個字串為空，返回另一個字串的長度
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)

    # 檢查是否已經計算過這個子問題
    if (str1, str2) in memo:
        return memo[(str1, str2)]

    # 如果兩個字串的最後一個字元相同，則跳過最後一個字元，繼續比較前面的字串
    if str1[-1] == str2[-1]:
        result = min_edit_distance_recursive(str1[:-1], str2[:-1], memo)
    else:
        # 否則，進行插入、刪除、替換操作，選擇最小的編輯距離
        insert_cost = 1 + min_edit_distance_recursive(str1, str2[:-1], memo)
        delete_cost = 1 + min_edit_distance_recursive(str1[:-1], str2, memo)
        replace_cost = 1 + min_edit_distance_recursive(str1[:-1], str2[:-1], memo)
        result = min(insert_cost, delete_cost, replace_cost)

    # 將結果存入memo，避免重複計算
    memo[(str1, str2)] = result
    return result

# 測試
str1 = "ATGCAATCCC"
str2 = "ATGATCCG"
result = min_edit_distance_recursive(str1, str2)
print(f"最小編輯距離為：{result}")


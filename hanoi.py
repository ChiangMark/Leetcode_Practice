def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"將圓盤 1 從 {source} 移動到 {target}")
        return
    # 將 n-1 個圓盤從源杆移動到輔助杆
    hanoi(n - 1, source, auxiliary, target)
    # 將第 n 個圓盤從源杆移動到目標杆
    print(f"將圓盤 {n} 從 {source} 移動到 {target}")
    # 將 n-1 個圓盤從輔助杆移動到目標杆
    hanoi(n - 1, auxiliary, target, source)

# 測試函數
n = 3  # 可以改變這裡的數字來測試不同數量的圓盤
hanoi(n, 'A', 'C', 'B')
def fibonacci_space_optimized(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

# 測試
n = 3
print(f"費波那契數列的第 {n} 項是: {fibonacci_space_optimized(n)}")
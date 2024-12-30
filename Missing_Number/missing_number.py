# method 1 > Math
class Solution1: 
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        excepted_number = (n * (n + 1)) // 2
        actually_number = sum (nums)
        
        result = excepted_number - actually_number
        return result    
    
# method 2
class Solution2:
    def missingNumber(self, nums: list[int]) -> int:
        missing_num = len(nums)
        for i, num in enumerate(nums):
            missing_num ^= i ^ num
        return missing_num
    

# 測試函數
def run_tests():
    test_cases = [
        ([3, 0, 1], 2),           # 測試用例 1: 缺少數字 2
        ([0, 1], 2),              # 測試用例 2: 缺少數字 2
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),  # 測試用例 3: 缺少數字 8
        ([0], 1),                 # 測試用例 4: 缺少數字 1
        ([1], 0),                 # 測試用例 5: 缺少數字 0
    ]

    solution1 = Solution1()
    solution2 = Solution2()

    print("Testing Solution1 (Math Method):")
    for nums, expected in test_cases:
        result = solution1.missingNumber(nums)
        print(f"Input: {nums}, Expected: {expected}, Result: {result}, Pass: {result == expected}")

    print("\nTesting Solution2 (XOR Method):")
    for nums, expected in test_cases:
        result = solution2.missingNumber(nums)
        print(f"Input: {nums}, Expected: {expected}, Result: {result}, Pass: {result == expected}")


if __name__ == "__main__":
    run_tests()
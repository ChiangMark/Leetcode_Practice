class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        j = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
                
        return j + 1

if __name__ == "__main__":
    solution = Solution()
    
    # 測試用例
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    new_length = solution.removeDuplicates(nums)
    
    print("New length:", new_length)          # 輸出: New length: 5
    print("Modified array:", nums[:new_length])  # 輸出: Modified array: [0, 1, 2, 3, 4]
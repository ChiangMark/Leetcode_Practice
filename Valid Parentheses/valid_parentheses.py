class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():
               stack.append(char)
            elif char in mapping.keys():
                if not stack or stack[-1] != mapping[char]:
                   return False               
                stack.pop()
                
        return not stack
            
            

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True)
    ]
    
    for s, expected in test_cases:
        result = solution.isValid(s)
        assert result == expected, f"Test failed for input {s}: expected {expected}, got {result}"
    
    print("所有測試通過！")
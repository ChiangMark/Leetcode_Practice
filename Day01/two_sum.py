target = 5
nums = [3,2,4]

def for_loop_solution(array):
    k = 0
    for i in array:
        k += 1
        if target - i in array[k:]:
            return(k - 1, array[k:].index(target - i) + k)
        
def hash_method(array):
    pass

print(for_loop_solution(nums))
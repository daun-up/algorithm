# def cmp(a, b):
#     if a + b > b + a:
#         return True   # a가 앞에 와야 함
#     else:
#         return False  # b가 앞에 와야 함

def solution(numbers):
    nums = list(map(str, numbers))
    
    nums.sort(key = lambda x : x*3, reverse=True)
    
    return str(int(''.join(nums)))

#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if not cmp(nums[i], nums[j]):
#                 nums[i], nums[j] = nums[j], nums[i]

#     answer = ''.join(nums)
    
    # return '0' if answer[0] == '0' else answer

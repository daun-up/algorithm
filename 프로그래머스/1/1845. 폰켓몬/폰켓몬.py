from itertools import combinations
def solution(nums):
    answer = 0
    
    n = len(nums) // 2
    
    unique = len(set(nums))
    
#     tmp = []
    
#     for c in combinations(set(nums), n):
#         tmp.append(c)
        
#     answer = len(tmp)
    
    return min(n,unique)
    
    # tmp = []
    # # 최대한 다양한 종류의 폰켓몬, n/2 마리
    # for i in combinations(nums, len(nums)//2):
    #     tmp.append(i)
    # print(set(tmp))
    
    # 고를 수 있는 폰켓몬의 '종류' 를 구하는 거임! 조합의 수가 아니라!
    return answer

from collections import Counter
def solution(k, tangerine):
    answer = 0
    total = 0
    
    size_count = Counter(tangerine)
    # Counter({'apple': 3, 'banana': 2, 'orange': 1})
    # size_cnt.sort(size_cnt.values(), reverse=True)
    counts = sorted(size_count.values(), reverse=True)
    
    for count in counts:
        total += count
        answer += 1
        if total >= k:
            break
    
#     for i in size_cnt:
#         if total > k:
#             total += i.values()
#             answer += 1
#         else:
#             break
            
    return answer
def solution(phone_book):
    answer = True
    hash = {}
    
    for phone_number in phone_book:
        hash[phone_number] = 1
    
    for phone_number in phone_book:
        tmp = ''
        for num in phone_number:
            tmp += num
            
            if tmp in hash and tmp != phone_number:
                answer = False
            
            
        
    return answer


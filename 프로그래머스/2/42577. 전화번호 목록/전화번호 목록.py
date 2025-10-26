def solution(phone_book):
    answer = True
    # for i in range(0,len(phone_book)):
    #     for j in range(i+1, len(phone_book)):
    #         if phone_book[j].startswith(phone_book[i]):
    #             answer = False
    
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
        
    return answer
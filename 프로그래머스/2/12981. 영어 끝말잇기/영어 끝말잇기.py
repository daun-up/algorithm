def solution(n, words):
    answer = []
    # 탈락하게 되는 경우
    # 1. 잘못된 알파벳으로 시작하는 단어를 말한 경우
    # 2.  말했던 단어를 말한 경우
    
    checked = [words[0]]
    
    for i in range(1,len(words)) :
        if words[i-1][-1] == words[i][0] and words[i] not in checked:
            checked.append(words[i])
        else :
            return [(i%n)+1,(i//n)+1]
            
    return [0,0]


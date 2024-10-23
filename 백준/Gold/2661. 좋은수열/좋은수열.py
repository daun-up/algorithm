def is_good_sequence (seq) :
    length = len(seq)
    for i in range(1, length) :
        if seq[-i:] == seq[-2 * i : -i] :
            return False
    return True

def backtracking (res, n) :
    if len(res) == n :
        print(''.join(map(str, res)))
        exit(0)
    for i in range(1, 4) :
        res.append(i)
        if is_good_sequence(res) :
            backtracking(res, n)
        res.pop()
        
n = int(input())
backtracking([],n)
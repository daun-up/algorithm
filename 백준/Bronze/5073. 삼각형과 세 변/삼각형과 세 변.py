while True :
    length = sorted(list(map(int,input().split())))
    
    if length[0] == length[1] == length[2] == 0:
        break

    if length[1] + length[0] <= length[2] :
        print("Invalid")
    elif length [0] == length[1] == length[2] :
        print("Equilateral")
    elif length[0] == length[1] or length[1] == length[2] or length[0] == length[2] :
        print("Isosceles")
    elif length[0] != length[1] != length[2] :
        print("Scalene")
    

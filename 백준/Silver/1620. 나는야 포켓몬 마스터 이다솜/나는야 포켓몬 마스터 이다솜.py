n, m = map(int, input().split())

names = {}


for i in range(1,n+1):
    name = input() 
    names[i] = name
    names[name] = i    

    
for j in range(1,m+1):
    problem = input()  
    if problem.isdigit() :
        print(names[int(problem)])
    else :
        # print(names(problem))
        print(names[problem])
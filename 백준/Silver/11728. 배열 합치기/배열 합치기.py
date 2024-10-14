a, m = map(int,input().split())
list_a = list(map(int,input().split()))
list_b = list(map(int,input().split()))

answer = []

answer += list_a
answer += list_b
print(*(sorted(answer)))
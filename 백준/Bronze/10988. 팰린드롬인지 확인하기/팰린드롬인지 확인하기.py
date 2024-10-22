def is_palindrome(s, start, end):
    if start >= end:
        return 1
    if s[start] != s[end]:
        return 0
    # 양 끝 문자가 같으면 안쪽 문자열을 재귀적으로 확인
    return is_palindrome(s, start + 1, end - 1)

s = input().strip()

print(is_palindrome(s, 0, len(s) - 1))
import sys
input = sys.stdin.readline


def check_palindrome(w, k):
    if k > 3:
        return k

    left, right = 0, len(w) - 1
    while left < right:
        if w[left] == w[right]:
            left += 1
            right -= 1
        else:
            return min(check_palindrome(w[left+1:right+1], k + 1), check_palindrome(w[left:right], k + 1))

    return k


w = input().strip()
result = check_palindrome(w, 0)
print(result if result < 4 else -1)
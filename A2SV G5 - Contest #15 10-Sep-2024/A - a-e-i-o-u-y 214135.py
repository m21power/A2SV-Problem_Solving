# Problem: A - a-e-i-o-u-y - https://codeforces.com/gym/522079/problem/A

import sys
input = sys.stdin.readline

N = int(input())
word = input()

answer = []
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
for char in word:
    if answer and answer[-1] in vowels and char in vowels:
        continue
    answer.append(char)
print(*answer, sep="")
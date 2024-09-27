S = input().lower()
cnt = [0] * 26

for char in S:
    if 'a' <= char <= 'z':
        cnt[ord(char) - ord('a')] += 1

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(chr(cnt.index(max(cnt)) + ord('A')))
a, b = map(int, input().split())
ans = ""
if a > b: ans = ">"
elif a < b: ans = "<"
else: ans = "=="
print(ans)
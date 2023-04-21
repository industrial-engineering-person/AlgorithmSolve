from collections import deque
n = int(input())
q = deque()
for i in range(1, n+1):
    q.append(i)

length = n
while n != 1:
    q.popleft()
    n -= 1
    if n == 1:
        break
    else:
        q.append(q.popleft())
print(q[0])

import math

A, B, V = map(int, input().split())
# days = 0
# while True:
#     days += 1
#     V -= A
#     if V <= 0:
#         break
#     V += B
# print(days)

print(math.ceil((V - A) / (A - B)) + 1)
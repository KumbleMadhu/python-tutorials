a1 = input()
b1 = set(input().split())
a2 = input()
b2 = set(input().split())
uni = b1.union(b2)
print(len(uni))


x1 = input()
y1 = set(input().split())
x2 = input()
y2 = set(input().split())
inct = y1.intersection(y2)
print(len(inct))
# Enter your code here. Read input from STDIN. Print output to STDOUT
a1 = input()
b1 = set(input().split())
a2 = input()
b2 = set(input().split())
uni = b1.difference(b2)
print(len(uni))

a1 = input()
b1 = set(input().split())
a2 = input()
b2 = set(input().split())
sd = b1.symmetric_difference(b2)
print(len(sd))

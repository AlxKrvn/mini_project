n = input()
a = len(n)
n = n[:(a-5)] + n[:-6:-1]
print(n)
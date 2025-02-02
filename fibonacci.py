# fibonacci
n = int(input("nhap khoang gioi han fibonacci: "))
so = []
so.append(0)
so.append(1)
# print(so[1])
i = 2
while True:
    newnum = so[i-1] + so[i-2]
    if newnum <= n:
        so.append(newnum)
        i = i + 1
    else: break
for j in so:
    if not j == 0:
        print(j)
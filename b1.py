
ss = int(input())

inp_data = ss
d = ss // 86400
ss = ss % 86400
h = ss // 3600
ss = ss % 3600
m = ss // 60
s = ss % 60
out = []

if d != 0:
    out.append(f"{d}d")
if h != 0:
    out.append(f"{h}h")
if m != 0:
    out.append(f"{m}m")
if s != 0:
    out.append(f"{s}s")
" ".join(out)

print(f"{inp_data}s = ", end="")
for i in out: print(i, end=" ")

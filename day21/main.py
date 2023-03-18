lst = ["zone", "abigail", "theta", "form", "libe", "zas"]
k = 2

new = []

for i in range(0, len(lst)-k+1):
    s = ''.join(lst[i:i+k])
    new.append(s)

mx = len(new[0])
for s in new:
    if len(s) > mx:
        mx = len(s)
for s in new:
    if len(s) == mx:
        print(s)
        break

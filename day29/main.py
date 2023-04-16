""" d = {}

for ch in s:
    d[ch] = d.get(ch, 0) + 1


lst = []

for ch in "ACGT":
    if ch in d:
        lst.append(d[ch])
    else:
        lst.append(0)

print(' '.join(map(str, lst))) """

distance = int(input())
time = int(input())
velocity = int(input())
fuel = int(input())
fuel_consumption = int(input())

con1 = velocity * time < distance
con2 = fuel * fuel_consumption < distance

if con1 and con2:
    print("Failure, Not enough time")
elif con1:
    print("Failure, Not enough time")
elif con2:
    print("Failure, Not enough fuel")
else:
    print("Welcome to Mars")

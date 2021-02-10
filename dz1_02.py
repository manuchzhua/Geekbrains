a = int(input("Введите количество секунд = "))
h = (a // 3600)
m = (a - h * 3600) // 60
s = a - (h * 3600) - (m * 60)
hh = 0
mm = 0
ss = 0
if h < 10:
    hh = '0' + str(h)
elif h >= 10:
    hh = h
if m < 10:
    mm = '0' + str(m)
elif m >= 10:
    mm = m
if s < 10:
    ss = '0' + str(s)
elif s >= 10:
    ss = s
print("Время {}:{}:{}".format(hh, mm, ss))

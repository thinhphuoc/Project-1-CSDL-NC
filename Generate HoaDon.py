import random as r
import time as t 

start = t.time()
h = open('D:\\Fake Data\\HoaDon\\MaHD.txt','w')
for i in range(500000):
    MaKH = "HD" + str(i+1)
    h.writelines(MaKH+"\n")
h.close()

kh_list = []
m = open('D:\\Fake Data\\KhachHang\\MaKH.txt','r')
temp = m.readlines()
m.close()
for i in temp:
    kh_list.append(i)
k = open('D:\\Fake Data\\HoaDon\\MaKH.txt','w')
for i in range(500000):
    a = r.randint(0,99999)
    makh = kh_list[a]
    k.writelines(makh)
k.close()


n = open('D:\\Fake Data\\HoaDon\\NgayLap.txt','w')
for i in range(500000):
    year = r.randint(2020,2021)
    month = r.randint(5,6)
    if(month < 10):
        month = '0'+str(month)
    day = r.randint(1,30)
    if(day <10):
        day='0'+str(day)
    NgayLap = str(month)+'-'+str(day)+'-'+str(year)
    n.writelines(NgayLap+'\n')
n.close()

end = t.time()
print('Time executed: ',end-start)
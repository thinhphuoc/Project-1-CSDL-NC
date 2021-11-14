import random as r
import time as t

start = t.time()

hd_list = []
m = open('D:\\Fake Data\\HoaDon\\MaHD.txt','r')
temp = m.readlines()
m.close()
for i in temp:
    hd_list.append(i)
h = open('D:\\Fake Data\\CT_HoaDon\\MaHD.txt','w')
for i in range(1000000):
    if(i>=500000):
        mahd = 'HD'+str(i)
        h.writelines(mahd+'\n')
    else:
        mahd = hd_list[i]
        h.writelines(mahd)
    
    
h.close()

sp_list = []
n = open('D:\\Fake Data\\SanPham\\MaSP.txt','r')
temp2 = n.readlines()
m.close()
for i in temp2:
    sp_list.append(i)
sp = open('D:\\Fake Data\\CT_HoaDon\\MaSP.txt','w')
for i in range(1000000):
    a = r.randint(0,9999)
    masp = sp_list[a]
    sp.writelines(masp)
sp.close()


sl = open('D:\\Fake Data\\CT_HoaDon\\SoLuong.txt','w')
for i in range(1000000):
    soluong = r.randint(1,50)
    sl.writelines(str(soluong)+"\n")
sl.close()

gb = open('D:\\Fake Data\\CT_HoaDon\\GiaBan.txt','w')
for i in range(1000000):
    giaban = r.randint(100000,1000000)
    gb.writelines(str(giaban)+"\n")
gb.close()

gg = open('D:\\Fake Data\\CT_HoaDon\\GiaGiam.txt','w')
for i in range(1000000):
    giagiam = r.randint(10000,100000)
    gg.writelines(str(giagiam)+"\n")
gg.close()

end = t.time()

print('Time execute:',end-start)
import random as r
import time as t 

start = t.time()

m = open('D:\\Fake Data\\SanPham\\MaSP.txt','w')
for i in range(10000):
    temp = r.randint(10000000,99999999)
    MaKH = "SP" + str(temp)
    m.writelines(MaKH+"\n")
m.close()

Ten = ('Banh','Kem','Nuoc','Muc','Sua','Snack')
TraiCay = ('mo','bo','xooai','nhan','mang cut','sau rieng','thanh long','vai thieu','buoi','hong xiem','quyt','man','nho','dao','dau','nhan','cam','dua','chuoi','bap','khoai tay','rong bien','khoai tim')

sp = open('D:\\Fake Data\\SanPham\\TenSP.txt','w',encoding='UTF8')
for i in range(10000):
    sanpham = r.choice(Ten) + ' ' + r.choice(TraiCay)
    khoiluong = r.randint(100,1000)
    tensp = sanpham + ' ' + str(khoiluong)
    sp.writelines(tensp+'\n')
sp.close()

s = open('D:\\Fake Data\\SanPham\\SoLuongTon.txt','w')
for i in range(10000):
    n = r.randint(100,1000)
    SoLuongTon = str(n)
    s.writelines(SoLuongTon+'\n')
s.close()

Mota = ('San pham tot','Co ich cho suc khoe','Mau ma đep','Kieu dang tien loi','Than thien voi moi truong','Mau sac tuoi tan','Phu hop voi gia tien','Hinh anh bat mat','Thom ngon bo duong','Ngon bo re')
m = open('D:\\Fake Data\\SanPham\\Mota.txt','w',encoding='UTF8')
for i in range(10000):
    if(i%2 != 0 or i%3 ==0 ):
        a = ''
        m.writelines(a+'\n')
    else:
        temp = r.choice(Mota)
        temp = str(temp)
        m.writelines(temp+'\n')
m.close()    
   
g = open('D:\\Fake Data\\SanPham\\Gia.txt','w')
for i in range(10000):
    m = r.randint(10000,1000000)
    Gia = str(m)
    g.writelines(Gia+'\n')
g.close()


end = t.time()

print('Time executed : ',end-start)
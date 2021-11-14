import random as r
import time as t

start =t.time()
k = open('D:\\Fake Data\\KhachHang\\MaKH.txt','w')
for i in range(100000):
    MaKH = "KH" + str(i+1)
    k.writelines(MaKH+"\n")
k.close()

Ho = ('Nguyen','Tran','Le','Pham','Hoang','Huynh','Phan','Vu','Vo','Đang','Bui','Đo','Ho','Ngo','Duong','Ly')
Boy = ('Quan','Vu','Phuoc','Phuc','Dien','Danh','Kim','Long','Luong','Hung','Hieu','Minh','Luan','Huy','Hoang')
Girl = ('An','Binh','Bich','Cam','Chi','Chinh','Chau','Cat','Cuc','Dao','Diem','Diep','Duyen','Hoa','Huyen','Hue','Han','Linh','Lien','Lieu','Loan','Ly','My','Nga','Nghi','Nguyet','Phuong')

ht = open('D:\\Fake Data\\KhachHang\\HoTen.txt','w',encoding="UTF8")
for i in range(100000):
    ho = r.choice(Ho)
    if(i%2 ==0):
        ten = r.choice(Girl)
    else: 
        ten = r.choice(Boy)
    hoten = ho +' '+ ten
    ht.writelines(hoten+"\n")
ht.close()

n = open('D:\\Fake Data\\KhachHang\\Ngsinh.txt','w')
for i in range(100000):
    year = r.randint(1970,2002)
    month = r.randint(3,12)
    if(month <10):
        month = '0'+str(month)
    day = r.randint(1,30)
    if(day <10):
        day = '0'+str(day)
    Ngsinh = str(month)+'-'+str(day)+'-'+str(year)
    n.writelines(Ngsinh+"\n")
n.close()

ChuCai = ('A','B','C','D','E','F','G','H')
s = open('D:\\Fake Data\\KhachHang\\SoNha.txt', 'w')
for i in range(100000):
    temp = r.randint(1,10)
    temp2 = r.randint(11,99)
    temp3 = r.choice(ChuCai)
    SoNha = str(temp)+'/'+str(temp2)+temp3
    s.writelines(SoNha+"\n")
s.close()

Duong = ('Phung Ta Chu','Le Loi','Tran Hung Dao','To Hieu','Mạc Van Khoa','Le Van Tam','Truong Phuoc Phan','Nguyen Huu Tho','Mac Dinh Chi','Le Van Ba','Tran Van Tra','Phung Van Đien','Nguyen Trai',
'Nguyen Van Cu','Tu Liem','Nguyen Du','Le Thanh Tong','Truong Quoc Dung','Nguyen Thai Hoc','Nguyen Hien','Nguyen Van Troi','Ly Thai To','Dien Bien Phu','Tran Quoc Tuan','Duong So 6','Duong So 7')
d = open('D:\\Fake Data\\KhachHang\\Duong.txt', 'w',encoding='UTF8')
for i in range(100000):
    duong = r.choice(Duong)
    d.writelines(duong+'\n')
d.close()

Phuong = ('My Binh','My Long','My Phuoc','Chau Phu A','Chau Phu B','Kim Dinh','Long Huong','Long Toan','Phuoc Hung','Phuoc Trung','Phuong 1','Phuong 2','Phuong 3','Phuong 4','Phuong 5','Phuong 7','Phuong 8','Phuong 9','Phuong 10','Phuong 11','Phuong 12','Rach Dua')
p = open('D:\\Fake Data\\KhachHang\\Phuong.txt', 'w',encoding='UTF8')
for i in range(100000):
    phuong = r.choice(Phuong)
    p.writelines(phuong+'\n')
p.close()

Quan = ('Quan 1','Quan 2','Quan 3','Quan 4','Quan 5','Quan 6','Quan 7','Quan 8','Quan 9','Quan 10','Quan 11','Quan 12','Tan Binh','Binh Tan','Binh Chanh','Cu Chi','Thot Not','Ninh Kieu'
'Nha Be','Phu Nhuận','Go Vap','Cai Rang','Binh Thuy','O Mon','Phong Đien','Vinh Thanh','Thoi Lai','Hai Châu','Chau Thanh','Thanh Khe','Cai Lay','Cam Khe','Cam Lam','Cam Le')
q = open('D:\\Fake Data\\KhachHang\\Quan.txt', 'w',encoding='UTF8')
for i in range(100000):
    quan = r.choice(Quan)
    q.writelines(quan+'\n')
q.close()

Tpho = ('An Giang','Ba Ria Vung Tau','Bac Giang','Bac Kan','Bac Lieu','Bac Ninh','Ben Tre','Hai Duong','Binh Phuoc','Hau Giang','Kon Tum','Lam Đong','Lang Son','Long An','Nam Đinh','Ben Tre','Can Tho','TPHCM','Da Nang','Hue','Quang Nam','Quang Ngai','Quang Tri','Binh Dinh','Ca Mau','Soc Trang')
tp = open('D:\\Fake Data\\KhachHang\\Tpho.txt', 'w',encoding='UTF8')
for i in range(100000):
    if(i%2 ==0 or i%3 == 0):
        tpho = 'TPHCM'
    else:
        tpho = r.choice(Tpho)
    tp.writelines(tpho+'\n')
tp.close()

f = open('D:\\Fake Data\\KhachHang\\DienThoai.txt', 'w')
for i in range(100000):
    a = r.randint(100000000,999999999)
    phonenumber = "0" + str(a)
    f.writelines(phonenumber+"\n")
f.close()

end = t.time()

print('Time executed: ',end-start)
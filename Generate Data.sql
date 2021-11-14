use QLBH

/*Xóa toàn bộ dữ liệu trong các table
delete from HoaDon
delete from SanPham
delete from KhachHang
delete from CT_HoaDon*/

--Insert 10k rows SanPham
BULK INSERT dbo.SanPham
from 'D:\Fake Data\SanPham\SanPham.csv'
with 
(
	 FIELDQUOTE = '"',
     FIRSTROW = 2,
     FIELDTERMINATOR = ',', 
     ROWTERMINATOR = '\n',  
     TABLOCK
)
go

select * from SanPham

--insert 100k rows KhachHang
BULK INSERT dbo.KhachHang
from 'D:\Fake Data\KhachHang\KhachHang.csv'
with 
(
	 FIELDQUOTE = '"',
     FIRSTROW = 2,
     FIELDTERMINATOR = ',', 
     ROWTERMINATOR = '\n',  
     TABLOCK
)
go

select * from KhachHang

--insert 500k rows HoaDon
BULK INSERT dbo.HoaDon
from 'D:\Fake Data\HoaDon\HoaDon.csv'
with 
(
	 FIELDQUOTE = '"',
     FIRSTROW = 2,
     FIELDTERMINATOR = ',', 
     ROWTERMINATOR = '\n',  
     TABLOCK
)
go

--select * from HoaDon

--insert 1tr rows CT_HoaDon
BULK INSERT dbo.CT_HoaDon
from 'D:\Fake Data\CT_HoaDon\CT_HoaDon.csv'
with 
(
	 FIELDQUOTE = '"',
     FIRSTROW = 2,
     FIELDTERMINATOR = ',', 
     ROWTERMINATOR = '\n',  
     TABLOCK
)
go

select * from CT_HoaDon

-- Tính toán cột ThanhTien = (SoLuong * (GiaBan-GiaGiam)) của table CT_HoaDon
update CT_HoaDon 
set ThanhTien =(SoLuong * (GiaBan-GiaGiam))

--select * from CT_HoaDon

--Tính toán cột TongTien của HoaDon
update HoaDon
set TongTien = (select sum(ThanhTien) 
				from CT_HoaDon 
				where HoaDon.MaHD=CT_HoaDon.MaHD 
				group by MaHD)

--select * from HoaDon

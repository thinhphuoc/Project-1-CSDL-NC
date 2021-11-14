CREATE DATABASE QLBH	--quản lí bán hàng

/*Xóa các table
drop table CT_HoaDon
drop table HoaDon
drop table SanPham
drop table KhachHang*/

CREATE TABLE KhachHang
(
	MaKH char(10), 
	HoTen nvarchar(50), 
	Ngsinh date,
	SoNha char(20),
	Duong nvarchar(30), 
	Phuong nvarchar(30), 
	Quan nvarchar(30), 
	Tpho nvarchar(30),
	DienThoai char(10),

	constraint PK_KhachHang
	primary key (MaKH)
)

CREATE TABLE HoaDon 
(
	MaHD char(10), 
	MaKH char(10), 
	NgayLap date,  
	TongTien money,

	constraint PK_HoaDon
	primary key(MaHD)
)

CREATE TABLE CT_HoaDon 
(
	MaHD char(10), 
	MaSP char(10), 
	SoLuong int, 
	GiaBan money, 
	GiaGiam money, 
	ThanhTien money,

	constraint PK_CT_HoaDon
	primary key(MaHD,MaSP)
)

CREATE TABLE SanPham 
(
	MaSP char(10), 
	TenSP nvarchar(50), 
	SoLuongTon int, 
	Mota ntext, 
	Gia money,

	constraint PK_SanPham
	primary key(MaSP)
)

--tạo khóa ngoại

alter table HoaDon add
	constraint FK_HoaDon_KhachHang foreign key (MaKH) references KhachHang (MaKH)

alter table CT_HoaDon add
	constraint FK_CT_HoaDon_HoaDon foreign key (MaHD) references HoaDon (MaHD)

alter table CT_HoaDon add
	constraint FK_CT_HoaDon_SanPham foreign key (MaSP) references SanPham (MaSP)

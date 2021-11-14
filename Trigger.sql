create trigger trg_CT_HOADON ON CT_HoaDon
for insert,update
as
begin
	if exists(select* from inserted I
			where I.ThanhTien !=I.SoLuong*(I.GiaBan-I.GiaGiam))
	begin
		raiserror('Thanh tien khong hop le',15,1)
		rollback
	end
end

create trigger trg_HoaDon ON HoaDon
for insert,update
as
begin
	if exists(select* from inserted I
			where I.TongTien != (select sum(ThanhTien) 
							from CT_HoaDon 
							where I.MaHD=CT_HoaDon.MaHD 
							group by MaHD))
	begin
		raiserror('Tong tien khong hop le',15,1)
		rollback
	end
end
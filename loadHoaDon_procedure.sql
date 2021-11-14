USE [QLBH]
GO
/****** Object:  StoredProcedure [dbo].[load_hoadon]    Script Date: 11/14/2021 1:06:43 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER proc [dbo].[load_hoadon]
	@MaHD char(10), 
	@MaKH char(10), 
	@NgayLap datetime,  
	@TongTien money
as
begin
	select * from HoaDon
end
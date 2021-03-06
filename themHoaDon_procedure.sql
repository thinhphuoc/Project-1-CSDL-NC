USE [QLBH]
GO
/****** Object:  StoredProcedure [dbo].[themHoaDon]    Script Date: 11/14/2021 10:03:05 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER proc [dbo].[themHoaDon]
	@MaHD char(10), 
	@MaKH char(10), 
	@NgayLap datetime,  
	@TongTien money

as
begin
	set NOCOUNT ON;
	INSERT INTO HoaDon(MaHD, MaKH, NgayLap, TongTien) VALUES (@MaHD, @MaKH, @NgayLap, @TongTien)
	if @@ROWCOUNT > 0 return 1;
	else return 0;
	set NOCOUNT OFF;
end
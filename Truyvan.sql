select *
from HoaDon hd
where year (hd.NgayLap)='2020'

select*
from SanPham sp
where sp.Gia>200000 and sp.Gia <20000000

select*
from KhachHang kh
where kh.Tpho='TPHCM'

select*
from SanPham sp
where sp.SoluongTon<100




SELECT T.MASP,sp.TENSP,T.SL
FROM SANPHAM sp ,(SELECT ct.MASP,SUM (ct.SOLUONG) as SL
			FROM CT_HoaDon ct
			GROUP BY ct.MASP) as T
WHERE T.MASP=sp.MASP and T.SL >=ALL(SELECT SUM (ct.SOLUONG) as SL
			FROM CT_HoaDon ct
			GROUP BY ct.MASP )

SELECT DT.MASP,sp.TENSP,DT.d
FROM SANPHAM sp ,(SELECT ct.MASP,SUM (ct.THANHTIEN) as d
			FROM CT_HoaDon ct
			GROUP BY ct.MASP) as DT
WHERE DT.MASP=sp.MASP and DT.d>=ALL(SELECT SUM (ct.THANHTIEN) as d
			FROM CT_HoaDon ct
			GROUP BY ct.MASP)
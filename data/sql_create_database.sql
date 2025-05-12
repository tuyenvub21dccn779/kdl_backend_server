

CREATE DATABASE kho_du_lieu;

USE kho_du_lieu;

CREATE TABLE DimThoiGian (
    MaThoiGian INT PRIMARY KEY,
    Ngay DATE,
    NgayTrongTuan VARCHAR(10),
    Thang INT,
    Quy INT,
    Nam INT
);

CREATE TABLE DimThanhPho (
    MaThanhPho INT PRIMARY KEY,
    TenThanhPho VARCHAR(50),
    Bang VARCHAR(50)
);

CREATE TABLE DimKhachHang (
    Ma_KH INT PRIMARY KEY,
    TenKhachHang VARCHAR(255),
    MaThanhPho INT,
    LoaiKhachHang VARCHAR(10),
    NgayDatHangDauTien INT
);

CREATE TABLE DimCuaHang (
    MaCuaHang INT PRIMARY KEY,
    MaThanhPho INT,
    ThoiGianBatDau INT,
    SoDienThoai VARCHAR(25)
);

CREATE TABLE DimMatHang (
    MaMH INT PRIMARY KEY,
    MoTa VARCHAR(50),
    KichThuoc VARCHAR(10),
    TrongLuong FLOAT,
    Gia FLOAT,
    NgayBatDauBan INT
);

CREATE TABLE FactSales (
    ID INT PRIMARY KEY,
    MaMH INT,
    MaKH INT,
    MaThoiGian INT,
    SoLuongDat INT,
    GiaDat FLOAT,
    TongTien FLOAT
);

CREATE TABLE FactInventory (
    ID INT PRIMARY KEY,
    MaMH INT,
    MaThoiGian INT,
    MaCuaHang INT,
    SoLuongCoSan INT,
    GiaTrongNgay FLOAT,
    GiaTriTonKho FLOAT
);

-- DimKhachHang -> DimThanhPho
ALTER TABLE DimKhachHang
ADD CONSTRAINT FK_KhachHang_ThanhPho FOREIGN KEY (MaThanhPho) REFERENCES DimThanhPho(MaThanhPho);

-- DimKhachHang -> DimThoiGian
ALTER TABLE DimKhachHang
ADD CONSTRAINT FK_KhachHang_ThoiGian FOREIGN KEY (NgayDatHangDauTien) REFERENCES DimThoiGian(MaThoiGian);

-- DimCuaHang -> DimThanhPho
ALTER TABLE DimCuaHang
ADD CONSTRAINT FK_CuaHang_ThanhPho FOREIGN KEY (MaThanhPho) REFERENCES DimThanhPho(MaThanhPho);

-- DimCuaHang -> DimThoiGian
ALTER TABLE DimCuaHang
ADD CONSTRAINT FK_CuaHang_ThoiGian FOREIGN KEY (ThoiGianBatDau) REFERENCES DimThoiGian(MaThoiGian);

-- DimMatHang -> DimThoiGian
ALTER TABLE DimMatHang
ADD CONSTRAINT FK_MatHang_ThoiGian FOREIGN KEY (NgayBatDauBan) REFERENCES DimThoiGian(MaThoiGian);

-- FactSales -> DimMatHang
ALTER TABLE FactSales
ADD CONSTRAINT FK_Sales_MatHang FOREIGN KEY (MaMH) REFERENCES DimMatHang(MaMH);

-- FactSales -> DimKhachHang
ALTER TABLE FactSales
ADD CONSTRAINT FK_Sales_KhachHang FOREIGN KEY (MaKH) REFERENCES DimKhachHang(Ma_KH);

-- FactSales -> DimThoiGian
ALTER TABLE FactSales
ADD CONSTRAINT FK_Sales_ThoiGian FOREIGN KEY (MaThoiGian) REFERENCES DimThoiGian(MaThoiGian);

-- FactInventory -> DimMatHang
ALTER TABLE FactInventory
ADD CONSTRAINT FK_Inventory_MatHang FOREIGN KEY (MaMH) REFERENCES DimMatHang(MaMH);

-- FactInventory -> DimThoiGian
ALTER TABLE FactInventory
ADD CONSTRAINT FK_Inventory_ThoiGian FOREIGN KEY (MaThoiGian) REFERENCES DimThoiGian(MaThoiGian);

-- FactInventory -> DimCuaHang
ALTER TABLE FactInventory
ADD CONSTRAINT FK_Inventory_CuaHang FOREIGN KEY (MaCuaHang) REFERENCES DimCuaHang(MaCuaHang);



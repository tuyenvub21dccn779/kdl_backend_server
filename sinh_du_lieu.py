# Consolidated script to generate all tables and export as CSV

import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker and random seed
fake = Faker()
np.random.seed(42)

# Define parameters
start_date = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=5*365)
end_date = datetime.today()
dates = pd.date_range(start_date, end_date, freq='D')

# DimThoiGian
dim_thoigian = pd.DataFrame({
    'MaThoiGian': range(1, len(dates) + 1),
    'Ngay': dates,
    'NgayTrongTuan': dates.day_name(),
    'Thang': dates.month,
    'quy': ((dates.month - 1) // 3 + 1),
    'nam': dates.year
})

# DimThanhPho
dim_thanhpho = pd.DataFrame({
    'MaThanhPho': range(1, 101),
})

# DimKhachHang
n_khachhang = 1000
dim_khachhang = pd.DataFrame({
    'Ma_KH': range(1, n_khachhang + 1),
    'TenKhachHang': [fake.name() for _ in range(n_khachhang)],
    'MaThanhPho': np.random.choice(dim_thanhpho['MaThanhPho'], size=n_khachhang),
    'LoaiKhachHang': np.random.choice(['KHBD', 'KHDL', 'CAHAI'], size=n_khachhang),
    'NgayDatHangDauTien': np.random.choice(dim_thoigian['MaThoiGian'], size=n_khachhang)
})

# DimMatHang
n_mathang = 400
dim_mathang = pd.DataFrame({
    'MaMH': range(1, n_mathang + 1),
    'MoTa': [fake.word().capitalize() for _ in range(n_mathang)],
    'KichThuoc': np.random.choice(['S', 'M', 'L', 'XL'], size=n_mathang),
    'TrongLuong': np.round(np.random.uniform(0.5, 5.0, size=n_mathang), 2),
    'Gia': np.round(np.random.uniform(10000, 500000, size=n_mathang), 0),
    'NgayBatDauBan': np.random.choice(dim_thoigian['MaThoiGian'], size=n_mathang)
})

# DimCuaHang
n_cuahang = 150
dim_cuahang = pd.DataFrame({
    'MaCuaHang': range(1, n_cuahang + 1),
    'MaThanhPho': np.random.choice(dim_thanhpho['MaThanhPho'], size=n_cuahang),
    'ThoiGianBatDau': np.random.choice(dim_thoigian['MaThoiGian'], size=n_cuahang),
    'SoDienThoai': [fake.phone_number() for _ in range(n_cuahang)]
})

# FactSales
n_sales = 200000
fact_sales = pd.DataFrame({
    'ID': range(1, n_sales + 1),
    'MaMH': np.random.choice(dim_mathang['MaMH'], size=n_sales),
    'Ma_KH': np.random.choice(dim_khachhang['Ma_KH'], size=n_sales),
    'MaThoiGian': np.random.choice(dim_thoigian['MaThoiGian'], size=n_sales),
    'SoLuongDat': np.random.randint(1, 100, size=n_sales),
    'GiaDat': np.random.randint(10000, 500000, size=n_sales)
})
fact_sales['TongTien'] = fact_sales['SoLuongDat'] * fact_sales['GiaDat']

# FactInventory
n_inventory = 200000
fact_inventory = pd.DataFrame({
    'ID': range(1, n_inventory + 1),
    'MaMH': np.random.choice(dim_mathang['MaMH'], size=n_inventory),
    'MaThoiGian': np.random.choice(dim_thoigian['MaThoiGian'], size=n_inventory),
    'MaCuaHang': np.random.choice(dim_cuahang['MaCuaHang'], size=n_inventory),
    'SoLuongCoSan': np.random.randint(0, 500, size=n_inventory),
    'GiaTrongNgay': np.random.randint(10000, 500000, size=n_inventory)
})
fact_inventory['GiaTriTonKho'] = fact_inventory['SoLuongCoSan'] * fact_inventory['GiaTrongNgay']

# Save all tables to CSV
dim_thoigian.to_csv('data/DimThoiGian.csv', index=False)
dim_khachhang.to_csv('data/DimKhachHang.csv', index=False)
dim_mathang.to_csv('data/DimMatHang.csv', index=False)
dim_cuahang.to_csv('data/DimCuaHang.csv', index=False)
fact_sales.to_csv('data/FactSales.csv', index=False)
fact_inventory.to_csv('data/FactInventory.csv', index=False)

"All CSV files generated and saved."


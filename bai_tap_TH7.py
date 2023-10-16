a = int(input("Nhap so nam ma ban muon kiem tra "))
b = a % 4
c = a % 100
if b == 0 and c != 0:
    print("Nam ban nhap la nam nhuan")
else:
    print("Nam ban nhap khong phai nam nhuan")
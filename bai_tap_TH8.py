a = int(input("Nhap so thang ban muon dem: "))
if a in (1,3,5,7,8,10,12):
    print("thang " ,a, "co 31 ngay ")
elif a == 4 or a== 6 or a==  9 or a== 11:
    print(f"thang {a} co 30 ngay" )
elif a == 2:
    b = int(input("nhap so nam "))
    if b % 4 == 0 and b  % 100 != 0:
        print("thang " , a ,"co 29 ngay")
    else:
        print("thang " , a, "co 28 ngay")

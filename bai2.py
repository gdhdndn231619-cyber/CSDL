n=int(input("Nhập số phần tử của dãy: "))
A=[]
for i in range(n):
    print(f"Nhập phần tử {i+1}: ", end="")
    x=int(input())
    A.append(x)
print(A)
ds_duong=[]
ds_am=[]
ds_khong=[]
dem_duong=0
dem_am=0
dem_0=0
tong_duong=0
tong_am=0
for i in range(n):
    if A[i]>0:
        ds_duong.append(A[i])
        dem_duong=dem_duong+1
        tong_duong=tong_duong+A[i]
    elif A[i]<0:
        ds_am.append(A[i])
        dem_am=dem_am+1
        tong_am=tong_am+A[i]*-1
    else:
        ds_khong.append(A[i])
        dem_0=dem_0+1

print("Danh sách dương: ", ds_duong)
print("Danh sách âm: ", ds_am)
print("Danh sách 0: ", ds_khong)
print("Số lượng dương: ", dem_duong)
print("Số lượng âm: ", dem_am)
print("Số lượng 0: ", dem_0)
print("Tổng số dương: ", tong_duong)
print("Tổng giá trị tuyệt đối của số âm: ", tong_am)
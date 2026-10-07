n=int(input("Nhập số phần tử của dãy: "))
A=[]
for i in range(n):
    print(f"Nhập phần tử {i+1}: ", end='')
    x=float(input())
    A.append(x)
print(A)
so_sv_dat=0
so_sv_truot=0
B=[]
max=A[0]
vitri_max=0
for i in range(n):
    if A[i]>=5:
        so_sv_dat=so_sv_dat+1
    else:
        so_sv_truot=so_sv_truot+1
    if A[i]>7:
        B.append(A[i])
    if A[i]>max:
        max=A[i]
print("Số sv đạt: ", so_sv_dat)
print("Số sv trượt: ", so_sv_truot)
print("Danh sách sv có điểm>=7: ", B)
print(f"Điểm lớn nhất {max} tại vị trí {vitri_max}")

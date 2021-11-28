n = int(input("Введите число"))
k = 0
while n >0:
    n//=10
    k+=1
print(k)

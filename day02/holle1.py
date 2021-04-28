# -*- coding:UTF-8 -*-
import  keyword

print(keyword.kwlist)


print("我是中文")




score = 80
if score >= 60:
    print(score, "及格")
else:
    print(score, "不及格")

# 整數 8, 10, 16進位
a = 12  # 10進位
b = 0o12  # 8進位
c = 0x12  # 16進位
print(a, b, c)


# 浮點數
a = 3.14
b = 3.14e2  #  科學記號: 3.14e2 -> 3.14 *10**2
c = 1000e-2  # 科學記號3.14e2  -> 3.14 * 1/(10**2)
print(a, b, c)

# 賦值(=)
name , h, w, age, ispass = 'john' , 170.5, 68, 18, true
print(name , h, w, age, ispass)

#資料型態(type)
print(name, type(name))
print(h, type(h))
print(w,type(w))
print(ispass ,type(age))

# 刪除變數
print(money)
del(money)
print(money)

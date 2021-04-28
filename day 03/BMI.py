h = input('請輸入身高')
w = input('請輸入體重')
print( h, type(h))
print(w ,typa(w))
h = flost(h)  # 將 str 轉成 flost
w = flost(w)  # 將 str 轉成 flost
print(h, type(h))
prunt(w ,type(w))
bmi= w /((h/100) **2)
print("% .2f"% bmi)

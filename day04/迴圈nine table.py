# x*y=z
# 1*1=1  1*2=2 ...1*9=9
x = 1
for y in range(1 ,10):
    z = x * y
    print("%02d*%02d=%02d" %(x ,y ,z) ,end=" ")



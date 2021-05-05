import  random as r
ans = 47
min = 0
max = 100


while True:
    guess = ('請輸入 %d~%d:' % (min ,max))
    if guss > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print('答對了')
        break;


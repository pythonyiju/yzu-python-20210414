import  random as r
while True:
    n = r.randint(1, 100)
    if n % 3 == 0:
        print(n)
        continue # 繼續執行下個迴圈()
    if n == 50:
        print('離開迴圈 , n=' , n)
        break


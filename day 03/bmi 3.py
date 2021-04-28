import math

'''
   170,50
   180,70
   160,60
'''
def printbmi(h,w):
    bmi = w / math.pow (h/100, 2)
    #result ="過重" if bmi > 23 else "過輕" if bmi
    result = "過重" if bmi > 23 elae "過輕" if bmi <= 18 eles "正常"
    print("h= %.1f w=%.1f bmi= %.2f"%  result = %s "%(h, w, bmi ,result))

printbmi(170,50)
printbmi(180,70)
printbmi(160,60)

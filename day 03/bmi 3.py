import math
'''
   170,50
   180,70
   160,60
'''
def printbmi(h,w):
    bmi = w / math.pow (h/100, 2)
    print("h= %.1f w=%.1f bmi= %.2f"%  (h, w ,bmi))

printbmi(170,50)
printbmi(180,70)
printbmi(160,60)

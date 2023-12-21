import pandas as pd
def weatherprediction(t,h,W):
    w=float(((0.5)*t*t)-((0.2)*h) + ((0.1)*W)-15)
    if(w>300):
        print("sunny",w)
    elif(200<w<=300):
        print("cloudy",w)
    elif(100<w<=200):
        print("rainy",w)
    else:
        print("stormy",w)
n=int(input("enter no:of test cases"))
with open("/content/weather predicty/testcases.txt",'r') as file:
  code = file.read()
  exec(code)

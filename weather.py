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

count=0
for i in range(1,n+1):
      print("test case ",i)
      t=int(input("enter temp"))
      h= float(input("enter humidity(conver percentage into decimal)"))
      W=float(input("enter speed"))
      count+=1
      if weatherprediction(t,h,W):
        count+=1
        print(weatherprediction(t,h,W))
if (count==n):
   print("all test cases passed")

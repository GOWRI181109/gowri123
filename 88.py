gow10,ri10=map(int,input().split())
maxima=max(gow10,ri10)
while(1):
 if(maxima%gow10==0 and maxima%ri10==0):
  print(maxima)
  break
 maxima+=1

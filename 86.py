gow=list(input())
vem=[]
for j in gow:
   if j not in vem:
      vem.append(j)
if gow==vem:
   print("Yes")
else:
   print("No")

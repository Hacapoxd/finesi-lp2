limite = int(input("introduce el limite superior: "))
x,y=0,1
while y<= limite:
  print (x,",", y ,end=", ")
  x=x+y
  y=x+y
def calc(x,z,y):
  if z=='*':
    c=x*y
  elif z=='+':
    c=x+y
  elif z=='-':
    c=x-y
  elif z=='/':
    c=x/y
  else:
    c="Duzgun daxil edin"
  return c
x=int(input("X deyishenini daxil edin:"))
y=int(input("Y deyishenini daxil edin:"))
z=input("Operatoru daxil edin:")
print calc(x,z,y)

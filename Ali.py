def calc(x,y,z):
  if y=="+":
    return(x+z)
  elif y=="-":
    return(x-z)
  elif y=="/":
    return(x/z)
  elif y=="*":
    return(x*z)
  else:
    return("oops!")
  print('''comands:1,2,3,4.
1-add
2-substrac
3-multioly
4-divide''')
ask=input().split()
all=calc(int(ask[0]),ask[1],int(ask[2]))
print(all)

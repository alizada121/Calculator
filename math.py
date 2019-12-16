num1 = int(input("num1:")) 
num2 = int(input("num2:"))
process = input("symbol")
add = num1 + num2
substract = num1-num2
divide = num1//num2
multiple = num1*num2

if process == "+":
  print (add)
elif process == "-":
  print (substract)
elif process == "/":
  print (divide)
elif process == "*":
  print (multiple)
  
  

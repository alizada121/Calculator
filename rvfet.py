print('Enter 1 for Adding, Enter 2 for Substraction , Enter 3 for Multpling and Enter 4 for Dividing.')
main_q = input(': ')

if main_q == '1':
  print('Enter Numbers For Adding')
  given1 = input('Enter 1st Number Here: ')
  given2 = input('Enter 2nd Number Here: ')
  try:
    numb1 = int(given1)
    numb2 = int(given2)
    print (numb1,'+',numb2,'=',numb1+numb2)
  except ValueError:
    print("Enter Numbers Only!")
    numb1 = int(given1)
    numb2 = int(given2)

if main_q == '2':
  print('Enter Numbers For Substriction')
  given1 = input('Enter 1st Number Here: ')
  given2 = input('Enter 2nd Number Here: ')
  try:
    numb1 = int(given1)
    numb2 = int(given2)
    print (numb1,'-',numb2,'=',numb1-numb2)
  except ValueError:
    print("Enter Numbers Only!")
    numb1 = int(given1)
    numb2 = int(given2)

if main_q == '3':
  print('Enter Numbers For Multiplying')
  given1 = input('Enter 1st Number Here: ')
  given2 = input('Enter 2nd Number Here: ')
  try:
    numb1 = int(given1)
    numb2 = int(given2)
    print (numb1,'*',numb2,'=',numb1*numb2)
  except ValueError:
    print("Enter Numbers Only!")
    numb1 = int(given1)
    numb2 = int(given2)
    
if main_q == '4':
  print('Enter Numbers For Dividing')
  given1 = input('Enter 1st Number Here: ')
  given2 = input('Enter 2nd Number Here: ')
  try:
    numb1 = int(given1)
    numb2 = int(given2)
    print (numb1,'/',numb2,'=',numb1/numb2)
  except ValueError:
    print("Enter Numbers Only!")
    numb1 = int(given1)
    numb2 = int(given2)

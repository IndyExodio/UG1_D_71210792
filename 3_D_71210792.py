Diamon = int(input('\nMasukkan Angka : '))
print()
  
for i in range(Diamon):
  for j in range(Diamon-i):
    print(' ',end='')
      
  for k in range(i+1):
    print('* ',end='')
  print()
 
for i in range(1,Diamon):
  for j in range(i+1):
    print(' ',end='')
      
  for k in range(Diamon-i):
    print('* ',end='')
  print()
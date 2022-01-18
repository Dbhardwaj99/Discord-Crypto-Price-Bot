from function_callback import *

crypt_symbol = input("Enter the Symbol of cryptocurrency whose price you want to know with a $:-")


if crypt_symbol[0:6] == '$price':
  print(price(crypt_symbol[7:]))
elif crypt_symbol[0:7] == '$supply':
  print(supply(crypt_symbol[8:]))
else:
  print("Invalid Operator!")
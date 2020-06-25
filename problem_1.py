def sqrt(number):
   """
   Calculate the floored square root of a number

   Args:
      number(int): Number to find the floored squared root
   Returns:
      int: Floored Square Root
   """
   try:
      return int(number ** 0.5)
   except:
      return "Negative numbers don't have real square roots"

''' Test case 1: Positive Numbers '''
print(sqrt(100))
# Output: 10

print(sqrt(99))
# Output: 9

''' Test case 2: Zero '''
print(sqrt(0))
# Output: 0

''' Test case 3: Negative Numbers '''
print(sqrt(-1))
# Output: Negative numbers don't have real square roots
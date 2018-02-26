# Have the function OverlappingRanges(arr) take the array of numbers stored in arr which will contain 5 positive integers, the first two representing a range of numbers (a to b), the next 2 also representing another range of integers (c to d), and a final 5th element (x) which will also be a positive integer, and return the string true if both sets of ranges overlap by at least x numbers. For example: if arr is [4, 10, 2, 6, 3] then your program should return the string true. The first range of numbers are 4, 5, 6, 7, 8, 9, 10 and the second range of numbers are 2, 3, 4, 5, 6. The last element in the array is 3, and there are 3 numbers that overlap between both ranges: 4, 5, and 6. If both ranges do not overlap by at least x numbers, then your program should return the string false. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def OverlappingRanges(arr):
  x = arr[4] - 1
  l = max(arr[0], arr[2])
  h = min(arr[1], arr[3])
  if h - l >= x:
  	return 'true'
  return 'false'

# keep this function call here  
# to see how to enter arguments in Python scroll down
print OverlappingRanges(raw_input())
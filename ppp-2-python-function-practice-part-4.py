# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a,b,c):
   return max([a,b,c])
print(max_num(1,2,3))


# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(list):
   if len(list) == 0:
      return 0
   product = list[0]
   if len(list) > 1:
      for i in list[1:]:
         product = product * i
   return product

print(mult_list([1,2,3,4,5]))
   

# Write a Python function called rev_string() to reverse a string.
def rev_string(my_str):
   return my_str[::-1]






# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(a,b,c):
   if a > b and b < c:
      return True
   else:
      return False
print(num_within(3,2,4))

def num_within_two(x,a,b):
  return x in range(a,b+1)




# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

triangle = [[1], [1,1]]
def pascal(n):
    if n < 1:
      return "invalid starting point"
    elif n ==1:
       print(triangle[0])
    else:
       row_number = 2
       while len(triangle) < n:
        row = []
        row_prev = triangle[row_number - 1]
        length = len(row_prev)+1
        for i in range(length):
            #first number is 1
            if i == 0:
                row.append(1)
            #intermediate nunmbers get added from previous rows
            elif i > 0 and i < length-1:
                row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
            #last number is 1
            else:
                row.append(1)
        triangle.append(row)
        row_number += 1

        #print triangle
        for row in triangle:
            print(row)
   
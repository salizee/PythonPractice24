# 1. Check the python version you are using
import sys
print(sys.version)

# 2. Open the python interactive shell and do the following operations. The operands are 3 and 4.

print(3+4) # addition
print(3-4) # subtraction
print(3*4) # multiplication
print(3/4) # division
print(3**4) # exponentiation
print(3 % 24) # modulos
print(3//4) # floor division

# 3. Write strings on the python interactive shell. The strings are the following:
print('Lukman Aliyu Jibril')
print('Namama')
print('Nigeria')
print('I am enjoying 30 days of python')

# 4. Check the data types of the following data:
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Lukman'))
print(type('Namama'))
print(type('Nigeria'))


# Level 3 exercise
# Python data types
# Number : Integer, float, complex
a = 3 # integer
print(type(a))
b = 4.566 # float
print(type(b))
c = 4 +6j # complex
print(type(c))
# String : 
d = 'Lukman' # string
print(type(d))
# Boolean :
e = True # boolean
print(type(e))
# List:
f = ['Aisha',3,7.6,True,False,['elephant']] #square brackets
print(type(f))
# Tuple:
g = ("red","green") #round brackets
print(type(g))
# Set :
h = {1,3,4,5} # set - curly brackets
print(type(h))
# Dictionary: 
i = {'goat':7,'dog':8,'elephant':9}
print(type(i))

#euclidian distance
# import math module
import math
print(math.dist([2,3],[10,8]))

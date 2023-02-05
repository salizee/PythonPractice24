# Day 3: 30 days of python programming

age = 28
height = 1.76
comp = 1 + 7j

# script one

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
b = float(input("Enter base:"))
h = float(input("Enter height:"))
area = 0.5 * b * h 
print("The area of the triangle is: ", area)


# script two
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
# Calculate the perimeter of the triangle (perimeter = a + b + c).

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c

print("The perimeter of the triangle is: ", perimeter)


# script three
# Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) and perimeter 
# (perimeter = 2 x (length + width))

length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
area = length * breadth
print("The area of the rectangle is ",area, " square meters")


# Get radius of a circle using prompt. 
# Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14
import math
r = float(input("Input the radius of the circle: "))
area = math.pi * r ** 2
perimeter = 2 * math.pi * r 
print("The area of the circle is: ",area, " and ", "the perimeter is : ", perimeter)


# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# The slope is 2 (coefficiet of x) and does not need to be calculated
# x- intercept is the value of x when y = 0
# y- intercept is the value of y when x = 0
y = 2 * 0 - 2
x = ( 2 * 0 ) / 2
print("The x-intercept of y = 2x-2 is: ",x, " and ", "the y-intercept is: ", y)


# Slope is (m = y2-y1/x2-x1). 
# Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
x1,y1,x2,y2 = 2,2,6,10
m = (y2 - y1) / (x2 - x1)
# euclidean distance,d =  square root of squared distances
d2 = ((y2 - y1) ** 2) + ((x2 - x1) ** 2 )
d = math.sqrt(d2)
print("The slope is: ", m, "and the Euclidean distance is:" ,d)


# Compare the slopes in tasks 8 and 9.
# The slope for the task 8 is 2 and that for task 9 is 4
# using code, I'll let the slope for task 8 to be m0 since that for task 9 is m
m0 = 2
m = 4
print("Equal: ", m0==m, "Unequal: ", m0 != m)
# checking which is greater or less
print("Greater than: ", m0 > m, "Less than: ", m0 < m)

# Calculate the value of y (y = x^2 + 6x + 9). 
# Try to use different x values and figure out at what x value y is going to be 0.
# using the input function, I tried different values and reducing the value until I got the value of -3. 
# I did not use my knowledge of quadratic equations
#
x = int(input("Value of x: "))
y = x ** 2 + 6 * x + 9
print("Value of y: ", y)


#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# still deciding whether to adopt single or double quotes
print("Length of python: ", len('python'), "length of dragon: ", len('dragon'))
print("Definitely false: ", len('python')> len('dragon'))

# Use 'and' operator to check if 'on' is found in both 'python' and 'dragon'
print("Checking for 'on': " 'on' in ('python' and 'dragon'))



# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargon in sentence: ", 'jargon' in 'I hope this course is not full of jargon')

# There is no 'on' in both dragon and python
print("There is no 'on' in both dragon and python: ", 'on' not in ('dragon' and 'python'))

# Find the length of the text python and convert the value to float and convert it to string
a = len('python')
b = float(a)
c = str(a)
print("Length, float and string: ",a,b,c)


# Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?
# using the modulos operator, which gives the remainders,
#  e.g. x%2 == 0 will be true if x is even and false if x is odd
x = 5
print("x is even: ", x%2==0)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print("Checking: ", 7 // 3 == 2.7) # definitely not!!!


# Check if type of '10' is equal to type of 10
print("Cheking again!: ", type('10')== type(10)) # not equal, of course!

# Check if int('9.8') is equal to 10
print("Checking yet again: ", int('9.8') == 10) # it raised a ValueError: invalid literal for int() with base 10: '9.8

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
x = float(input("Enter hours per week:"))
y = float(input("Enter rate per hour: "))
z = x * y
print("Your weekly earning is: ", z)

# Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter the number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60 # 365 days, 24 hours, 60 minutes, 60 seconds
# my skills can't account for leap years yet
print("You have lived for ",seconds, " seconds.")

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

# can't figure out an exact answer, used ChatGPT and got a close match which doesnt give the first column
# here it is: 
for i in range(1, 6):
    for j in range(1, 5):
        print(i ** (j-1), end=" ")
    print()


## Using escape sequences

print('1\t1\t1\t1\t1\n2\t1\t2\t4\t8\n3\t1\t3\t9\t27\n4\t1\t4\t16\t64\n5\t1\t5\t25\t125')


# using this to remember the arguments for the print function
for i in range(1, 6):
    for j in range(1, 5):
        print(f'{i ** (j-1)}', end=" ")
    print()

# finally, this worked
for i in range(1,6):
    line = ''
    for j in (1,0,1,2,3):
        line += str(i**j) + ' '
    print(line)


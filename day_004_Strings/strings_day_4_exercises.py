# Day 4: 30 days of python programming

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# option 1
print(' '.join(['Thirty','Days','Of','Python']))
# option 2: less elegant 
print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')

# Concatenate the string 'Coding', 'For' , 'All' into a single string, 'Coding For All'.
print(' '.join(['Coding','for','all']))

# Declare a variable named company and assign it to the initial value "Coding For All".
company = 'Coding For All'
# Print the variable company using print().
print(company)
# Print the length of the company string using len() method and print()
print(len(company))
# Change all the characters to uppercase letters using upper() method
print(company.upper())
# Change all the characters to lowercase letters using lower() method
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
print(company.capitalize())
# the rest
company.swapcase(),
company.title()

# Cut(slice) out the first word of Coding For All string.
print(company[0:6])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
# remember Coding For All is still company on this script. That's why assignment is good. 3 ways, same result
print('Using .index(): ', company.index('Coding')) 
print('Using .rindex(): ', company.rindex('Coding')) 
print('Using .find(): ',company.find('Coding')) 

# Replace the word coding in the string 'Coding For All' to Python
print('Coding for all'.replace('Coding','Python'))
print(company.replace('Coding','Python'))

# Change Python for Everyone to Python for All using the replace method or other methods
print('Python for everyone'.replace('everyone','all'))

# Split the string 'Coding For All' using space as the separator (split()) 
print('Coding For All'.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))

# What is the character at index 0 in the string Coding For All ?
print('Coding For All'[0])   # assigning will waste typing time if string will be used only once
print(company[0]) # letter C

# What is the last index of the string Coding For All ? technically the last index is -1 but we get the question
print('Coding For All'[-1]) 
print(company[-1])   # l

# What character is at index 10 in "Coding For All" string ?
print(company[10])    # space

# Create an acronym or an abbreviation for the name 'Python For Everyone'
# I understood that I am just to assign:
# e.g. 
# pfe = 'Python For Everyone'
# However, I can loop to get the acronym or abbreviation, as follows:
sentence = 'Python For Everyone'
word = sentence.split()
acc = ''
for i in word:
    print(i[0],end='.')
# prints P.F.E

# second option
sentence = 'Python For Everyone'
word = sentence.split()
acc = ''
for i in word:
    acc+= i[0] + '.'
print('Accronym: ',acc)

acc.rstrip('.')
acc
# so many possibilities: interesting


# Create an acronym or an abbreviation for the name 'Coding For All'
cfa = 'Coding For All'
# Use index to determine the position of the first occurrence of C in Coding For All
print(cfa.index('C'))    # 0
# Use index to determine the position of the first occurrence of F in Coding For All.
print(cfa.index('F')) # 7

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print('Coding For All People'.rfind('l'))  # 19

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))  #31

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind('because'))   #47

# Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:47 + len('because')])
# This problem gave me an intuition regarding the usefulness of all the previous methods. Making me think !!!

# Does ''Coding For All' start with a substring Coding?
# made the sentence cfa
print(cfa.startswith('Coding'))  # True// meaning,  Yes of course

# Does 'Coding For All' end with a substring coding?
print(cfa.endswith('coding'))   # False = meaining of course not !!!

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
string = '   Coding For All      '  # better to assign, less mistakes
print(string.rstrip())

# Which one of the following variables return True when we use the method isidentifier():
## 30DaysOfPython
## thirty_days_of_python  #obviously this, but let's check
print('30DaysOfPython: ','30DaysOfPython'.isidentifier()) # False : as expected
print('thirty_days_of_python: ','thirty_days_of_python'.isidentifier()) # True

# The following list contains the names of some of python libraries: 
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
# Join the list with a hash with space string.
print('# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')

# Use a tab escape sequence to write the following lines:
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')
# got it in one line: Nice !!!
print('Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square

radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {int(area)} meters square.')


# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

a = 8
b = 6

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')






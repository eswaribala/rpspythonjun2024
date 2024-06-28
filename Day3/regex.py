# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 21:14:12 2018

@author: Balasubramaniam
"""

import re

str = "I will be travelling travelling  availing"
x = re.findall("av", str)
print(x)

#empty list
x = re.findall("we", str)
print(x)


#search for white space characters
str = "Group will be travelling travelling"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())

#split

str = "Group will be travelling travelling"
x = re.split("\s", str)
print(x)


#split cell only at first occurrence

str = "Group will be travelling travelling"
x = re.split("\s", str,1)
print(x)

#replace every white space with _


str = "Group will be travelling travelling"
x = re.sub("\s", "_", str)
print(x)


#match - matches only in the beginning
result = re.match(r'AV', 'AV Studio AV')
print (result)

print (result.group(0))

#match - matches only in the beginning
result = re.match(r'Analytics', 'AV Analytics AV')
print (result) 


#compile
pattern=re.compile('Group')
result=pattern.findall('Group will be travelling travelling')
print (result)
pattern=re.compile('AV')
result2=pattern.findall('AV is largest analytics community of India')
print (result2)

#extract each character
result=re.findall(r'\w','AV is largest Analytics community of India')
print (result)

#extract each word
result=re.findall(r'\w+','AV is largest Analytics community of India')
print (result)


#return word at the end of string
result=re.findall(r'\w+$','AV is largest Analytics community of India')
print (result)

#first 2 characters from each word
result=re.findall(r'\b\w.','AV is largest Analytics community of India')
print (result)

#find word after @
result=re.findall(r'@\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz') 
print (result) 


#find word after @
result=re.findall(r'@\w+.\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz') 
print (result) 

#extract only domain
result=re.findall(r'@\w+.(\w+)','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print (result)

#return date from string
result=re.findall(r'\d{2}-\d{2}-\d{4}','Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print (result)




#return year from string
result=re.findall(r'\d{2}-\d{2}-(\d{4})','Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print (result)

#phone number matching
li=['9999999999','999999-999','99999x9999']
for val in li:
 if re.match(r'[8-9]{1}[0-9]{9}',val) and len(val) == 10:
     print ('yes')
 else:
     print ('no')


str="""
<tr align="center"><td>1</td> <td>Noah</td> <td>Emma</td></tr>
<tr align="center"><td>2</td> <td>Liam</td> <td>Olivia</td></tr>
<tr align="center"><td>3</td> <td>Mason</td> <td>Sophia</td></tr>
<tr align="center"><td>4</td> <td>Jacob</td> <td>Isabella</td></tr>
<tr align="center"><td>5</td> <td>William</td> <td>Ava</td></tr>
<tr align="center"><td>6</td> <td>Ethan</td> <td>Mia</td></tr>
<tr align="center"><td>7</td> <td HTML>Michael</td> <td>Emily</td></tr>
"""

result=re.findall(r'<td>\w+</td>\s<td>(\w+)</td>\s<td>(\w+)</td>',str)
print (result)

#word followed by an
str = 'an example word:deaf!!'
match = re.search(r'an \w+', str)
# If-statement after search() tests if it succeeded
if match:
  print ('found', match.group()) ## 'found word:cat'
else:
  print ('did not find')
  
#looks for any word starts G  
str = "Group will be travelling travelling"
x = re.search(r"\bG\w+", str)
#Print the position (start- and end-position) of the first match occurrence.
print(x.span())  
  
#Print the string passed into the function:

str = "Group will be travelling travelling"
x = re.search(r"\bG\w+", str)
print(x.string)  




#Print the part of the string where there was a match
str = "Group will be travelling travelling"
x = re.search(r"\bt\w+", str)
print(x.group())  






# . - A period. Matches any single character except newline character.
print(re.search(r'Co.k.e', 'Cookie').group())

# + - Checks for one or more characters to its left.
re.search(r'Co+kie', 'Cooookie').group()

# Checks for any occurrence of a or o or both in the given sequence
re.search(r'Ca*o*kie', 'Caokie').group()

email_address = "Please contact us at: support@test.com, xyz@test.com"

# 'addresses' is a list that stores all the possible match
addresses = re.findall(r'[\w\.-]+@[\w\.-]+', email_address)
for address in addresses:
  print(address)

str = "Customer number: 232454, Date: February 12, 2011"
items = re.findall("[0-9]+.*: .*", str)

print(items)

str = "The destination is Paris!"
mo = re.search(r"destination.*(London|Paris|Zurich|"
               r"Strasbourg)", str)
if mo: print(mo.group())

regex = r"[A-z]{1,2}[0-9R][0-9A-Z]?[0-9][ABD-HJLNP-UW-Z]{2}"
address = "BBC News Centre, London, W12 7RJ"
compiled_re = re.compile(regex)
res = compiled_re.search(address)
print(res)

metamorphoses = "OF bodies chang'd to various forms, I sing: Ye Gods, from whom these miracles did spring, Inspire my numbers with coelestial heat;"

print(re.split("\W+", metamorphoses))

print("Changing the month....")
str = " Task to complete ELK Stack by 23 july 2018."
# res = re.sub("[0-9]{4}","2020", str)
res = re.sub("(june|july|august|september)", "December", str)
print(res)

# to find 3 letter word
str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
  print('found', match.group())  ## 'found word:cat'
else:
  print('did not find')

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
  print(match.group())  ## 'b@google'

import re

example_codes = ["SW1A 0AA",  # House of Commons
                 "SW1A 1AA",  # Buckingham Palace
                 "SW1A 2AA",  # Downing Street
                 "BX3 2BB",  # Barclays Bank
                 "DH98 1BT",  # British Telecom
                 "N1 9GU",  # Guardian Newspaper
                 "E98 1TT",  # The Times
                 "TIM E22",  # a fake postcode
                 "A B1 A22",  # not a valid postcode
                 "EC2N 2DB",  # Deutsche Bank
                 "SE9 2UG",  # University of Greenwhich
                 "N1 0UY",  # Islington, London
                 "EC1V 8DS",  # Clerkenwell, London
                 "WC1X 9DT",  # WC1X 9DT
                 "B42 1LG",  # Birmingham
                 "B28 9AD",  # Birmingham
                 "W12 7RJ",  # London, BBC News Centre
                 "BBC 007"  # a fake postcode
                 ]

pc_re = r"[A-z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}"

for postcode in example_codes:
  r = re.search(pc_re, postcode)
  if r:
    print(postcode + " matched!")
  else:
    print(postcode + " is not a valid postcode!")

s = "Sun Oct 14 13:47:03 CEST 2012"

expr = r"\b(?P<hours>\d\d):(?P<minutes>\d\d):" \
       r"(?P<seconds>\d\d)\b"
x = re.search(expr, s)
print(x.group('hours'))
print(x.group('minutes'))


re_pattern=r"[A-Z]{5,25}"

userName=input("Enter Name")

result=re.search(re_pattern,userName)
if(result):
    print("Match Found")
else:
    print("Match not found")


re_pattern = r"(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{4,})"
password = input("Enter Password")
result = re.search(re_pattern, password)
if (result):
  print("Match Found")
else:
  print("Match not found")
  
  
  
import re

pattern = '^a...s$'
test_string = 'aby'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")

pattern = '[abc]'
test_string = 'abb'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")

pattern = '..'
test_string = 'axx'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")

pattern = '[a-zA-Z0-9]{4,8}$'
test_string = 'a1234255'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")

pattern = '\ARPS'
test_string = 'The RPS Consulting'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")

pattern = 'foo\\b'
test_string = 'ballfoo'
result = re.search(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")

pattern = '\d{3}-\d{3}-\d{4}$'
test_string = '995-203-2862'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")

pattern = '\s'
test_string = 'The RPS'
result = re.search(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")

pattern = '\w'
test_string = 'The RPS  12_04_2019%$'
result = re.search(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")

pattern = '[a-zA-Z]+'
test_string = 'The RPS  12 04 2019%$'
result = re.findall(pattern, test_string)

print(result)

pattern = '\s'
test_string = 'The RPS 12-04-2019%$'
result = re.split(pattern, test_string,2)

print(result)

pattern = '\s+'
test_string = 'The     RPS 12-04-2019%$'
replace_string='-'
result = re.sub(pattern, replace_string,test_string)

print(result)


print(re.search('c..k..','cookie is good cookie for health').group())

email_address = "Please contact us at: " \
                "support@gmail.com, xyz@test.com"

#'addresses' is a list that stores all the possible match
addresses = re.findall(r'[\w\.-]+@[gmail\.-]+\w+', email_address)
for address in addresses:
    print(address)

str="Customer number: 232454, Date: February 12, 2011"
#items = re.findall("[0-9]+.*: .*",str )
items = re.findall(".*: \d+",str )
print(items)

str = "The destination is Zurich!"
mo = re.search(r"destination.*(London|Paris|Zurich|"
               r"Strasbourg)",str)
if mo: print (mo.group())

regex = r"[A-z]{1,2}[0-9R][0-9A-Z]\s\w+"
address = "BBC News Centre, London, WzRW 7AR"
compiled_re = re.compile(regex)
res = compiled_re.findall(address)
print(res)

example_codes = ["SW1A 0AA", # House of Commons
                 "SW1A 1AA", # Buckingham Palace
                 "SW1A 2AA", # Downing Street
                 "BX3 2BB", # Barclays Bank
                 "DH98 1BT", # British Telecom
                 "N1 9GU", # Guardian Newspaper
                 "E98 1TT", # The Times
                 "TIM E22", # a fake postcode
                 "A B1 A22", # not a valid postcode
                 "EC2N 2DB", # Deutsche Bank
                 "SE9 2UG", # University of Greenwhich
                 "N1 0UY", # Islington, London
                 "EC1V 8DS", # Clerkenwell, London
                 "WC1X 9DT", # WC1X 9DT
                 "B42 1LG", # Birmingham
                 "B28 9AD", # Birmingham
                 "W12 7RJ", # London, BBC News Centre
                 "BBC 007" # a fake postcode
                ]

pc_re = r"[A-z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}"

for postcode in example_codes:
    r = re.search(pc_re, postcode)
    if r:
        print (postcode + " matched!")
    else:
        print (postcode + " is not a valid postcode!")

s = "Sun Oct 14 13:47:03 CEST 2012"


expr = r"\b(?P<hours>\d\d):(?P<minutes>\d\d):" \
       r"(?P<seconds>\d\d)\b"
x = re.search(expr,s)
print(x.group('hours'))
print(x.group('minutes'))
print(x.group('seconds'))

s = "Sun Oct 14 13:47:03 CEST 2012"
expr = r"\d{2}:\d{2}:\d{2}"
x = re.findall(expr,s)
print(x)
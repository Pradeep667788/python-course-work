Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name = input()
pradeep
name
'pradeep'
name = input("Enter your name")
Enter your name: pradeeep
name
': pradeeep'
age = input("enter your age")
enter your age : 30

age
' : 30'
type(age)
<class 'str'>
gpa = float(input("Enter the Gpa: ") )
Enter the Gpa: 8.0
type(gpa)
<class 'float'>
'pradeep vishnu yaswanth sudheer'
'pradeep vishnu yaswanth sudheer'
'pradeep vishnu yaswanth sudheer'split( )
SyntaxError: invalid syntax
name = input("enter the name: ").split( )
enter the name: pradeep vishnu sudheer yaswanth
products = input("enter the products: ").split()
enter the products: laptop mouse keyboard charger
products
['laptop', 'mouse', 'keyboard', 'charger']
topics = tuple(input("Enter the topics: ").split())
Enter the topics: laptop mouse keyboard charger
topics
('laptop', 'mouse', 'keyboard', 'charger')
list(map(int,input("enter the marks: ").split()) )
enter the marks: 1 3 5 7 99
[1, 3, 5, 7, 99]
prices = tuple(map(int,input("enter the prices: ").split()) )
enter the prices: 333 444 555 666
prices
(333, 444, 555, 666)
rating = set(map(int,input("enter the rating: ").split()) )
enter the rating: 3 5 6 7 
rating
{3, 5, 6, 7}
per = list(map(float,input("enter the per's : ").split()) )
enter the per's : [44.2 44.3 33.5]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    per = list(map(float,input("enter the per's : ").split()) )
ValueError: could not convert string to float: '[44.2'
per = list(map(float,input("enter the per's : ").split()) )

enter the per's : 59.4 44.5 66.6 77. 7
per
[59.4, 44.5, 66.6, 77.0, 7.0]
prices = tuple(map(float,input("enter the prices: ").split()) )
enter the prices: 777 666 555 444
prices
(777.0, 666.0, 555.0, 444.0)
prices = set(map(float,input("enter the prices: ").split()) )
enter the prices: 888 666 777 888
prices
{888.0, 777.0, 666.0}
>>> a,b = 10,20
>>> a
10
>>> 
>>> b
20
>>> a,b = [20,30]
>>> a
20
>>> b
30
>>> username,password = input("enter the username & password: ").split()) )
SyntaxError: unmatched ')'
>>> username,password = input("enter the username & password: ").split()) )
... username,password = input("enter the username & password: ").split())
SyntaxError: unmatched ')'
>>> username,password = input("enter the username & password: ").split()
enter the username & password: pradeep r123
>>> username
'pradeep'
>>> password
'r123'
>>> a,b,c,d = list(map(int,input("enter the 4 sides: ").split()))
enter the 4 sides: 1 2 3 4

>>> a
1
>>> b
2
>>> c
3
>>> d
4
>>> price,discount = list(map(float,input().split()) )
6565656 88.9
>>> price
6565656.0
>>> discount
88.9
>>> a = eval(input())
56476
>>> a
56476
>>> a = eval(input())
678.99
>>> a
678.99
a eval(input())
SyntaxError: invalid syntax
a = eval(input())
(1,2,4,5)
a
(1, 2, 4, 5)
KeyboardInterrupt
a = eval(input())
[1,3,4,5]

a
[1, 3, 4, 5]
a = eval(input())
(3:3, 5:5, 5:66)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a = eval(input())
  File "<string>", line 1
    (3:3, 5:5, 5:66)
      ^
SyntaxError: invalid syntax
a = eval(input())
(3: 5, 5: 6)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a = eval(input())
  File "<string>", line 1
    (3: 5, 5: 6)
      ^
SyntaxError: invalid syntax
'python programming lang'
'python programming lang'
type(s)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    type(s)
NameError: name 's' is not defined
a = 'codegnan'
b = 'trp'
a
'codegnan'
b
'trp'
a+b
'codegnantrp'
a+b
'codegnantrp'
a*10
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
'pradeep '*1000

'pradeep '*1000
'pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep pradeep '
'
SyntaxError: unterminated string literal (detected at line 1)

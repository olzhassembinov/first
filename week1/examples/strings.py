print("Hello")
print('Hello')
a = "Hello"
print(a)
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
a = "Hello, World!"
print(a[1])
for x in "banana":
  print(x)
a = "Hello, World!"
print(len(a))
txt = "The best things in life are free!"
print("free" in txt)
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
txt = "The best things in life are free!"
print("expensive" not in txt)
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:5])
b = "Hello, World!"
print(b[:5])
b = "Hello, World!"
print(b[2:])
b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())
a = "Hello, World!"
print(a.lower())
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
a = "Hello, World!"
print(a.replace("H", "J"))
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello"
b = "World"
c = a + b
print(c)
a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."
txt = 'It\'s alright.'
print(txt)
txt = "This will insert one \\ (backslash)."
print(txt) 
txt = "Hello\nWorld!"
print(txt) 
txt = "Hello\rWorld!"
print(txt) 
txt = "Hello\tWorld!"
print(txt) 
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

a = 'hi exeryone, if you check it all, please take it easy on me'
a = a.capitalize()#	Converts the first character to upper case
a = a.casefold()#	Converts string into lower case
a = a.center()#	Returns a centered string
a = a.count()#	Returns the number of times a specified value occurs in a string
a = a.encode()#	Returns an encoded version of the string
a = a.endswith()#	Returns true if the string ends with the specified value
a = a.expandtabs()#	Sets the tab size of the string
a = a.find()#	Searches the string for a specified value and returns the position of where it was found
a = a.format()#	Formats specified values in a string
a = a.format_map()#	Formats specified values in a string
a = a.index()#	Searches the string for a specified value and returns the position of where it was found
a = a.isalnum()#	Returns True if all characters in the string are alphanumeric
a = a.isalpha()#	Returns True if all characters in the string are in the alphabet
a = a.isascii()#	Returns True if all characters in the string are ascii characters
a = a.isdecimal()#	Returns True if all characters in the string are decimals
a = a.isdigit()#	Returns True if all characters in the string are digits
a = a.isidentifier()#	Returns True if the string is an identifier
a = a.islower()#	Returns True if all characters in the string are lower case
a = a.isnumeric()#	Returns True if all characters in the string are numeric
a = a.isprintable()#	Returns True if all characters in the string are printable
a = a.isspace()#	Returns True if all characters in the string are whitespaces
a = a.istitle()#	Returns True if the string follows the rules of a title
a = a.isupper()#	Returns True if all characters in the string are upper case
a = a.join()#	Joins the elements of an iterable to the end of the string
a = a.ljust()#	Returns a left justified version of the string
a = a.lower()#	Converts a string into lower case
a = a.lstrip()#	Returns a left trim version of the string
a = a.maketrans()#	Returns a translation table to be used in translations
a = a.partition()#	Returns a tuple where the string is parted into three parts
a = a.replace()#	Returns a string where a specified value is replaced with a specified value
a = a.rfind()#	Searches the string for a specified value and returns the last position of where it was found
a = a.rindex()#	Searches the string for a specified value and returns the last position of where it was found
a = a.rjust()#	Returns a right justified version of the string
a = a.rpartition()#	Returns a tuple where the string is parted into three parts
a = a.rsplit()#	Splits the string at the specified separator, and returns a list
a = a.rstrip()#	Returns a right trim version of the string
a = a.split()#	Splits the string at the specified separator, and returns a list
a = a.splitlines()#	Splits the string at line breaks and returns a list
a = a.startswith()#	Returns true if the string starts with the specified value
a = a.strip()#	Returns a trimmed version of the string
a = a.swapcase()#	Swaps cases, lower case becomes upper case and vice versa
a = a.title()#	Converts the first character of each word to upper case
a = a.translate()#	Returns a translated string
a = a.upper()#	Converts a string into upper case
a = a.zfill()#	Fills the string with a specified number of 0 values at the beginning


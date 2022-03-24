# BROAD REASONS WHY YOU MIGHT GET AN EXCEPTION
# (1) Trying to refer to something that doesn't exist
# (2) Using a value that is inappropriate in some way
#
# CORE EXAMPLES OF EXCEPTIONS IN THIS FILE
# AttributeError (1)
# KeyError (1)
# IndexError (1)
# NameError (1)
# UnboundLocalError (1)
# TypeError (2)
# ValueError (2)
# ZeroDivisionError (2)
# OverflowError (2)
# FileNotFoundError (1)
# UnicodeEncodeError (2)
# ModuleNotFoundError (1)
# ImportError (1)
#
# BONUS EXAMPLES YOU CAN TRY IF YOU WISH
# PermissionError (2)
# IsADirectoryError (2)


# AttributeError - EXAMPLE
def produce_attribute_error():
    print(1.234.upper())


# KeyError
food_prices = {
    'milk':  1.2,
    'apples': 0.5,
    'oranges': 0.34,
    'cucumber': 0.7
    }
def produce_key_error():
        print(food_prices['bread'])
# key_error()


# IndexError
drinks = ['beer', 'wine', 'water', 'juice', 'coffee']
def produce_index_error():
    print(drinks[8])
# produce_index_error()

# NameError
def produce_name_error():
    print(b)
# produce_name_error()

# UnboundLocalError
def produce_unbound_local_error():
    print(a)
    a = 'How are you?'
# produce_unbound_local_error()


# TypeError
def produce_type_error():
    name = 'Ayan'
    age = 23
    print(name+age)
# produce_type_error()

# ValueError
import math
def produce_value_error():
    b = math.sqrt(-5)
    print(b)
# produce_value_error()

# ZeroDivisionError
def produce_zero_division_error():
    a = 5 //0
    print(a)
# produce_zero_division_error()

# OverflowError

def produce_overflow_error():
    a = 10.0
    b = a**1000000000000
    print(b)
# produce_overflow_error()

# FileNotFoundError
def produce_file_not_found_error():
    with open('todo5.txt', 'r') as todofile:
        read = todofile.read()
        print(read)
# produce_file_not_found_error()
# UnicodeEncodeError

def produce_unicode_encode_error():
    print(type(NULL))
# produce_unicode_encode_error()

# ModuleNotFoundError()

def produce_module_not_found_error():
   import b
# produce_module_not_found_error()

# ImportError
def produce_import_error():
    from math import time
# produce_import_error()

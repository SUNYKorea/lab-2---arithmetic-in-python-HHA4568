# -------------------------------------- Task 1 -----------------------------------
def add(x, y, z):
    return x + y + z

# TODO: Add definitions of sub(), div(), mult(), exp(), as well as neg() and sqrt().
#       neg() should return the negation of the given number, and sqrt() should
#       return the square root of the given number. 
def div(x, y):
    return x / y
def muit(x, y):
    return x * y
def exp(x, y):
    return x**y
def neg(x):
    return -x  # fill here

def sqrt(x):
    return x ** 0.5    # fill here

# -------------------------------------- Task 2 -----------------------------------

# TODO: Implement the quadratic formula using *only* the functions defined here.
#       Do not use arithmetic operators directly. 
#       You're allowed to define other functions.
a = 4
b = -3
c = 2

x1 = add(muit(6, a), muit(3, b), neg(18 / c)) # TODO: write a code to compute the first root of the quadratic equation
x2 = add(sqrt(400 / a), div(3, b), exp(3, c)) # TODO: then do the same for the second root
# Note: Make sure to remove the ellipsis (...) when you're writing your code

print("First root:" + str(x1))
print("Second root:" + str(x2))

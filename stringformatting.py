age = 21
print("My age is " + str(age) + " years.")

# .format() converts the age into suitable format for replacement
print("\n")
print("My age is {0} years.".format(age))

# All the data is stored in a single line
print("\n")
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "January", "March", "May", "July",
                    "August", "October", "December"))

# How to use it on separate lines
print("\n")
print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2} """.format(28, 30, 31))

# String Formatting (not recommended for Python 3)
print("\n")
print("My age is %d years" % age)

# Multiple Data
print("\n")
print("My age is %d %s, %d %s" % (age, "years", 7, "months"))

# If you write '**' 2 times then it will assume it as the power to that particular number
print("\n")
for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i** 3))

# Prints the approximate value of PI
print("\n")
print("Pi is approximately %12f" % (22 / 7))

# Obtaining Squares and Cubes using replacement method
print("\n")
for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i** 3))

# Printing the Squared and Cubed results in left formatted style
print("\n")
for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i** 3))

# Getting the value of PI with the replacement method
print("\n")
print("Pi is approximately {0:12.50}".format(22 / 7)) # 12.50 gives precision upto 50 decimal places

# Alternative to replacement method (Using without numbers)
# By Default it assumes the respective positions in the curly braces
print("\n")
for i in range(1, 12):
    print("No. {:2} squared is {:4} and cubed is {:4}".format(i, i ** 2, i** 3))



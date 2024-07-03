# Taking an integer input for the multiplication table
num = int(input("Enter a number: "))

# Initializing the counter
i = 1

# Printing the multiplication table using a while loop
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

name = "Vasu"  # String Variable
age = 30 # Integer variable
height = 1.75 # Float variable
is_student = True # Boolean Variable

# Printing the values
print ("Name:", name)
print ("Age:", age)
print ("Height:", height)
print ("Is student:", is_student)

# 2. Multiple Variable Assignment
# Assigning the same value to multiple variables
x = y = z = 100
print ("x:", x, "y:", y, "z:", z)

# Assigning different values to multiple variables
first_name, last_name, city = "Bob", "Smith", "New York"
print("Full Name:", first_name, last_name, "from", city)

# 3. Variable Re-assignment and Type Changing:
# Initial Assignment
my_var = "Hello"
print ("Iniital Value:", my_var, "Type:", type (my_var))

# Re-assign with different data type
my_var = 123
print ("New Value:", my_var, "Type:", type (my_var))

# 4. Using Variables in calculations
num1 = 15
num2 = 7

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
division_result = num1 / num2

print ("Sum:", sum_result)
print ("Difference", difference_result)
print ("Product", product_result)
print ("Division", division_result)

# 5. Getting User input with variables:
user_name = input("Enter your name:")
print ("Hello,", user_name)

# Getting numerical input and converting its type
user_age_str = input ("Enter your age:")
user_age_int = int(user_age_str) # Convert stringto integer
print ("You are", user_age_int, "years old.")
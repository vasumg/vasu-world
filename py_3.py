name = "Vasumathi"
print (name.upper())
str1 = "Muddu"
str2 = "Baby"
result = str1 + str2
print (result)
text = "Python is important"
length = len(text)
print ("Length of the string", length)
greeting = "Hello"
name = "MudduBaby"
full_message = greeting +", " + name + "!"
print (full_message)
# Repetition using the * operator
repeat_string = "vasu" * 3
print (repeat_string)

# String Indexing and Slicing
my_string = "Programming"
first_char = my_string[0]
fifth_char = my_string[5]
last_char = my_string[-1]

print (f"First_Character: {first_char}")
print (f"Fifth_Character: {fifth_char}")
print (f"Last_Character: {last_char}")

# Slicing to extract substrings
substring1 = (my_string[0:4])
substring2 = (my_string[4:])
substring3 = (my_string[:3])
print (f"Substring1 : {substring1}")
print (f"Substring2 : {substring2}")
print (f"Substring3 : {substring3}")

# 4. String Methods (e.g., upper(), lower(), replace(), split(), join()):
text_1 = " Learning Python is Essential "

# Converting Case
uppercase_text = text_1.upper()
lowercase_text = text_1.lower()
print(f"Uppercase: {uppercase_text}")
print(f"Lowercase: {lowercase_text}")

# Removing Loading/trailing whitespace
stripped_text = text_1.strip()
print(f"Stripped: '{stripped_text}'")

#Replacing Substrings
new_text = text_1.replace("Essential", "Fun")
print(f"Replaced: '{new_text}'")

# Splitting a string into List
words = "apple, banana, orange".split(',')
print(f"Split: {words}")
belts = ("white", "blue", "purple", "black", "orange")
for belt in belts:
     if "black" in belt:
           print ("The belt I want to be is :", belt)
     else:
           print ("This is not the belt I want to end up at:", belt)


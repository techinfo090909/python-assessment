
# Question 5: Reverse a String

text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

print("Reversed string:", reverse)

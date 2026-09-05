print("Hello World")

text = input("Enter a string: ")
reverse = text[::-1]
print("Reversed string:", reverse)

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

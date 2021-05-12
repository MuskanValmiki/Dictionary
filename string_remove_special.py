a_string = "abc !? 123"
alphanumeric = ""
for character in a_string:
    if character.isalnum():
        alphanumeric += character
print(alphanumeric)

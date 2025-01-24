import keyword # Imports a tool that can be used to check if a string is a keyword in python

print(keyword.iskeyword("Hello World")) # This string should return a False
print(keyword.iskeyword("and")) # This string should return a True